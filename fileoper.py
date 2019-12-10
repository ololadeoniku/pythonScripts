# myFile = open("textfile.csv", "w+")
# #myFile = open("textfile.csv", "a")
# myFile = open("textfile.csv", "r")
# # for i in range(10):
# #     myFile.write(f"This is line # {i} \n")

# # myFile.close()

# if myFile.mode == 'r':
#     #content = myFile.read()
#     #print(content)
#     myLine = myFile.readlines()
#     for x in myLine:
#         print(x, end = "")

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time
import shutil
from shutil import make_archive
from zipfile import ZipFile



print(os.name)
print("Path exists?", str(path.exists("textfile.csv")))
print("Item is a file?", str(path.isfile("textfile.csv")))
print("Item is a directory?", str(path.isdir("textfile.csv")))
print("Item path is:", str(path.realpath("textfile.csv")))
print("Item path and name:", str(path.split(path.realpath("textfile.csv"))))

timemod = time.ctime(path.getmtime("textfile.csv"))
print(timemod)

src = path.realpath("textfile.csv")
dst = src + ".bak"
shutil.copy(src, dst)
shutil.copystat(src, dst)

#os.rename("textfile.csv", "newfile.csv")
with ZipFile("textzip.zip", 'w') as newzip:
    newzip.write("textfile.csv")
    newzip.write("textfile.csv.bak")