#trixdemo.wsgi
import sys
sys.path.insert(0, '/var/www/html/trixdemo')
sys.path.insert(0, '/home/ubuntu/fawkes/app/venv/lib/python3.6/site-packages')

from trixdemo import app as application
