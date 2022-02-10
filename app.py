from flask import Flask, render_template, request, redirect, url_for
import random


app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
  tab_1 = [0 for i in range(100)]
  f_tune = ["1,6", "4,5", "8,1", "14,1", "25,1", "31,1", "32,1", 
          "33,1", "34,1", "36,1", "37,1", "39,1", "41,1", "43,1", 
          "44,1", "46,1", "48,1", "50,1", "52,1", "54,1", "57,1",
          "59,1", "61,1", "64,1", "67,1", "69,1", "72,1", "75,1", "79,1",
           "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", 
           "  ", "  ", "  "]
  f_tune1 = f_tune[:21]
  f_tune2 = f_tune[21:]
  vol1 = ["0" for i in range(21)]
  vol2 = ["0" for i in range(8)] + [" " for i in range(13)]
  tab_3 = [0 for i in range(100)]
  tab_4_1 = [0 for i in range(100)]
        
  if request.method == "POST":
    #Table 1
    tab_1 = table_1()
    #Table 2.1
    f_tune, vol = table_2_1()
    f_tune1 = f_tune[:21]
    f_rune2 = f_tune[21:]
    vol1 = vol[:21]
    vol2 = vol[21:]
    #Table 3
    tab_3 = table_3()
    #Table 4.1
    
    
    return render_template('index.html', tab_1=tab_1, f_tune1=f_tune1, f_tune2=f_tune2, 
                           vol1=vol1, vol2=vol2, tab_3=tab_3, tab_4_1=tab_4_1)
  
  else:
    return render_template('index.html', tab_1=tab_1, f_tune1=f_tune1, f_tune2=f_tune2, 
                           vol1=vol1, vol2=vol2, tab_3=tab_3, tab_4_1=tab_4_1)
  
  
#Table 1
def table_1():
  tab_1 = ["0"]
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
  x10 = str(round(random.uniform(-0.3, -0.6), 1))
  tab_1.append(x10)
  #print("'минус (0,6±0,5)'      {0}".format(x10))
  x11 = str(round(random.uniform(20.1, 22.5), 1))
  tab_1.append(x11)
  #print("'плюс (20,0±5)'     {0}  {0}".format(x11))
  x12 = "-" + x11
  tab_1.append(x12)
  #print("'плюс (20,0±5)'    {0} {0}".format(x12))
  
  return tab_1


#Table 2.1
def table_2_1():
  f_tune = ["1,6", "4,5", "8,1", "14,1", "25,1", "31,1", "32,1", 
          "33,1", "34,1", "36,1", "37,1", "39,1", "41,1", "43,1", 
          "44,1", "46,1", "48,1", "50,1", "52,1", "54,1", "57,1",
          "59,1", "61,1", "64,1", "67,1", "69,1", "72,1", "75,1", "79,1",
           "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", "  ", 
           "  ", "  ", "  "]
  
  vol = []
  x = round(random.uniform(1.4, 1.6), 1)
  for i in range(29):
    a = round(random.uniform(x-0.2, x+0.3), 1)
    if a > 2.1:
      a = 2.1
    vol.append(a)
    x = a
  
  temp = vol[0]
  count = 1
  for i in range(1, len(vol)):
    if vol[i] == temp:
      count += 1
      if count > 2:
        vol[i] += round(random.uniform(-0.3, +0.0), 1)
    else:
      count = 1
      temp = vol[i]
      
  vol = list(map(lambda x: round(x, 1), vol))
  
  vol[2] = max(vol)
  vol[5] = max(vol)
  vol = vol + [" " for i in range(13)]
  
  return f_tune, vol


#Table 3
def table_3():
  tab_3 = ["0"]
  x1 = str(round(random.uniform(0.4, 0.8), 1))
  tab_3.append(x1)
  #print("   1,2      {}".format(x1))
  x2 = str(round(random.uniform(1.0, 1.6), 1))
  tab_3.append(x2)
  #print("   2,4      {}".format(x2))
  x3 = str(round(float(x2) + random.uniform(0.3, 0.7), 1))
  tab_3.append(x3)
  #print("   3,3      {}".format(x3))
  x4 = str(round(random.uniform(7.5, 8.9), 1))
  tab_3.append(x4)
  #print(" 18(m=30%)  {}".format(x4))
  x5 = str(round(random.uniform(2.0, 2.8), 1))
  tab_3.append(x5)
  #print("8,5(m=90%)  {}".format(x5))
  x6 = str(round(random.uniform(2.0, 2.8), 1))
  tab_3.append(x6)
  #print("8,5(m=90%)  {}".format(x6))
  x7 = str(round(random.uniform(4.5, 5.5), 1))
  tab_3.append(x7)
  #print("   6,0      {}".format(x7))
  #print("- - - - - - - -")
  x8 = str(round(random.uniform(0.4, 0.6), 1))
  tab_3.append(x8)
  #print("   1,0      {}".format(x8))
  x9 = str(round(random.uniform(1.2, 1.6), 1))
  tab_3.append(x9)
  #print("   2,0      {}".format(x9))
  x10 = str(round(random.uniform(1.9, 2.2), 1))
  tab_3.append(x10)
  #print("   2,7      {}".format(x10))
  x11 = str(round(random.uniform(13.2, 14.2), 1))
  tab_3.append(x11)
  #print("14,5(m=30%) {}".format(x11))
  x12 = str(round(random.uniform(2.5, 3.6), 1))
  tab_3.append(x12)
  #print(" 6,8(m=90%) {}".format(x12))
  x13 = str(round(random.uniform(2.5, 3.6), 1))
  tab_3.append(x13)
  #print(" 6,8(m=90%) {}".format(x13))
  x14 = str(round(random.uniform(1.6, 2.8), 1))
  tab_3.append(x14)
  #print("   4,8      {}".format(x14))
  
  return tab_3


#Table 4.1
def table_1():
  tab_1 = ["0"]
  
  
  
  

  
  
  
