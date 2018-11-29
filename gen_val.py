import os
import numpy as np
import random

os.makedirs('./data/val/0/')
os.makedirs('./data/val/1/')
os.makedirs('./data/val/2/')
os.makedirs('./data/val/3/')
os.makedirs('./data/val/4/')
os.makedirs('./data/val/5/')
os.makedirs('./data/val/6/')
os.makedirs('./data/val/7/')
os.makedirs('./data/val/8/')

file = open('val_links.py','w') 
file.write('import urllib\n')
file.write('i=0\n')

for i in xrange(250):
      a=random.randint(0,9)
      b=random.randint(0,9)
      c=random.randint(0,9)
      d=random.randint(0,9)
      f1=random.randint(0,9)
      f2=random.randint(0,9)
      f3=random.randint(0,9)
      f4=random.randint(0,9)
      f5=random.randint(0,9)
      f6=random.randint(0,9)
      if a==0:
         a1=1
      elif a==1:
         a1=0
      elif a==2:
         a1=0
      elif a==3:
         a1=0
      elif a==4:
         a1=0
      elif a==5:
         a1=0
      elif a==6:
         a1=1
      elif a==7:
         a1=0
      elif a==8:
         a1=2
      elif a==9:
         a1=1
      if b==0:
         b1=1
      elif b==1:
         b1=0
      elif b==2:
         b1=0
      elif b==3:
         b1=0
      elif b==4:
         b1=0
      elif b==5:
         b1=0
      elif b==6:
         b1=1
      elif b==7:
         b1=0
      elif b==8:
         b1=2
      elif b==9:
         b1=1
      if c==0:
         c1=1
      elif c==1:
         c1=0
      elif c==2:
         c1=0
      elif c==3:
         c1=0
      elif c==4:
         c1=0
      elif c==5:
         c1=0
      elif c==6:
         c1=1
      elif c==7:
         c1=0
      elif c==8:
         c1=2
      elif c==9:
         c1=1
      if d==0:
         d1=1
      elif d==1:
         d1=0
      elif d==2:
         d1=0
      elif d==3:
         d1=0
      elif d==4:
         d1=0
      elif d==5:
         d1=0
      elif d==6:
         d1=1
      elif d==7:
         d1=0
      elif d==8:
         d1=2
      elif d==9:
         d1=1
      file.write('urllib.urlretrieve("https://dummyimage.com/56x28/000/')
      file.write(str(f1))
      file.write(str(f2))
      file.write(str(f3))
      file.write(str(f4))
      file.write(str(f5))
      file.write(str(f6))
      file.write('.png&text=')
      file.write(str(a))
      file.write(str(b))
      file.write(str(c))
      file.write(str(d))
      if a1+b1+c1+d1==0:
         file.write('", "data/val/0/')
      elif a1+b1+c1+d1==1:
         file.write('", "data/val/1/')
      elif a1+b1+c1+d1==2:
         file.write('", "data/val/2/')
      elif a1+b1+c1+d1==3:
         file.write('", "data/val/3/')
      elif a1+b1+c1+d1==4:
         file.write('", "data/val/4/')
      elif a1+b1+c1+d1==5:
         file.write('", "data/val/5/')
      elif a1+b1+c1+d1==6:
         file.write('", "data/val/6/')
      elif a1+b1+c1+d1==7:
         file.write('", "data/val/7/')
      elif a1+b1+c1+d1==8:
         file.write('", "data/val/8/')
      file.write(str(a))
      file.write(str(b))
      file.write(str(c))
      file.write(str(d))
      file.write('_')
      file.write(str(f1))
      file.write(str(f2))
      file.write(str(f3))
      file.write(str(f4))
      file.write(str(f5))
      file.write(str(f6))
      file.write('.png")')
      file.write('\n')
      file.write('i+=1\n')
      file.write('print "validation images downloaded:", i\n')

file.close()

import val_links
