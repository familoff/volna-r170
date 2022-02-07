from flask import Flask, render_template, request, redirect, url_for
import datetime
import os


#UPLOAD_FOLDER = "data/data"
#ALLOWED_EXTENSIONS = {'txt', 'py', }


app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


count = 0
@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == "POST":
    global count
    count += 1
    return redirect('/')
  else:
    return render_template('index.html', count=count)

  
  
  
