from flask import Flask, render_template, request, redirect, url_for
import random


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
  tab_1 = [0 for i in range(100)]
  if request.method == "POST":
    '''
    x1 = str(round(random.uniform(0.74, 0.81), 2))
    if x1 == "0.8":
      x1 = "0.80"
    tab_1.append(x1)  
    #print("'0,775±0,070'       {0}   {0}".format(x1))
    x2 = str(round(random.uniform(2.6, 3.2), 1))
    tab_1.append(x2)
    #print("'2,5, не менее'     {0}    {0}".format(x2))
    x3 = str(round(random.uniform(3.2, 3.9), 1))
    tab_1.append(x3)
    #print("'2,7, не менее'     {0}    {0}".format(x3))
    x4 = str(round(random.uniform(0.25, 0.39), 2))
    tab_1.append(x4)
    #print("'0,1, не менее'        {0}".format(x4))
    x5 = str(round(random.uniform(0.51, 0.62), 2))
    tab_1.append(x5)
    #print("'0,25, не менее'    {0}   {0}".format(x5))
    x6 = str(round(random.uniform(0.50, 0.75), 2))
    tab_1.append(x6)
    #print("'0,35, не менее'       {0}".format(x6))
    '''
    tab_1 = table_1()
    
    #return redirect('/')
    #return render_template('index.html', x1=x1, x2=x2, x3=x3, x4=x4, x5=x5, x6=x6)
    return render_template('index.html', tab_1=tab_1)
  else:
    return render_template('index.html', tab_1=tab_1)
  
  
#Table_1
def table_1():
  tab_1 = []
  tabb_1[0] = 0
  x1 = str(round(random.uniform(0.74, 0.81), 2))
  if x1 == "0.8":
    x1 = "0.80"
  tab_1.append(x1)
  #print("'0,775±0,070'       {0}   {0}".format(x1))
  
  x2 = str(round(random.uniform(2.6, 3.2), 1))
  tab_1.append(x2)
  #print("'2,5, не менее'     {0}    {0}".format(x2))

  x3 = str(round(random.uniform(3.2, 3.9), 1))
  tab_1.append(x3)
  #print("'2,7, не менее'     {0}    {0}".format(x3))

  x4 = str(round(random.uniform(0.25, 0.39), 2))
  tab_1.append(x4)
  #print("'0,1, не менее'        {0}".format(x4))

  x5 = str(round(random.uniform(0.51, 0.62), 2))
  tab_1.append(x5)
  #print("'0,25, не менее'    {0}   {0}".format(x5))

  x6 = str(round(random.uniform(0.50, 0.75), 2))
  tab_1.append(x6)
  #print("'0,35, не менее'       {0}".format(x6))

  x7 = str(round(random.uniform(10.5, 12.4), 1))
  tab_1.append(x7)
  #print("'плюс (10,0±2,5)'   {0}   {0}".format(x7))

  x8 = str(round(random.uniform(-0.3, -0.6), 1))
  tab_1.append(x8)
  #print("'минус (0,6±0,5)'  {0}   {0}".format(x8))

  x9 = str(round(random.uniform(float(x7), float(x7) + 0.4), 1))
  tab_1.append(x9)
  #print("'плюс (10,0±2,5)'      {0}".format(x9))

  x10 = str(round(random.uniform(0.3, 0.6), 1))
  tab_1.append(x10)
  #print("'минус (0,6±0,5)'      {0}".format(x10))

  x11 = str(round(random.uniform(20.1, 22.5), 1))
  tab_1.append(x11)
  #print("'плюс (20,0±5)'     {0}  {0}".format(x11))

  x12 = "-" + x11
  tab_1.append(x12)
  #print("'плюс (20,0±5)'    {0} {0}".format(x12))
  
  return tab_1
  
  

  
  
  
