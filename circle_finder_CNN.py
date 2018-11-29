import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model

circle_finder_model = load_model('models/circle_finder_CNN.h5')

# dimensions of our images
img_width, img_height = 56, 28
# you can use any quantity of pictures in your dataset, but dont forget that total number of them should be possible to devide by batch_size
test_data_dir = 'test'
# set batch size whatever you want now, but its better to set it equal to total number of pictures in your dataset or just close to it
batch_size=150
# set the number of steps equal to number of batches dataset can be devided (ex. if dataset is 100 picture then batch_size can be 25 and steps can be 4)
steps=1

test_generator = ImageDataGenerator().flow_from_directory(
        test_data_dir,
        target_size=(img_width, img_height),
        color_mode='rgb',
        batch_size=batch_size)

predictions = circle_finder_model.predict_generator(test_generator, steps=steps)
bsteps=batch_size*steps
num=0
for j in xrange(bsteps):
    arr=predictions
    a=arr[num,0]
    b=arr[num,1]
    c=arr[num,2]
    d=arr[num,3]
    e=arr[num,4]
    f=arr[num,5]
    g=arr[num,6]
    h=arr[num,7]
    i=arr[num,8]
    if a>b and a>c and a>d and a>e and a>f and a>g and a>h and a>i:
        prediction=[0]
    if b>a and b>c and b>d and b>e and b>f and b>g and b>h and b>i:
        prediction=[1]
    if c>a and c>b and c>d and c>e and c>f and c>g and c>h and c>i:
        prediction=[2]
    if d>a and d>b and d>c and d>e and d>f and d>g and d>h and d>i:
        prediction=[3]
    if e>a and e>b and e>c and e>d and e>f and e>g and e>h and e>i:
        prediction=[4]
    if f>a and f>b and f>c and f>d and f>e and f>g and f>h and f>i:
        prediction=[5]
    if g>a and g>b and g>c and g>d and g>e and g>f and g>h and g>i:
        prediction=[6]
    if h>a and h>b and h>c and h>d and h>e and h>f and h>g and h>i:
        prediction=[7]
    if i>a and i>b and i>c and i>d and i>e and i>f and i>g and i>h:
        prediction=[8]
    print prediction
    num+=1
