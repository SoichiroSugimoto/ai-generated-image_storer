#! /bin/bash

# remove
touch ai-generated-image_storer.zip
rm ai-generated-image_storer.zip
cd stability-sdk-api

# compress
zip -r stability-sdk-api ./*
cd ..

if [ ! -f ./lambda_layer.zip ]; then
  mkdir python
  pip install -t ./python numpy --upgrade
  pip install -t ./python requests
  pip install -t ./python pynamodb
  pip install -t ./python stability-sdk
  zip -r ./lambda_layer.zip ./python
  rm -r ./python
fi