# CNN finding the number of circles
![CNN finder logo](https://raw.githubusercontent.com/vadimfedulov321/CNN-finding-the-number-of-circles/master/logo/index.png)
## Convolutional Neural Network counts circles in 4 different numbers of any color

You should have:

python2.7 or higher (`sudo apt install python2.7 python-pip`)

Jupyter Notebook (`python -m pip install --upgrade pip`, `python -m pip install jupyter`)

NumPy (`pip install numpy`)

h5py (`pip install h5py`)

Keras v2 with TensorFlow backend (`pip install tensorflow-gpu`, `pip install keras`)

CUDA 9.0 and cuDNN 7.0.5 (for TensorFlow backend)

Augmentor, if you want to generate your own dataset to reproduce the experiment (`pip install augmentor`)



You can use pretrained CNN-model in folder 'models' by circle_finder_CNN.ipynb or train your own by train_circle_finder_CNN.ipynb

You can also use your own trained model, it will be in folder 'models' after training, dont forget to delete pretrained one.

And you can use circle_finder_CNN.py by command `python circle_finder_CNN.py`, it will work the same way as circle_finder_CNN.ipynb,
but without vizualisation and in terminal.

You can download your own randomly generated training dataset by command `python gen_train.py`, validation dataset
by command `python gen_val.py` and test dataset by command `python gen_test.py` Notebooks and circle_finder_CNN.py will find generated paths, so dont change
them, if you dont really need it.

circle_finder_CNN.ipynb and circle_finder_CNN.py use the same path "test/test/*.png"

train_circle_finder_CNN.ipynb use pathes "data/train/../*png", "data/val/../*png"

Special thanks to web-site https://dummyimage.com I have downloaded my own dataset there with scripts generating random numbers with random colors. If you dont want to lose time by generating your
own, you can download my dataset here, it had been augmented already https://mega.nz/#!OfZkgabI!fND1wYutt2lA7gdSr4xgsNNmXPZwrGPaqvKhPZf7uxk
