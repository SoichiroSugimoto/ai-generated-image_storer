import io
import os
import time
import json
import boto3
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

s3 = boto3.resource('s3')
BUCKET_NAME = "ai-generated-image"

def request_validation(params):
  auth_token = os.getenv['AUTH_TOKEN']
  if (params.token != auth_token):
    return False
  return True

def lambda_handler(event, context):
  stability_api = client.StabilityInference(
    key=os.getenv['STABILITY_KEY'],
    verbose=True,
  )

  receive_body = json.parse(event['body'])
  prompt_text = json.loads(receive_body['text'])
  answers = stability_api.generate(
    prompt=prompt_text
  )

  for resp in answers:
    for artifact in resp.artifacts:
      if artifact.finish_reason == generation.FILTER:
        print("NSFW")
        return {
        'statusCode': 204
        }
      if artifact.type == generation.ARTIFACT_IMAGE:
        img = Image.open(io.BytesIO(artifact.binary))
        bucket = s3.Bucket(BUCKET_NAME)
        object_key_name = str(time.time()) + '.png'
        obj = bucket.Object(object_key_name)
        r = obj.put(img)
        return {
        'statusCode': 200
        }