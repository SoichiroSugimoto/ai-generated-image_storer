import io
import os
import time
import boto3
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

s3 = boto3.resource('s3')
BUCKET_NAME = "ai-generated-image"

def lambda_handler(event, context):
  stability_api = client.StabilityInference(
    key=os.environ['STABILITY_KEY'],
    verbose=True,
  )

  answers = stability_api.generate(
    prompt="Beautiful mirror under the sea"
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