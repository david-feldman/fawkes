from flask import Flask, render_template, send_from_directory, request, redirect
from datetime import datetime
import random
import string
import os
import sys
import time
import subprocess
from base64 import b64decode
from fawkes.protection import Fawkes
from format_demo_output import format_demo_output
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
random.seed(datetime.now())
protector = Fawkes("high_extract", "0", 1)

def get_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@app.route('/')
def hello_world():
  return 'Hello from Flask!'

@app.route("/process/<mode>", methods=["POST"])
def process(mode):
    
    if mode == 'user':
        fawkes_mode = 'low'
    elif mode == 'celeb':
        fawkes_mode = 'mid'
    elif mode == 'prom_celeb':
        fawkes_mode = 'high'
    else:
        return "Incorrect mode specification!\n"
    
    fname = get_random_string(12)
    print(request.form['file'][0:100])
    with open('/home/ubuntu/fawkes/app/tmp/' + fname + '.png',"wb") as f:
        f.write(b64decode(request.form['file'].split('base64,')[1]))
    file_ra = ['/home/ubuntu/fawkes/app/tmp/' + fname + '.png']


    try:
        protector.run_protection(file_ra, mode=fawkes_mode, th=.01, sd=1e9, lr=2, max_step=1000, batch_size=1, format="png", separate_target=True, debug=False)
    except Exception as inst:
        return "Something went wrong!\n"

    out_url = format_demo_output(fname, '/home/ubuntu/fawkes/app/tmp/' + fname + '.png', '/home/ubuntu/fawkes/app/tmp/' + fname + '_' + fawkes_mode + '_cloaked' + '.png')
    return out_url

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0", port=80, ssl_context='adhoc')
