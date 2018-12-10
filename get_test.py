import os
import numpy as np
import random

ntest_imgs=50
format=4 #quantity of nulls before the actual number

os.makedirs('./test/test/')

file = open('test_links.py','w')
file.close()
file = open('test_links.py','r+')
file.write('import urllib\n')
file.write('i=0\n')

print('Start generating random numbers for test data')

for i in xrange(ntest_imgs):
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
      number=str(a)+str(b)+str(c)+str(d)
      color=str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
      print 'number', number, 'of color', color, 'was generated'
      file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
      file.write(str(color))
      file.write('.png&text=')
      file.write(str(number))
      file.write('", "test/test/')
      file.write(str(i+1).zfill(format))
      file.write('.png")')
      file.write('\n')
      file.write('i+=1\n')
      file.write('print "test images downloaded:", i\n')

file.close()

print('Links for downloading test data were generated successfully')
print('Start downloading test data to directory "test"...')

import test_links

os.remove('test_links.py')
os.remove('test_links.pyc')

print 'Dataset was successfully downloaded'
