import os
import sys


PROJECT_PATH = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..', '..'))

DATA_PATH = os.path.join(PROJECT_PATH, 'data')
RAW_DATA_PATH = os.path.join(DATA_PATH, 'raw_data')
TEST_DATA_PATH = os.path.join(DATA_PATH, 'test_data')
os.makedirs(TEST_DATA_PATH, exist_ok=True)
TRAIN_DATA_PATH =  os.path.join(DATA_PATH, 'train_data')
os.makedirs(TRAIN_DATA_PATH, exist_ok=True)

NOTEBOOKS_PATH =  os.path.join(PROJECT_PATH, 'notebooks')
os.makedirs(TRAIN_DATA_PATH, exist_ok=True)
MODELS_PATH =  os.path.join(NOTEBOOKS_PATH, 'models')
os.makedirs(MODELS_PATH, exist_ok=True)
LOGS_PATH =  os.path.join(NOTEBOOKS_PATH, 'logs')
os.makedirs(LOGS_PATH, exist_ok=True)
