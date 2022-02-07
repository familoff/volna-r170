from flask import Flask, render_template, request, redirect, url_for
import datetime
import os


#UPLOAD_FOLDER = "data/data"
#ALLOWED_EXTENSIONS = {'txt', 'py', }


app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['POST', 'GET'])
def index():
  count = 0
  if request.method == "POST":
    count += 1
    return redirect('/', count=count)
  else:
    return render_template('index.html', count=count)

  
  
  
