#!/usr/bin/env python

from __future__ import print_function
from utils import parse_pssm, parse_fasta, seq_to_profile

import sys

if __name__ == "__main__":

	try:
		import argparse
		import numpy as np
	except ImportError as e:
		print('This program requires Python 2.7+ and numpy', file=sys.stderr)
		raise ImportError(e)

	parser = argparse.ArgumentParser(description='Use the GOR method to predict protein secondary structure from a PSSM or from a FASTA file.')
	group = parser.add_mutually_exclusive_group(required=True)
	group.add_argument('--pssm', type=str, help='File containing the PSSM profile.')
	group.add_argument('--fasta', type=str, help='File containing the FASTA sequence.')
	parser.add_argument('filename_model', type=str, help='File containing the GOR model.')
	args = parser.parse_args()

	model = np.load(args.filename_model)['model'].item()

	if args.pssm:
		profile = parse_pssm(args.pssm)
	else:
		profile = seq_to_profile(parse_fasta(args.fasta))
	
	dssp = ''

	for i in range(0, len(profile)):
		half_window_size = int((len(model['-'])-1)/2)
		score_H, score_E, score_C = 0, 0, 0
		for j in range(max(0,i-half_window_size), min(i+half_window_size+1,len(profile))):
			for k in range(0, len(profile[i])):
				score_H += profile[j][k] * model['H'][j-i+half_window_size][k]
				score_E += profile[j][k] * model['E'][j-i+half_window_size][k]
				score_C += profile[j][k] * model['-'][j-i+half_window_size][k]
		scores = [score_H, score_E, score_C]
		dssp += ['H', 'E', '-'][scores.index(max(scores))]

	print(dssp)
