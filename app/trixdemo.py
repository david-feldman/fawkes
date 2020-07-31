from flask import Flask, render_template, send_from_directory, request, redirect
import os
from PIL import Image
from datetime import datetime

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

import random
import string
random.seed(datetime.now())

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

@app.route('/')
def hello_world():
  return 'Hello from Flask!'

@app.route('/multiply/<num>')
def multiply(num):
    return 'Result: ' + str(int(num)*12)
@app.route("/process", methods=["POST"])
def process():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save('/home/ubuntu/fawkes/app/tmp/' + uploaded_file.filename)
    return "That worked!\n"

if __name__ == '__main__':
  app.run()
