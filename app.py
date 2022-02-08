from flask import Flask, render_template, request, redirect, url_for
import random


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
  if request.method == "POST":
    
    x1 = str(round(random.uniform(0.74, 0.81), 2))
    if x1 == "0.8":
    x1 = "0.80"
    #print("'0,775±0,070'       {0}   {0}".format(x1))
  
    x2 = str(round(random.uniform(2.6, 3.2), 1))
    #print("'2,5, не менее'     {0}    {0}".format(x2))

    x3 = str(round(random.uniform(3.2, 3.9), 1))
    #print("'2,7, не менее'     {0}    {0}".format(x3))
      
    #return redirect('/')
    return render_template('index.html', x1=x1, x2=x2, x3=x3)
  else:
    return render_template('index.html', )
  
  
'''  
#Table_1
def table_1():
  x1 = str(round(random.uniform(0.74, 0.81), 2))
  if x1 == "0.8":
    x1 = "0.80"
  print("'0,775±0,070'       {0}   {0}".format(x1))
  
  x2 = str(round(random.uniform(2.6, 3.2), 1))
  print("'2,5, не менее'     {0}    {0}".format(x2))

  x3 = str(round(random.uniform(3.2, 3.9), 1))
  print("'2,7, не менее'     {0}    {0}".format(x3))

  x4 = str(round(random.uniform(0.25, 0.39), 2))
  print("'0,1, не менее'        {0}".format(x4))

  x5 = str(round(random.uniform(0.51, 0.62), 2))
  print("'0,25, не менее'    {0}   {0}".format(x5))

  x6 = str(round(random.uniform(0.50, 0.75), 2))
  print("'0,35, не менее'       {0}".format(x6))

  x7 = str(round(random.uniform(10.5, 12.4), 1))
  print("'плюс (10,0±2,5)'   {0}   {0}".format(x7))

  x8 = str(round(random.uniform(-0.3, -0.6), 1))
  print("'минус (0,6±0,5)'  {0}   {0}".format(x8))

  x9 = str(round(random.uniform(float(x7), float(x7) + 0.4), 1))
  print("'плюс (10,0±2,5)'      {0}".format(x9))

  x10 = str(round(random.uniform(0.3, 0.6), 1))
  print("'минус (0,6±0,5)'      {0}".format(x10))

  x11 = str(round(random.uniform(20.1, 22.5), 1))
  print("'плюс (20,0±5)'     {0}  {0}".format(x11))

  x12 = "-" + x11 
  print("'плюс (20,0±5)'    {0} {0}".format(x12))
'''  

  
  
  
