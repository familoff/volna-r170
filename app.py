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
  tab_4_2 = [0 for i in range(100)]
  tab_5 = [[0, 0] for i in range(10)]
  tab_6 = [[0, 0, 0] for i in range(10)]
  tab_6_1 = [[0, 0] for i in range(30)]
  
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
    tab_4_1 = table_4_1()
    tab_4_2 = table_4_2()
    #Table 5
    tab_5 = table_5()
    #Table 6
    tab_6, tab_6_1 = table_6(tab_1, vol)
    
    return render_template('index.html', tab_1=tab_1, f_tune1=f_tune1, f_tune2=f_tune2, 
                           vol1=vol1, vol2=vol2, tab_3=tab_3, tab_4_1=tab_4_1, tab_4_2=tab_4_2,
                          tab_5=tab_5, tab_6=tab_6, tab_6_1=tab_6_1)
  
  else:
    return render_template('index.html', tab_1=tab_1, f_tune1=f_tune1, f_tune2=f_tune2, 
                           vol1=vol1, vol2=vol2, tab_3=tab_3, tab_4_1=tab_4_1, tab_4_2=tab_4_2,
                          tab_5=tab_5, tab_6=tab_6, tab_6_1=tab_6_1)
  
  
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
  global x9 #Исправление
  x9 = str(round(random.uniform(float(x7), float(x7) + 0.4), 1))
  tab_1.append(x9)
  #print("'плюс (10,0±2,5)'      {0}".format(x9))
  global x10
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
def table_4_1():
  tab_4_1 = ["0"]
  x1 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_1.append(x1)
  #print("1,6 | 0,8     {}".format(x1), "\n")
  x2 = str(round(random.uniform(0.4, 0.9), 1))
  tab_4_1.append(x2)
  #print("              {}".format(x2))
  x3 = str(round(random.uniform(0.6, 0.9), 1))
  tab_4_1.append(x3)
  #print("1,6 | 0,8     {}".format(x3))
  x4 = str(round(random.uniform(0.5, 0.8), 1))
  tab_4_1.append(x4)
  #print("              {}".format(x4), "\n")
  x5 = str(round(random.uniform(0.9, 1.5), 1))
  tab_4_1.append(x5)
  #print("              {}".format(x5))
  x6 = str(round(random.uniform(0.9, 1.5), 1))
  tab_4_1.append(x6)
  #print("2,1 | 1,1     {}".format(x6))
  x7 = str(round(random.uniform(0.9, 1.5), 1))
  tab_4_1.append(x7)
  #print("              {}".format(x7))
  x8 = str(round(random.uniform(0.9, 1.5), 1))
  tab_4_1.append(x8)
  #print("              {}".format(x8), "\n")
  x9 = str(round(random.uniform(0.4, 0.9), 1))
  tab_4_1.append(x9)
  #print("              {}".format(x9))
  x10 = str(round(random.uniform(0.5, 0.9), 1))
  tab_4_1.append(x10)
  #print("              {}".format(x10))
  x11 = str(round(random.uniform(0.5, 0.9), 1))
  tab_4_1.append(x11)
  #print("3,0 | 1,5     {}".format(x11))
  x12 = str(round(random.uniform(0.5, 0.9), 1))
  tab_4_1.append(x12)
  #print("              {}".format(x12))
  x13 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_1.append(x13)
  #print("              {}".format(x13), "\n")
  x14 = str(round(random.uniform(0.3, 0.7), 1))
  tab_4_1.append(x14)
  #print("1,0 | 0,6   {}|{}".format(x14, x14))
  x15 = str(round(random.uniform(0.3, 0.7), 1))
  tab_4_1.append(x15)
  #print("            {}|{}".format(x15, x15), "\n")
  x16 = str(round(random.uniform(0.3, 0.7), 1))
  tab_4_1.append(x16)
  #print("            {}|{}".format(x16, x16))
  x17 = str(round(random.uniform(0.3, 0.7), 1))
  tab_4_1.append(x17)
  #print("1,8 | 0,8   {}|{}".format(x17, x17))
  x18 = str(round(random.uniform(0.3, 0.7), 1))
  tab_4_1.append(x18)
  #print("            {}|{}".format(x18, x18), "\n")
  x19 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_1.append(x19)
  #print("            {}|{}".format(x19, x19))
  x20 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_1.append(x20)
  #print("2,1 | 1,0   {}|{}".format(x20, x20))
  x21 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_1.append(x21)
  #print("            {}|{}".format(x21, x21))
  x22 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_1.append(x22)
  #print("            {}|{}".format(x22, x22), "\n")
  x23 = str(round(random.uniform(0.5, 0.9), 1))
  tab_4_1.append(x23)
  #print("            {}|{}".format(x23, x23))
  x24 = str(round(random.uniform(0.5, 0.9), 1))
  tab_4_1.append(x24)
  #print("            {}|{}".format(x24, x24))
  x25 = str(round(random.uniform(0.5, 0.9), 1))
  tab_4_1.append(x25)
  #print("3,0 | 1,5   {}|{}".format(x25, x25))
  x26 = str(round(random.uniform(0.5, 0.9), 1))
  tab_4_1.append(x26)
  #print("            {}|{}".format(x26, x26))
  x27 = str(round(random.uniform(0.5, 0.9), 1))
  tab_4_1.append(x27)
  #print("            {}|{}".format(x27, x27), "\n")
  x28 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_1.append(x28)
  #print("            {}|{}".format(x28, x28))
  x29 = str(round(random.uniform(0.4, 0.7), 1))
  tab_4_1.append(x29)
  #print("            {}|{}".format(x29, x29))
  x30 = str(round(random.uniform(0.5, 0.8), 1))
  tab_4_1.append(x30)
  #print("3,5 | 2,0   {}|{}".format(x30, x30))
  x31 = str(round(random.uniform(0.6, 0.9), 1))
  tab_4_1.append(x31)
  #print("            {}|{}".format(x31, x31))
  x32 = str(round(random.uniform(0.6, 0.9), 1))
  tab_4_1.append(x32)
  #print("            {}|{}".format(x32, x32))
  x33 = str(round(random.uniform(0.5, 0.8), 1))
  tab_4_1.append(x33)
  #print("            {}|{}".format(x33, x33), "\n")
  x34 = str(round(random.uniform(0.4, 0.7), 1))
  tab_4_1.append(x34)
  #print("1,1 | 0,6     {}".format(x34))
  x35 = str(round(random.uniform(0.7, 0.9), 1))
  tab_4_1.append(x35)
  #print("1,6 | 0,8     {}".format(x35))
  x36 = str(round(random.uniform(0.9, 1.5), 1))
  tab_4_1.append(x36)
  #print("2,1 | 1,1     {}".format(x36), "\n")
  x37 = str(round(random.uniform(1.4, 2.1), 1))
  tab_4_1.append(x37)
  #print("   2,5        {}".format(x37))
  x38 = str(round(random.uniform(1.9, 2.7), 1))
  tab_4_1.append(x38)
  #print("   3,3        {}".format(x38))
  x39 = str(round(random.uniform(2.2, 2.9), 1))
  tab_4_1.append(x39)
  a, b = float(x38), float(x39)
  if b <= a:
      b = a + 0.3
      x39 = str(b)
  tab_4_1.append(x1)    
  #print("   5,0        {}".format(x39))
  
  return tab_4_1


#Table 4.2
def table_4_2():
  tab_4_2 = ["0"]
  x1 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_2.append(x1)
  #print("10      {}".format(x1))
  x2 = str(round(random.uniform(0.2, 0.4), 1))
  tab_4_2.append(x2)
  #print("5       {}".format(x2))
  x3 = str(round(random.uniform(0.3, 0.5), 1))
  tab_4_2.append(x3)
  #print("7       {}".format(x3))
  x4 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_2.append(x4)
  #print("10      {}".format(x4))
  x5 = str(round(random.uniform(0.2, 0.4), 1))
  tab_4_2.append(x5)
  #print("5       {}".format(x5))
  x6 = str(round(random.uniform(0.2, 0.4), 1))
  tab_4_2.append(x6)
  #print("5       {}".format(x6))
  x7 = str(round(random.uniform(0.3, 0.5), 1))
  tab_4_2.append(x7)
  #print("7       {}".format(x7))
  x8 = str(round(random.uniform(0.3, 0.5), 1))
  tab_4_2.append(x8)
  #print("7       {}".format(x8), "\n")
  x9 = str(round(random.uniform(0.2, 0.4), 1))
  tab_4_2.append(x9)
  #print("5     {0}|{0}".format(x9))
  x10 = str(round(random.uniform(0.2, 0.4), 1))
  tab_4_2.append(x10)
  #print("5     {0}|{0}".format(x10), "\n")
  x11 = str(round(random.uniform(0.3, 0.5), 1))
  tab_4_2.append(x11)
  #print("7       {}".format(x11), "\n")
  x12 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_2.append(x12)
  #print("10    {0}|{0}".format(x12))
  x13 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_2.append(x13)
  #print("        {}".format(x13), "\n")
  x140 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_2.append(x140)
  #print("10    {0}|{0}".format(x140))
  x150 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_2.append(x150)
  #print("      {0}|{0}".format(x150), "\n")
  x14 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_2.append(x14)
  #print("      {0}|{0}".format(x14))
  x15 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_2.append(x15)
  #print("10    {0}|{0}".format(x15))
  x16 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_2.append(x16)
  #print("      {0}|{0}".format(x16), "\n")
  x17 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_2.append(x17)
  #print("10    {0}|{0}".format(x17))
  x18 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_2.append(x18)
  #print("      {0}|{0}".format(x18), "\n")
  x19 = str(round(random.uniform(0.6, 1.0), 1))
  tab_4_2.append(x19)
  #print("15    {0}|{0}".format(x19))
  x20 = str(float(x19) + 0.1)
  if float(x19) == 0.7:
      x20 = "0.8"
  tab_4_2.append(x20)    
  #print("      {0}|{0}".format(x20), "\n")
  x21 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_2.append(x21)
  #print("      {0}|{0}".format(x21))
  x22 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_2.append(x22)
  #print("10    {0}|{0}".format(x22))
  x23 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_2.append(x23)
  #print("      {0}|{0}".format(x23))
  x24 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_2.append(x24)
  #print("      {0}|{0}".format(x24), "\n")
  x25 = str(round(random.uniform(0.6, 1.0), 1))
  tab_4_2.append(x25)
  #print("15    {0}|{0}".format(x25), "\n")
  x26 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_2.append(x26)
  #print("      {0}|{0}".format(x26))
  x27 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_2.append(x27)
  #print("10    {0}|{0}".format(x27))
  x28 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_2.append(x28)
  #print("      {0}|{0}".format(x28))
  x29 = str(round(random.uniform(0.4, 0.8), 1))
  tab_4_2.append(x29)
  #print("      {0}|{0}".format(x29), "\n")
  x30 = str(round(random.uniform(0.8, 1.0), 1))
  tab_4_2.append(x30)
  #print("15    {0}|{0}".format(x30))
  x31 = str(float(x30) + 0.2)
  if float(x30) == 0.7:
      x31 = "0.9"
  tab_4_2.append(x31)    
  #print("      {0}|{0}".format(x31), "\n")
  x32 = str(round(random.uniform(1.8, 3.0), 1))
  tab_4_2.append(x32)
  #print("10    {0}|{0}".format(x32))
  x33 = str(round(random.uniform(0.4, 0.6), 1))
  tab_4_2.append(x33)
  #print("        {}".format(x33))
  
  return tab_4_2


#Table 5
def table_5():
  tab_5 = ["0"]
  f_list = set()
  for i in range(random.randint(7, 10)):
      lev = 0
      f = random.randint(10, 79)
      if i == 9:
          f = 79
      if f < 25:
          lev = 7
      elif 25 <= f < 35:
          lev = 7.5
      elif 35 <= f < 45:
          lev = 8
      elif 45 <= f < 55:
          lev = 8.5
      elif 55 <= f < 65:
          lev = 9
      elif 65 <= f < 70:
          lev = 9.5
      else:
          lev = 10

      for i in ["997", "998", "999"]:
         f_list.add("{}   {}".format(str(f)+i, lev))

  tab = sorted(list(f_list))
  tab_5 = list(map(lambda x: x.split(), tab))
    
  return tab_5


#Table 6 #Исправления
def table_6(t1, t2):
  tab_6 = []
  a1 = t1[3]
  a1_1 = float(a1) + 0.1
  # print("    2,7       {0}/{0}      {1}/{1}      {0}/{0}".format(a1, round(a1_1, 1)))
  tab_6.append(["2,7", a1 + " / " + a1, "{0} / {0}".format(round(a1_1, 1))])
  # tab_6.append(["2,7", a1 + " / " + a1, a1_1])
  a2 = t1[7]
  a2_1 = float(a2) + 0.1
  #print("  10±2,5     {0}/{0}    {1}/{1}    {0}/{0}".format(a2, round(a2_1, 1)))
  tab_6.append(["10±2,5", a2 + " / " + a2, "{0} / {0}".format(round(a2_1, 1))])
  a3 = t1[8]
  a3_1 = float(a3) + 0.1
  #print("-0,6±0,5     {0}/{0}    {1}/{1}    {0}/{0}".format(a3, round(a3_1, 1)))
  tab_6.append(["-0,6±0,5", a3 + " / " + a3, "{0} / {0}".format(round(a3_1, 1))])
  a4 = t1[11]
  a4_1 = float(a4) + 0.1
  #print("   20±5      {0}/{0}    {1}/{1}    {0}/{0}".format(a4, round(a4_1, 1)))
  tab_6.append(["20±5", a4 + " / " + a4, "{0} / {0}".format(round(a4_1, 1))])
  a5 = t1[12]
  a5_1 = float(a5) + 0.1
  #print("  -20±5     {0}/{0}  {1}/{1}  {0}/{0}".format(a5, round(a5_1, 1)), "\n")
  tab_6.append(["-20±5", a5 + " / " + a5, "{0} / {0}".format(round(a5_1, 1))])
  
  tab_6.append([" \xa0", " \xa0", " \xa0"])
  
  #print("  10±2,5     {0}         {1}         {0}".format(a2, round(a2_1, 1)))
  tab_6.append(["10±2,5", a2, round(a2_1, 1)])
  #print("  10±2,5     {0}         {1}         {0}".format(a2, round(a2_1, 1)))
  tab_6.append(["10±2,5", a2, round(a2_1, 1)])
  #print("-(0,6±0,5)   {0}         {1}         {0}".format(a3, round(a3_1, 1)))
  tab_6.append(["-(0,6±0,5)", a3, round(a3_1, 1)])
  #print("-(0,6±0,5)   {0}         {1}         {0}".format(a3, round(a3_1, 1)))
  tab_6.append(["-(0,6±0,5)", a3, round(a3_1, 1)])
  #print("  10±2,5     {0}         {1}         {0}".format(a2, round(a2_1, 1)))
  tab_6.append(["10±2,5", a2, round(a2_1, 1)])
  #print("-(0,6±0,5)   {0}         {1}         {0}".format(a3, round(a3_1, 1)))
  tab_6.append(["-(0,6±0,5)", a3, round(a3_1, 1)])
  #print("  10±2,5     {0}         {1}         {0}".format(a2, round(a2_1, 1)))
  tab_6.append(["10±2,5", a2, round(a2_1, 1)])
  #print("-(0,6±0,5)   {0}         {1}         {0}".format(a3, round(a3_1, 1)))
  tab_6.append(["-(0,6±0,5)", a3, round(a3_1, 1)])
  #print("   20±5      {0}         {1}         {0}".format(a4, round(a4_1, 1)))
  tab_6.append(["20±5", a4, round(a4_1, 1)])
  #print("   20±5      {0}         {1}         {0}".format(a4, round(a4_1, 1)))
  tab_6.append(["20±5", a4, round(a4_1, 1)])
  #print(" -(20±5)     {0}         {1}         {0}".format(a4, round(a4_1, 1)))
  tab_6.append(["-20±5", a5, round(a5_1, 1)])
  #print(" -(20±5)     {0}         {1}         {0}".format(a4, round(a4_1, 1)))
  tab_6.append(["-20±5", a5, round(a5_1, 1)])
  #print("   20±5      {0}         {1}         {0}".format(a4, round(a4_1, 1)))
  tab_6.append(["20±5", a4, round(a4_1, 1)])
  #print(" -(20±5)     {0}         {1}         {0}".format(a4, round(a4_1, 1)))
  tab_6.append(["-20±5", a5, round(a5_1, 1)])
  #print("   20±5      {0}         {1}         {0}".format(a4, round(a4_1, 1)))
  tab_6.append(["20±5", a4, round(a4_1, 1)])
  #print(" -(20±5)     {0}         {1}         {0}".format(a4, round(a4_1, 1)))
  tab_6.append(["-20±5", a5, round(a5_1, 1)])
  
  tab_6.append([" \xa0", " \xa0", " \xa0"])
  
  #Исправление
  tab_6.append(["10±2,5", x9, round(float(x9) + 0.1, 1)])
  tab_6.append(["-(0,6±0,5)", x10, round(float(x10) + 0.1, 1)])
  
  volumes_1 = t2[:29]
  temp_v = list(map(lambda x: x+0.1, volumes_1))
  volumes_2 = list(map(lambda x: round(x, 1), temp_v))
  tab_6_1 = []
  
  for i in range(len(volumes_1)):
    tab_6_1.append([volumes_1[i], volumes_2[i]])
    
  return tab_6, tab_6_1
