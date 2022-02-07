# Author: Megana Boddam
# CSS 532: IoT Final Project: lightSense
# Date: 12/9/2021
# Goal: Program for Raspberry Pi to subscribe to messages on the topic 
#       "lightSense", operate the prototype, and publish the corresponding 
#       data to the S3 bucket for storage. 

import json
import boto3
from datetime import datetime

s3 = boto3.client('s3')
    
# input event: a message that contains "message" and "sequence number" in json object
# output: the output message in json object form will contain message, sequence number, 
#           core name, reception time, and the string "forwarded upstream" 
#         this will be sent to the S3 bucket "meganahw3data" with "sequence".json" 
#         as file name.
def lambda_handler(event, context):
    bucket = 'meganahw3data'
    fileName = str(event["sequence"]) + ".json"
    output = {"device_name": event["message"]}
    output["sequence"] = event["sequence"]
    output["core_name"] = "megana_hw3_Core"
    output["reception_time"] = datetime.now().strftime("%H:%M:%S")
    output["message_from_core"] = "forwarded upstream"
    uploadByteStream = bytes(json.dumps(output).encode('UTF-8'))
    s3.put_object(Bucket = bucket, Key = fileName, Body = uploadByteStream)
    