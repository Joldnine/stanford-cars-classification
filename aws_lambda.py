try:
    import unzip_requirements
except ImportError:
    pass

import os
import io
import json
import time

import boto3
import requests
import PIL

import torch
import torch.nn.functional as F
from torchvision import transforms


def initialize():
    s3 = boto3.client('s3')
    MODEL_BUCKET = os.environ.get('MODEL_BUCKET')
    MODEL_KEY = os.environ.get('MODEL_KEY')
    CLASSES_TXT_KEY = os.environ.get('CLASSES_TXT_KEY')

    preprocess = transforms.Compose([
        transforms.Resize(299),
        transforms.CenterCrop(299),
        transforms.ToTensor(),
    ])

    obj = s3.get_object(Bucket=MODEL_BUCKET, Key=MODEL_KEY)
    model = io.BytesIO(obj['Body'].read())
    model = torch.jit.load(model, map_location=torch.device('cpu')).eval()

    obj = s3.get_object(Bucket=MODEL_BUCKET, Key=CLASSES_TXT_KEY)
    classes = obj['Body'].read().splitlines()

    return model, classes, preprocess


MODEL, CLASSES, PREPROCESS = initialize()


def input_fn(img_request):
    img = PIL.Image.open(io.BytesIO(img_request.content))
    img_tensor = PREPROCESS(img)
    img_tensor = img_tensor.unsqueeze(0)
    return img_tensor


def predict(input_object):
    predict_values = MODEL(input_object)
    preds = F.softmax(predict_values, dim=1)
    conf_score, indx = torch.max(preds, dim=1)
    predict_class = CLASSES[indx]
    response = {}
    response['class'] = str(predict_class, 'utf-8')
    response['confidence'] = "{:.2%}".format(conf_score.item())
    
    return response


def get_response(body_dict, code):
    return {
        'statusCode': code,
        'body': json.dumps(body_dict),
        'headers': {
            "Access-Control-Allow-Origin": os.environ.get('CORS'),
            "Access-Control-Allow-Credentials": True
        }
    }


def lambda_handler(event, context):
    start_time = time.time()
    
    request_body = event['body']
    if isinstance(request_body, str):
        request_body = json.loads(request_body)

    if not request_body['url'].endswith('.jpg'):
        return get_response({'error': 'Not a valid jpg image.'}, 200)

    img_request = requests.get(request_body['url'], stream=True)
    if img_request.status_code != 200:
        return get_response({'error': 'Not a valid url.'}, 200)

    input_object = input_fn(img_request)
    response = predict(input_object)
    
    response['time'] = "{:.2f} ms".format((time.time() - start_time) * 1000)
    return get_response(response, 200)
