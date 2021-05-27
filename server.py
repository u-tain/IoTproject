import base64
import binascii
import io
import json
from PIL.ImageShow import show
from flask import Flask, request, jsonify, Response, render_template, flash, url_for, make_response, send_file
import requests
from PIL import Image
from io import BytesIO
import numpy as np
from matplotlib import pyplot as plt
app = Flask(__name__)




@app.route('/', methods=['POST', 'GET'])
def home():
    request.get_data()
    r = request.get_data()
    try:
        data = base64.b64decode(r + b'==')
        image = io.BytesIO(data)
        image1 = make_response(Image.open(image))
        image1.headers['Content-Type'] = 'image/jpeg'
        return image1
    except FileNotFoundError as e:
        return Response(response='error', status=200)


if __name__ == '__main__':
    app.run(debug=True)