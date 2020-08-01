from flask import Flask, render_template, send_from_directory, request, redirect
from datetime import datetime
import random
import string
import os
import sys
import time
import subprocess



app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
random.seed(datetime.now())

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

    
    uploaded_file = request.files['file']
    
    if uploaded_file.filename != '':
        uploaded_file.save('/home/ubuntu/fawkes/app/tmp/' + uploaded_file.filename)
    else:
        fname = get_random_string(12)
        uploaded_file.save('/home/ubuntu/fawkes/app/tmp/' + fname)


    try:
        logs = subprocess.check_output("python3 /home/ubuntu/fawkes/fawkes/protection.py -d /home/ubuntu/fawkes/app/tmp/ -m %s" % fawkes_mode, shell=True)
    except subprocess.CalledProcessError as e:
        return "Processing error!\n"

    return "That worked!\n"

if __name__ == '__main__':
  app.run()
