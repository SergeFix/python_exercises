# script for mass renaming music files according to labels
# sample input format:  <album> - <track> <title> (<year>).mp3
# Sample output format: Bob Dylan/<year> <album>/<track> <title>.mp3

import os
import re
import shutil

path = r'D:\temp\files'
ListFiles = os.listdir(path)
LenList = len(ListFiles)
t_data = []
os.chdir(path)

# parsing file name for data required for folder creation
for i in range (0, LenList):
    pat = r'(.*) - (\d+) (.*) \((\d+)\)\.mp3'
    t_data = re.search(pat, ListFiles[i]).groups()

# creation of new folder
newPath = path + '\\' + t_data[0] + '\\' + t_data[3] + " " + t_data[0]
os.makedirs(newPath)

# moving files to new destination
for i in range (0, LenList):
    shutil.move(ListFiles[i], newPath)

# files renaming
os.chdir(newPath)
for i in range (0, LenList):
    pat = r'(.*) - (\d+) (.*) \((\d+)\)\.mp3'
    t_data = re.search(pat, ListFiles[i]).groups()
    final_name = t_data[1] + ' ' + t_data[2] + '.mp3'
    os.rename(ListFiles[i], final_name)








