from ntpath import join
import os

TOKEN = 'Enter You Token'
BASE_PATH = os.getcwd()
UPLOADS_DIR = 'uploads'


def uploads_list():
    list_dir = os.listdir(UPLOADS_DIR)
    list = []
    for item in list_dir:
        result = os.path.join(BASE_PATH, UPLOADS_DIR, item)
        list.append(result)
    return list
