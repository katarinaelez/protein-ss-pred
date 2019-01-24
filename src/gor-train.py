#!/usr/bin/env python

from __future__ import print_function
from utils import parse_pssm, parse_dssp

import sys

if __name__ == "__main__":
	
	try:
		import argparse
		import numpy as np
	except ImportError as e:
		print('This program requires Python 2.7+ and numpy', file=sys.stderr)
		raise ImportError(e)

	parser = argparse.ArgumentParser(description='Train the GOR method on PSSM and DSSP files.')
	parser.add_argument('filename_id_list', type=str, help='File containing a list of ids.')
	parser.add_argument('dir_pssm', type=str, help='Directory containing the PSSM files.')
	parser.add_argument('dir_dssp', type=str, help='Directory containing the DSSP files.')
	parser.add_argument('--filename_model', type=str, default='model', help='Name for the model file. Default is "model".')
	parser.add_argument('--window_size', type=int, default=17, help='Size of the window to be considered when building the model. Default is 17.')
	args = parser.parse_args()

	with open(args.filename_id_list) as id_list:
		
		model = {}
		model['H'] = np.zeros((args.window_size,20),dtype=float)
		model['E'] = np.zeros((args.window_size,20),dtype=float)
		model['-'] = np.zeros((args.window_size,20),dtype=float)
	
		for line in id_list:
			line = line.rstrip()
			profile = np.array(parse_pssm(args.dir_pssm+'/'+line+'.pssm'))
			if np.sum(profile) != 0:
				ss = parse_dssp(args.dir_dssp+'/'+line+'.dssp')
				ss = ss.replace('C','-')
				for i in range(0, len(profile)):
					half_window_size = int((args.window_size-1)/2)
					for j in range(max(0,i-half_window_size), min(i+half_window_size+1,len(profile))):
						for k in range(0, len(profile[i])):
							matrix = model[ss[i]]
							matrix[j-i+half_window_size][k] += float(profile[j][k])
							model[ss[i]] = matrix
	
		model['H'] = np.divide(model['H'], np.sum(model['H'], axis=1).reshape(17,1))
		model['E'] = np.divide(model['E'], np.sum(model['E'], axis=1).reshape(17,1))
		model['-'] = np.divide(model['-'], np.sum(model['-'], axis=1).reshape(17,1))
		np.savez(args.filename_model+'.npz', model=model)
