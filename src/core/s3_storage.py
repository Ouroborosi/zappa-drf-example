import boto3
import botocore
import json
import uuid

from django.conf import settings

from core.sotrage import Storage

def _get_s3_resource():
    return boto3.resource('s3')

# def _check_bucket():

def _upload_to_s3_bucket(key, json_data):
    try:
        upload_file = bytes(json.dumps(json_data).encode('UTF-8'))

        # if _check_bucket():
        bucket = _get_s3_resource().Bucket(settings.STORAGE_S3_BUCKET)
        bucket.put_object(Key=key, Body=upload_file)
    except botocore.exceptions.ClientError as e:
        logging.error(e)
        return False
    return True

def _read_from_s3_bucket(key):
    try:
        content_object = _get_s3_resource().Object(key)
        file_content = content_object.get()['Body'].read().decode('utf-8')
        json_content = json.loads(file_content)
    except botocore.exceptions.ClientError as e:
        logging.error(e)
        return False
    return True

class Task(Storage):
    def get(self, id: uuid, condition: dict = None):
        logging.error('Not implement yet.')

    def save(self, data):
        data['id'] = str(uuid.uuid4())
        _upload_to_s3_bucket(data['id'], data)
        return data
    
    def delete(self, id: uuid):
        logging.error('Not implement yet.')