'''
Information and howto read from pythonlibary.org
Website URL Used: http://www.blog.pythonlibrary.org/2017/10/11/convert-a-photo-to-black-and-white-in-python/
'''

from PIL import Image

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

if __name__ == '__main__':  
    black_and_white('TestImages/caterpillar.jpg','TestOutput/bw_caterpillar.jpg')
    black_and_white_dithering('TestImages/caterpillar.jpg', 'TestOutput/bw_caterpillar_dithering.jpg')

    black_and_white('TestImages/MH.png', 'TestOutput/MH_BK.png')
    black_and_white_dithering('TestImages/MH.png', 'TestOutput/MH_BK_dithering.png')

    print('done')
