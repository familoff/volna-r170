from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == "POST":
    
    return redirect('/')
  else:
    return render_template('index.html')

  
