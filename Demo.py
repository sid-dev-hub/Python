import os
import shutil

path = "/home/sid/Downloads"
files = os.listdir(path)

for file in files:
    filenma,extension = os.path.splitext(file)
    
    if os.path.exists(path) 