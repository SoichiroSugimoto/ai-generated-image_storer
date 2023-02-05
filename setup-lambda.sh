#! /bin/bash

# remove
touch ai-generated-image_storer.zip
rm ai-generated-image_storer.zip
cd ai-generated-image_storer

# compress
zip -r ../ai-generated-image_storer.zip ./*
cd ..

if [ ! -f ./lambda_layer.zip ]; then
  mkdir python
  pip install -t ./python numpy --upgrade
  pip install -t ./python requests
  pip install -t ./python pynamodb
  pip install -t ./python stability-sdk
  zip -r ./lambda_layer.zip ./python
fi