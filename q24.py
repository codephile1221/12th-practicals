import os
os.mkdir("myDir")
os.chdir("/home/lukshya/Desktop/python/12th-practicals-main/myDir")
a = open("myFile.txt", "w")
a.write("Here is an example of a text file\n")
a.write("This file was created with python\n")
a.write("We can write on this file\n")
a.close()