from flask import Flask, render_template, send_from_directory, request, redirect
from datetime import datetime
import random
import string
import os
import sys
import time
import subprocess
from fawkes.protection import Fawkes


app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
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
    
    uploaded_file = request.files['file']
    fname = get_random_string(12) + '.png' # this is a lie and a hack
    uploaded_file.save('/home/ubuntu/fawkes/app/tmp/' + fname )
    file_ra = ['/home/ubuntu/fawkes/app/tmp/' + fname]


    try:
        protector.run_protection(file_ra, mode=fawkes_mode, th=.01, sd=1e9, lr=2, max_step=1000, batch_size=1, format="png", separate_target=True, debug=False)
    except Exception as inst:
        return "Processing error!\n"

    return "That worked!\n"

if __name__ == '__main__':
    app.debug = True
    app.run()
