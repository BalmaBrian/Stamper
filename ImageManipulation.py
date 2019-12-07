'''
Information and howto read from pythonlibary.org
Website URL Used: http://www.blog.pythonlibrary.org/2017/10/11/convert-a-photo-to-black-and-white-in-python/
'''

from PIL import Image
import NameOfImages

def black_and_white(input_image_path,
    output_image_path):
   color_image = Image.open(input_image_path)
   bw = color_image.convert('L')
   bw.save(output_image_path)

def black_and_white_dithering(input_image_path,
    output_image_path,
    dithering=False):
    color_image = Image.open(input_image_path)
    if dithering:
        bw = color_image.convert('1')  
    else:
        bw = color_image.convert('1',
 
    dither=Image.NONE)
    bw.save(output_image_path)

def setFiles():
    # Gets all the names of the files to be prepared to become a Black & White image
    NameOfImages.getNames()
    file = open('names.txt')
    i = 0
    for each in file:
        path = ''
        path2 = ''
        getPath = 'TurnFilesB&W/' + each
        for letter in getPath:
            if letter != '\n':
                path += letter
        getpath2 = 'FilesIn/' + str(i) + '.png'
        for letter in getpath2:
            if letter != '\n':
                path2 += letter
        i += 1
        black_and_white_dithering(path, path2)
    print('done')