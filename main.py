import ImageManipulation as IM
from subprocess import call
import os

if len(os.listdir('TurnFilesB&W')) != 0:
    IM.setFiles()

def makeScript(name):
    String1 = 'scale([.1, .1, 0.1])\n\tsurface(file = \"'
    String2 = '\", center = true, invert = true);'
    nameFile = 'OpenSCadScripts/' + str(name) + '.scad'
    file = open(nameFile, 'w')
    file.write(String1)
    file.write('FilesIn/' + str(name) + '.png')
    file.write(String2)
    file.close()

# getting the number of files in directory
path, dirs, files = next(os.walk("OpenSCadScripts/FilesIn/"))
file_count = len(files)

# making all the scripts
for i in range(file_count):
    makeScript(i)

for i in range(file_count):
    stlName = str(i) + '.stl'
    call(['openscad', '-o', stlName, 'OpenSCadScripts/0.scad'])