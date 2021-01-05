import hashlib
import numpy as np
import os
import tkinter as tk
from tkinter import filedialog


os.chdir(filedialog.askdirectory())
os.getcwd()

file_list = os.listdir()
print(len(file_list))

duplicates = []
hash_keys = dict()
for index, filename in  enumerate(os.listdir('.')):  
    if os.path.isfile(filename):
        with open(filename, 'rb') as f:
            filehash = hashlib.md5(f.read()).hexdigest()
        if filehash not in hash_keys: 
            hash_keys[filehash] = index
        else:
            duplicates.append((index,hash_keys[filehash]))

print(duplicates)

for index in duplicates:
    os.remove(file_list[index[0]])

