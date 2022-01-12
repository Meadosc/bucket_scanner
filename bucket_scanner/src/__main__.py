"""
Iterate over dictionaries and find the unique keys
"""
import os
import json

from s3_fetcher import get_s3_data
from functions import test_1, find_company_ids




def main(func):
	""" func is a function that receives and processes the data pulled by
	get_s3_data.
	"""
	s3_gen = get_s3_data()
	for data, fname in s3_gen:
		print(fname)
		func(data, fname)	



if __name__ == '__main__':
	main(find_company_ids)
