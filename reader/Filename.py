import os

def list_dir(path):
    FOLDER_PATH = path
    filenames = os.listdir(FOLDER_PATH)
    return filenames
