import os
import json
import boto3
import ast
import datetime
from urllib import parse

from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, NumberAttribute, MapAttribute


def lambda_handler(event, context):
