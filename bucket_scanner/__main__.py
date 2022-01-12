"""
Iterate over dictionaries and find the unique keys
"""
import os
import json
from glob import glob

from s3_fetcher import get_s3_data
from functions import test_1, find_company_ids




def collect_results():
	""" after data is retrieved and saved, collect multiple files 
	and make a single file
	"""	
	all_data = []
	for fname in glob("results/individual/*.json"):
		with open(fname, 'r') as fp:
			data = json.load(fp)
		all_data.append(data)
	with open("results/companies.json", 'w') as fp:
		json.dump(data, fp)



def main(func):
	""" func is a function that receives and processes the data pulled by
	get_s3_data.
	"""
	s3_gen = get_s3_data()
	for data, fname in s3_gen:
		print(fname)
		func(data, fname)	
	collect_results() # debug


if __name__ == '__main__':
	main(find_company_ids)
