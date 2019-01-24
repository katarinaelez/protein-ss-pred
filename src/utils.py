#!/usr/bin/python

def parse_pssm(pssm_filename):
	profile = []
	with open(pssm_filename) as pssm:
		pssm_lines = pssm.readlines()
		for line in pssm_lines[3:-6]:
			profile_line = []
			for n in line.rstrip().split()[22:-2]:
				profile_line.append(float(n)/100)
			profile.append(profile_line)
	return profile

def parse_dssp(dssp_filename):
	ss = ''
	with open(dssp_filename) as dssp:
		dssp.readline()
		ss = dssp.readline().rstrip()
	return ss

def parse_fasta(fasta_filename):
	seq = ''
	with open(fasta_filename) as fasta:
		fasta.readline()
		seq = fasta.readline().rstrip()
	return seq

def seq_to_profile(seq):
	profile = []
	aa_list = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
	for res in seq:
		profile_line = []
		for aa in aa_list:
			if res == aa:
				profile_line.append(1)
			else:
				profile_line.append(0)
		profile.append(profile_line)
	return profile
