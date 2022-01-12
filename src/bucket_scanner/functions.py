"""
Functions for usage by main to process data
"""
import os
import json
from glob import glob

def test_1(chunk, fname):
	print(fname)


def save_data(data, fname):
	print("\nSaving data...")
	fname = os.path.splitext(fname)[0] # strip file extensions
	components = str.split(fname, '/')
	name = components[-1]
	date = components[2]
	
	data['fname'] = fname
	with open(f"results/individual/{date}-{name}", 'w') as fp:
		json.dump(data, fp)	
	print("Done.\n")


def collect_results():
	""" after data is retrieved and saved, collect multiple files 
	and make a single file
	"""	
	all_data = []
	for fname in glob("results/individual/*.json"):
		data = json.load(fname)
		all_data.append(data)
	with open("results/companies.json", 'w') as fp:
		json.dump(data, fp)


def find_company_ids(data_list, fname):
	""" for a list of company ids, find and save the locations """
	for i, data in enumerate(data_list):
		try:
			comp_id = 'salesforce' 
			if str.lower(data['doc']['name']) == comp_id:
				print(f"\n company id {comp_id} found in:\n    {fname}")
				print(f"    name: {data['doc']['name']}")
				save_data(data, fname)
		except KeyError:
			print(fname)
			print(json.dumps(data, indent=4))
