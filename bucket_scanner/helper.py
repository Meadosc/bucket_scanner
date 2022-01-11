"""
Collection of minor helper functions and classes
"""

import yaml


class Constants:
	def __init__(self):
		with open('constants.yaml', 'r') as f:
			constants = yaml.safe_load(f)
		self.constants = constants
		self.prefix = constants['prefix']
		self.prefix_start = constants['prefix_start']
		self.bucket = constants['s3_bucket_name']
	
