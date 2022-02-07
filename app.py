from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

count = 0
@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == "POST":
    global count
    count += 1
    return redirect('/')
  else:
    return render_template('index.html', count=count)

  
