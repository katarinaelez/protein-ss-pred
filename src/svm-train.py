#!/usr/bin/env python

from __future__ import print_function
from utils import parse_pssm, parse_dssp

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

	parser = argparse.ArgumentParser(description='Train the SVM method on PSSM and DSSP files.')
	parser.add_argument('filename_id_list', type=str, help='File containing a list of ids.')
	parser.add_argument('dir_pssm', type=str, help='Directory containing the PSSM files.')
	parser.add_argument('dir_dssp', type=str, help='Directory containing the DSSP files.')
	parser.add_argument('--filename_model', type=str, default='model', help='Name for the model file. Default is "model".')
	parser.add_argument('--window_size', type=int, default=17, help='Size of the window to be considered when building the model. Default is 17.')
	args = parser.parse_args()

	with open(args.filename_id_list) as id_list:
		
		X, y = [], []

		ss_map = {'H': 0, 'E': 1, 'C': 2, '-': 2}

		for line in id_list:
			line = line.rstrip()
			profile = np.array(parse_pssm(args.dir_pssm+'/'+line+'.pssm'))
			if np.sum(profile) != 0:
				ss = parse_dssp(args.dir_dssp+'/'+line+'.dssp')
				for i in range(0, len(profile)):
					half_window_size = int((args.window_size-1)/2)
					part1 = np.zeros(20*max(0, half_window_size-i))
					part2 = np.ndarray.flatten(profile[max(0,i-half_window_size):min(i+half_window_size+1,len(profile))])
					part3 = np.zeros(20*max(0, half_window_size-(len(profile)-i-1)))
					vec = np.concatenate((part1, part2, part3))
					X.append(vec.tolist())
					y.append(ss_map[ss[i]])

		X, y = np.array(X), np.array(y)
	
		model = svm.SVC(kernel='rbf',C=1,gamma=0.125,probability=True)
		model.fit(X, y)
		pickle.dump(model, open(args.filename_model+'.sav', 'wb'))
