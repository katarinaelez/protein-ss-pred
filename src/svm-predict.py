#!/usr/bin/env python

from __future__ import print_function
from utils import parse_pssm, parse_fasta, seq_to_profile

import sys

if __name__ == "__main__":

	try:
		import argparse
		import pickle
		import numpy as np
		from sklearn import svm
	except ImportError as e:
		print('This program requires Python 2.7+, numpy and scikit-learn', file=sys.stderr)
		raise ImportError(e)

	parser = argparse.ArgumentParser(description='Use the SVM method to predict protein secondary structure from a PSSM or from a FASTA file.')
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('--pssm', type=str, help='File containing the PSSM profile.')
	group.add_argument('--fasta', type=str, help='File containing the FASTA sequence.')
	parser.add_argument('--probs', action='store_true', help='Output class probabilities together with the prediction.')
	parser.add_argument('filename_model', type=str, help='File containing the model.')
	args = parser.parse_args()

	model = pickle.load(open(args.filename_model, 'rb'))

	if args.pssm:
		profile = np.array(parse_pssm(args.pssm))
	else:
		profile = np.array(seq_to_profile(parse_fasta(args.fasta)))
	
	dssp = ''

	for i in range(0, len(profile)):
		half_window_size = int((len(model.support_vectors_[0])/20-1)/2)
		part1 = np.zeros(20*max(0, half_window_size-i))
		part2 = np.ndarray.flatten(profile[max(0,i-half_window_size):min(i+half_window_size+1,len(profile))])
		part3 = np.zeros(20*max(0, half_window_size-(len(profile)-i-1)))
		vec = np.concatenate((part1, part2, part3))
		if args.probs:
			probs = model.predict_proba(vec.reshape(1, -1))[0]
			dssp += ' '.join([str(round(prob, 3)).rjust(5) for prob in probs])
			dssp += ' ' + ['H', 'E', '-'][np.argmax(probs)] + '\n'
		else:
			dssp += ['H', 'E', '-'][model.predict(vec.reshape(1, -1))[0]]
	
	if args.probs:
		dssp = dssp[:-1]
	print(dssp)
