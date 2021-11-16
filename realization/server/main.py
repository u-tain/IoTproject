import base64
import binascii
import io
import json
import pickle

import PIL
from flask import Flask, request, jsonify, Response, render_template, flash, url_for, make_response, send_file
import requests
from PIL import Image
from io import BytesIO
import numpy as np
from matplotlib import pyplot as plt
app = Flask(__name__)




@app.route('/photo', methods=['POST', 'GET'])
def photo():
    r = request.get_data()
    try:
        with open(r'C:\Users\s7911\Downloads\zkEDnrQ3dtE.jpg', mode='rb') as file:
            img = file.read()
        image1 = make_response(img)
        image1.headers['Content-Type'] = 'image/jpg'
        data = r'http://c6f43a7f90a5.ngrok.io/photo'
        res = requests.post(r'http://c6f43a7f90a5.ngrok.io', data=data)
        return image1
    except FileNotFoundError as e:
        return Response(response='error', status=200)


@app.route('/', methods=['GET', 'POST'])
def home():
    r = request.get_data()
    data = {'url': r'http://c6f43a7f90a5.ngrok.io/photo'}
    res = json.dumps(data)
    response = make_response(res)
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.run(debug=True)