import os
import numpy as np
import random

os.makedirs('./test/test/')

file = open('test_links.py','w') 
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
      file.write('", "test/test/')
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
      file.write('print "test images downloaded:", i\n')

file.close()

import test_links

os.remove('test_links.py')
os.remove('test_links.pyc')
