# CNN finding the number of circles
![CNN finder logo](https://raw.githubusercontent.com/vadimfedulov321/CNN-finding-the-number-of-circles-v2/master/logo/index.png)
## Convolutional Neural Network counts circles in 4 different numbers of any color

You should have:

python2.7 or higher (`sudo apt install python2.7 python-pip`)

Jupyter Notebook (`python -m pip install --upgrade pip`, `python -m pip install jupyter`)

NumPy (`pip install numpy`)

Keras v2 with TensorFlow backend (`pip install tensorflow-gpu`, `pip install keras`)

CUDA 9.0 and cuDNN 7.0.5 (for TensorFlow backend)



You can use pretrained CNN-model in folder 'models' by circle_finder_CNN_v2.ipynb or train your own by train_circle_finder_CNN_v2.ipynb

You can also use your own trained model, it will be in folder 'models' after training, dont forget to delete pretrained one.

And you can use circle_finder_CNN_v2.py by command `python circle_finder_CNN_v2.py`, it will work the same way as circle_finder_CNN_v2.ipynb,
but without vizualisation and in terminal.

And you can denote some last lines of code in circle_finder_CNN_v2.ipynb and circle_finder_CNN_v2.py to rename all files using predictions

You can download your own randomly generated training and validation datasets by command `python get_data.py`, test dataset by command `python get_test.py` Notebooks and circle_finder_CNN.py will find generated paths, so dont change
them, if you dont really need it.

circle_finder_CNN.ipynb and circle_finder_CNN_v2.py use the same path "test/test/*.png"

train_circle_finder_CNN_v2.ipynb use pathes "data/train/../*png", "data/val/../*png"

Special thanks to web-site https://dummyimage.com I have downloaded my own dataset there with scripts generating random numbers with random colors. If you dont want to lose time by generating your
own, you can download dataset that I used during training of pretrained model here, https://drive.google.com/file/d/1q7_2xQxbyP-f8h9rYhIXAyRAU2muGyKf/view?usp=sharing
