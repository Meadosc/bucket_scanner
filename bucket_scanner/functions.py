"""
Functions for usage by main to process data
"""
import os
import json


def test_1(chunk, fname):
	print(fname)


def save_data(data, fname, foundby):
	print("\nSaving data...")
	fname = os.path.splitext(fname)[0] # strip file extensions
	components = str.split(fname, '/')
	name = components[-1]
	date = components[2]
	
	data['fname'] = fname
	data['foundby'] = foundby
	with open(f"results/individual/{date}-{name}", 'w') as fp:
		json.dump(data, fp)	
	print("Done.\n")


def find_company_ids(data_list, fname):
	""" for a list of company ids, find and save the locations """
	for i, data in enumerate(data_list):
		try:
			data_id = data['doc']['source_id']
		except KeyError:
			data_id = data['doc']['id']

		comp_id = [11159, 9079, 100569, 575263, 391850]
		if data_id in comp_id:
			print(f"\n company id {data_id} found in:\n    {fname}")
			print(f"    name: {data['doc']['name']}")
			save_data(data, fname, 'id')

		comp = ['salesforce', 'google', 'twitter', 'uber', 'airbnb']
		if str.lower(data['doc']['name']) in comp:
			print(f"\n company name {comp} found in:\n    {fname}")
			print(f"    name: {data['doc']['name']}")
			save_data(data, fname, 'name')
