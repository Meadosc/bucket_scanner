"""
Fetch data from aws S3
"""
import gzip
import json

import boto3
import yaml


class Constants:
	def __init__(self):
		with open('constants.yaml', 'r') as f:
			constants = yaml.safe_load(f)
		self.constants = constants
		self.prefix = constants['prefix']
		self.prefix_start = constants['prefix_start']
		self.bucket = constants['s3_bucket_name']
	

def get_s3_data_chunk():	
	"""	Get s3 data chunk from prefix defined in constants.yaml """
	const= Constants()
	s3 = boto3.resource('s3')
	bucket = s3.Bucket(name=const.bucket)
	s3_keys = [obj.key for obj in bucket.objects.filter(Prefix=const.prefix)]
	start = f"{const.prefix}{const.prefix_start}"	
	s3_keys = [key for key in s3_keys if key >= start and key.endswith('json.gz')]

	for fname in s3_keys:
		obj = s3.Object(bucket_name=const.bucket, key=fname)
		data = obj.get()['Body'].read() # read raw bytes
		data = gzip.decompress(data) # decompress from gzip
		data = json.loads(data) # read json data
		yield data, fname

