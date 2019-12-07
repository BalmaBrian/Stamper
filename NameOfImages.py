from os import listdir
from os.path import isfile, join

def getNames():
    mypath = 'TestImages'
    file = open('names.txt','w')

    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

    while onlyfiles:
        file.write(onlyfiles.pop())
        file.write('\n')

    file.close()