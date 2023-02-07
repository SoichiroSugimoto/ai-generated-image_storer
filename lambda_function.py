import os
import json
import boto3
import datetime

import io
import os
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation


def lambda_handler(event, context):
  # APIインタフェースの準備
  stability_api = client.StabilityInference(
      key=os.environ['STABILITY_KEY'],
      verbose=True,
  )

  # テキストからの画像生成
  answers = stability_api.generate(
      prompt="Beautiful mirror under the sea",
  )

  # 結果の出力
  for resp in answers:
      for artifact in resp.artifacts:
          if artifact.finish_reason == generation.FILTER:
              print("NSFW")
          if artifact.type == generation.ARTIFACT_IMAGE:
              img = Image.open(io.BytesIO(artifact.binary))
              img.save('output.png')