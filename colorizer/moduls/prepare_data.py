import os
import numpy as np
from PIL import Image
from keras.preprocessing.image import img_to_array, load_img
from . import paths
from .constants import SIZE, RGB_24


def resize_img(img_name, size=SIZE, raw_path=paths.RAW_DATA_PATH, final_path=paths.TEST_DATA_PATH):
    image = Image.open(os.path.join(raw_path, img_name))
    resized_image = image.resize(size)
    resized_image.save(os.path.join(final_path, f'resized_{img_name}'))
    pass

def imgs_to_np(pt):
    x = []
    for file in os.listdir(pt):
        x.append(img_to_array(load_img(os.path.join(pt, file))))
    x = np.array(x, dtype=float)
    x /= RGB_24
    return x

