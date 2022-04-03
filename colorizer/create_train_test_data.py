import os
import sys
from sklearn.model_selection import train_test_split
from moduls.prepare_data import resize_img
from moduls import paths
from moduls.constants import RANDOM_SEED


if __name__ == '__main__':
    images = [file for file in os.listdir(paths.RAW_DATA_PATH) if file.endswith(('jpeg', 'png', 'jpg'))]
    train_names, test_names = train_test_split(images, test_size=.3, shuffle=True, random_state=RANDOM_SEED)
    for img in train_names: 
        resize_img(img, size=(225, 225), raw_path=paths.RAW_DATA_PATH, final_path=paths.TRAIN_DATA_PATH)
    for img in test_names: 
        resize_img(img, size=(225, 225), raw_path=paths.RAW_DATA_PATH, final_path=paths.TEST_DATA_PATH)


