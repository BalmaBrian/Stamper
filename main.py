import ImageManipulation as IM
from subprocess import call
import os

if len(os.listdir('TurnFilesB&W')) != 0:
    IM.setFiles()

def makeScript(name):
    String1 = 'scale([.1, .1, 0.06])\n\tsurface(file = \"'
    String2 = '\", center = true, invert = false);'
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
    print('processing file ' + str(i + 1) + ' of ' + str(file_count))
    stlName = str(i) + '.stl'
    stlNamePath = 'OpenSCadScripts/' + str(i) + '.scad'
    call(['openscad', '-o', stlName, stlNamePath])
    call(['mv', stlName, 'FilesOut/'])
print('Completed')