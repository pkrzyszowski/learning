import os

for dirname,dirnames,filenames in os.walk('/home/pk/GITHUB'):
    #printpathtoallsubdirectoriesfirst.
    for subdirname in dirnames:
        print(os.path.join(dirname,subdirname))