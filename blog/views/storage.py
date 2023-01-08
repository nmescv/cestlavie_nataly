import os
import uuid

import boto3
from botocore.exceptions import NoCredentialsError

from cestlavie_nataly import settings

session = boto3.session.Session()
s3 = session.client(
		service_name='s3',
		aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
		aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
		region_name=settings.AWS_DEFAULT_REGION,
		endpoint_url=settings.ENDPOINT_URL
		)


def upload(bucket_name, object_name):
	try:
		extension = os.path.splitext(object_name)[-1].lower()
		s3_file_path = "{0}{1}".format(uuid.uuid1(), extension)
		s3.upload_file(object_name, bucket_name, s3_file_path)
		print("Upload Successful")
		return True
	except FileNotFoundError:
		print("The file was not found")
		return False
	except NoCredentialsError:
		print("Credentials not available")
		return False


def delete(bucket_name, s3_file_path):
	try:
		s3.delete_object(Bucket=bucket_name, Key=s3_file_path)
	except FileNotFoundError:
		print("The file was not found")
		return False
	except NoCredentialsError:
		print("Credentials not available")
		return False


def download(bucket_name, s3_file_path):
	s3.download_file(bucket_name, s3_file_path, s3_file_path)


if __name__ == '__main__':
	result = upload('cestlavie-nataly-storage', 'bridge.jpg')
	print(result)
	# delete('cestlavie-nataly-storage', '737a5f80-8f4f-11ed-bd4c-acde48001122.jpg')