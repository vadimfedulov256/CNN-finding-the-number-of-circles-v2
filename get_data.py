import os
import random

# number of training images to download for each category,  but +1 for the last
ntrain_imgs = 11111
# number of validation images to download for each category,  but +1 for the last
nval_imgs = 11

os.makedirs('./data/train/0/')
file = open('train_links0.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 0...')

while x < ntrain_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 0 and not str(color) in open('train_links0.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('train_links0.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/train/0/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "training images to directory 0 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading training data to directory 0 were generated successfully')
print('Start downloading training data to directory 0...')

import train_links0

os.remove('train_links0.py')
os.remove('train_links0.pyc')

os.makedirs('./data/train/1/')
file = open('train_links1.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 1...')

while x < ntrain_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 1 and not str(color) in open('train_links1.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('train_links1.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/train/1/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "training images to directory 1 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading training data to directory 1 were generated successfully')
print('Start downloading training data to directory 1...')

import train_links1

os.remove('train_links1.py')
os.remove('train_links1.pyc')

os.makedirs('./data/train/2/')
file = open('train_links2.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 2...')

while x < ntrain_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 2 and not str(color) in open('train_links2.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('train_links2.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/train/2/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "training images to directory 2 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading training data to directory 2 were generated successfully')
print('Start downloading training data to directory 2...')

import train_links2

os.remove('train_links2.py')
os.remove('train_links2.pyc')

os.makedirs('./data/train/3/')
file = open('train_links3.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 3...')

while x < ntrain_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 3 and not str(color) in open('train_links3.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('train_links3.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/train/3/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "training images to directory 3 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading training data to directory 3 were generated successfully')
print('Start downloading training data to directory 3...')

import train_links3

os.remove('train_links3.py')
os.remove('train_links3.pyc')

os.makedirs('./data/train/4/')
file = open('train_links4.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 4...')

while x < ntrain_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 4 and not str(color) in open('train_links4.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('train_links4.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/train/4/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "training images to directory 4 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading training data to directory 4 were generated successfully')
print('Start downloading training data to directory 4...')

import train_links4

os.remove('train_links4.py')
os.remove('train_links4.pyc')

os.makedirs('./data/train/5/')
file = open('train_links5.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 5...')

while x < ntrain_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 5 and not str(color) in open('train_links5.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('train_links5.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/train/5/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "training images to directory 5 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading training data to directory 5 were generated successfully')
print('Start downloading training data to directory 5...')

import train_links5

os.remove('train_links5.py')
os.remove('train_links5.pyc')

os.makedirs('./data/train/6/')
file = open('train_links6.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 6...')

while x < ntrain_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 6 and not str(color) in open('train_links6.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('train_links6.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/train/6/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "training images to directory 6 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading training data to directory 6 were generated successfully')
print('Start downloading training data to directory 6...')

import train_links6

os.remove('train_links6.py')
os.remove('train_links6.pyc')

os.makedirs('./data/train/7/')
file = open('train_links7.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 7...')

while x < ntrain_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 7 and not str(color) in open('train_links7.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('train_links7.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/train/7/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "training images to directory 7 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading training data to directory 7 were generated successfully')
print('Start downloading training data to directory 7...')

import train_links7

os.remove('train_links7.py')
os.remove('train_links7.pyc')

os.makedirs('./data/train/8/')
file = open('train_links8.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating numbers for directory 8...')

while x < ntrain_imgs+1:
    try:
        a = 8
        b = 8
        c = 8
        d = 8
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if not str(color) in open('train_links8.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('train_links8.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/train/8/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "training images to directory 8 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading training data to directory 8 were generated successfully')
print('Start downloading training data to directory 8...')

import train_links8

os.remove('train_links8.py')
os.remove('train_links8.pyc')

os.makedirs('./data/val/0/')
file = open('val_links0.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 0...')

while x < nval_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 0 and not str(color) in open('val_links0.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('val_links0.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/val/0/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "validation images to directory 0 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading validation data to directory 0 were generated successfully')
print('Start downloading validation data to directory 0...')

import val_links0

os.remove('val_links0.py')
os.remove('val_links0.pyc')

os.makedirs('./data/val/1/')
file = open('val_links1.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 1...')

while x < nval_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 1 and not str(color) in open('val_links1.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('val_links1.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/val/1/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "validation images to directory 1 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading validation data to directory 1 were generated successfully')
print('Start downloading validation data to directory 1...')

import val_links1

os.remove('val_links1.py')
os.remove('val_links1.pyc')

os.makedirs('./data/val/2/')
file = open('val_links2.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 2...')

while x < nval_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 2 and not str(color) in open('val_links2.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('val_links2.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/val/2/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "validation images to directory 2 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading validation data to directory 2 were generated successfully')
print('Start downloading validation data to directory 2...')

import val_links2

os.remove('val_links2.py')
os.remove('val_links2.pyc')

os.makedirs('./data/val/3/')
file = open('val_links3.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 3...')

while x < nval_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 3 and not str(color) in open('val_links3.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('val_links3.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/val/3/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "validation images to directory 3 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading validation data to directory 3 were generated successfully')
print('Start downloading validation data to directory 3...')

import val_links3

os.remove('val_links3.py')
os.remove('val_links3.pyc')

os.makedirs('./data/val/4/')
file = open('val_links4.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 4...')

while x < nval_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 4 and not str(color) in open('val_links4.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('val_links4.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/val/4/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "validation images to directory 4 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading validation data to directory 4 were generated successfully')
print('Start downloading validation data to directory 4...')

import val_links4

os.remove('val_links4.py')
os.remove('val_links4.pyc')

os.makedirs('./data/val/5/')
file = open('val_links5.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 5...')

while x < nval_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 5 and not str(color) in open('val_links5.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('val_links5.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/val/5/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "validation images to directory 5 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading validation data to directory 5 were generated successfully')
print('Start downloading validation data to directory 5...')

import val_links5

os.remove('val_links5.py')
os.remove('val_links5.pyc')

os.makedirs('./data/val/6/')
file = open('val_links6.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 6...')

while x < nval_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 6 and not str(color) in open('val_links6.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('val_links6.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/val/6/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "validation images to directory 6 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading validation data to directory 6 were generated successfully')
print('Start downloading validation data to directory 6...')

import val_links6

os.remove('val_links6.py')
os.remove('val_links6.pyc')

os.makedirs('./data/val/7/')
file = open('val_links7.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating random numbers for directory 7...')

while x < nval_imgs:
    try:
        a = random.randint(0, 9)
        b = random.randint(0, 9)
        c = random.randint(0, 9)
        d = random.randint(0, 9)
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if a == 0:
            a1 = 1
        elif a == 1:
            a1 = 0
        elif a == 2:
            a1 = 0
        elif a == 3:
            a1 = 0
        elif a == 4:
            a1 = 0
        elif a == 5:
            a1 = 0
        elif a == 6:
            a1 = 1
        elif a == 7:
            a1 = 0
        elif a == 8:
            a1 = 2
        elif a == 9:
            a1 = 1
        if b == 0:
            b1 = 1
        elif b == 1:
            b1 = 0
        elif b == 2:
            b1 = 0
        elif b == 3:
            b1 = 0
        elif b == 4:
            b1 = 0
        elif b == 5:
            b1 = 0
        elif b == 6:
            b1 = 1
        elif b == 7:
            b1 = 0
        elif b == 8:
            b1 = 2
        elif b == 9:
            b1 = 1
        if c == 0:
            c1 = 1
        elif c == 1:
            c1 = 0
        elif c == 2:
            c1 = 0
        elif c == 3:
            c1 = 0
        elif c == 4:
            c1 = 0
        elif c == 5:
            c1 = 0
        elif c == 6:
            c1 = 1
        elif c == 7:
            c1 = 0
        elif c == 8:
            c1 = 2
        elif c == 9:
            c1 = 1
        if d == 0:
            d1 = 1
        elif d == 1:
            d1 = 0
        elif d == 2:
            d1 = 0
        elif d == 3:
            d1 = 0
        elif d == 4:
            d1 = 0
        elif d == 5:
            d1 = 0
        elif d == 6:
            d1 = 1
        elif d == 7:
            d1 = 0
        elif d == 8:
            d1 = 2
        elif d == 9:
            d1 = 1
        if a1 + b1 + c1 + d1 == 7 and not str(color) in open('val_links7.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('val_links7.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/val/7/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "validation images to directory 7 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading validation data to directory 7 were generated successfully')
print('Start downloading validation data to directory 7...')

import val_links7

os.remove('val_links7.py')
os.remove('val_links7.pyc')

os.makedirs('./data/val/8/')
file = open('val_links8.py', 'w')
file.write('import urllib\n')
file.write('i = 0\n')
file.close()
x = 0

print('Start generating numbers for directory 8...')

while x < nval_imgs+1:
    try:
        a = 8
        b = 8
        c = 8
        d = 8
        f1 = random.randint(0, 9)
        f2 = random.randint(0, 9)
        f3 = random.randint(0, 9)
        f4 = random.randint(0, 9)
        f5 = random.randint(0, 9)
        f6 = random.randint(0, 9)
        number = str(a)+str(b)+str(c)+str(d)
        color = str(f1)+str(f2)+str(f3)+str(f4)+str(f5)+str(f6)
        if not str(color) in open('val_links8.py').read():
            print 'number',  number,  'of color',  color,  'was generated and accepted to be downloaded'
            file = open('val_links8.py', 'a')
            file.write('urllib.urlretrieve("https://dummyimage.com/600x300/000/')
            file.write(str(color))
            file.write('.png&text = ')
            file.write(str(number))
            file.write('",  "data/val/8/')
            file.write(str(number))
            file.write('_')
            file.write(str(color))
            file.write('.png")')
            file.write('\n')
            file.write('i += 1\n')
            file.write('print "validation images to directory 8 downloaded:",  i\n')
            file.close()
            x += 1
    except:
        print 'An error occured!'

print('Links for downloading validation data to directory 8 were generated successfully')
print('Start downloading validation data to directory 8...')

import val_links8

os.remove('val_links8.py')
os.remove('val_links8.pyc')

print 'Dataset was successfully downloaded'
