from flask import Flask
from flask import render_template
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response 

import pymysql 
import json
app = Flask(__name__,static_url_path='')


@app.route('/basichttp')
def basichttp():
    if request.args.get('myvar') is not None:
        return 'your var:' + request.args.get('myvar')
    else:
        return 'myvar not set' 

@app.route('/')
def home():
    return render_template('test.html', title='Test', msg='Welcome!')

@app.route('/index')
def index():
    user = {'username': 'Tyler'}
    items = [
        {'name':'Apple','price':2.34},
        {'name':'Orange','price':4.88},
        {'name':'Grape','price':2.44}
    ]
    return render_template('index.html', title='Home', user=user, items=items)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
   app.secret_key = '1234'
   app.run(host='127.0.0.1',debug=True)