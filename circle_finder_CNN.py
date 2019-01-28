import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import load_model

circle_finder_v2_model = load_model('models/circle_finder_CNN_v2.h5')

# dimensions of our images
img_width, img_height = 600, 300
# you can use any quantity of pictures in your dataset, but dont forget that
# total number of them should be possible to devide by batch size
test_data_dir = 'test'
# set batch size whatever you want, but its better to set it as big as you can
# for faster predictions
batch_size = 25
# set the number of steps equal to number of batches dataset can be devided
steps = 2

test_generator = ImageDataGenerator().flow_from_directory(
        test_data_dir,
        target_size=(img_width, img_height),
        color_mode='rgb',
        batch_size=batch_size,
        shuffle=False)

predictions = circle_finder_v2_model.predict_generator(test_generator, steps=steps)
bsteps = batch_size * steps
for i in xrange(bsteps):
    x = predictions[i, :]
    if np.argmax(x, axis=0) == 0:
        prediction = 0
    if np.argmax(x, axis=0) == 1:
        prediction = 1
    if np.argmax(x, axis=0) == 2:
        prediction = 2
    if np.argmax(x, axis=0) == 3:
        prediction = 3
    if np.argmax(x, axis=0) == 4:
        prediction = 4
    if np.argmax(x, axis=0) == 5:
        prediction = 5
    if np.argmax(x, axis=0) == 6:
        prediction = 6
    if np.argmax(x, axis=0) == 7:
        prediction = 7
    if np.argmax(x, axis=0) == 8:
        prediction = 8
    introduction = 'Neural network prediction: '
    final_prediction = introduction+str(prediction)
    print final_prediction
    # original_name = os.path.join('test/test/', str(num+1).zfill(4)+'.png')
    # prediction_name = os.path.join('test/test/', str(num+1).zfill(4)+'_'+str(prediction)+'.png')
    # os.rename(original_name, prediction_name)  # denote these lines to write predictions in the names
