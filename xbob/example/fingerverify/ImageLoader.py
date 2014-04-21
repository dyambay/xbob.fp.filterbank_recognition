import bob
from PIL import Image
np = bob.ip.numpy
#loads image into an array and converts from 3d image to 2D grayscale image
def loadImage(imageLocation):
#loads image in from specified location
    img = Image.open(imageLocation)
    image = np.asarray(img,dtype='float64')
#converts image from 3d RGB image to a 2D grayscale image for future processing
    #image = bob.ip.rgb_to_gray(img)
    np.savetxt('/remote/filer.gx/home.active/dyambay/Bob/FingerprintRec/RGBImage.txt',image)
#for processing steps the image needs to have both height and width
#divisible by 8 This function checks the size of the image and zeros pads the right and bottom of the image to make the image size divisible by 8
	#intial height and width of image. If image is right size, these values get returned
    height=len(image)
    width=len(image[0])
#checks height of image
    if (height%8)!=0:
#calculates how many pixels the image is off in height and creates a block of zeros with the missing pixels
        addheight = height%8
        #hb = np.zeros((8-addheight, width))
#since in python white is 255, changes the zero block to 255 elements
        #h_block = [x+255 for x in hb] 
#adds the block to the bottom of the original matrix
        #image = np.concatenate((image,h_block),axis=0)
        image = image[addheight:len(image),0:len(image[0])]
#saves new height of the image
        height = len(image)
#checks width of the image
    if (width%8)!=0:
#calculates how many pixels the image is off in width and creates a block of zeros with the missing pixels
        addwidth = width%8
        #wb = np.zeros((height,8-addwidth))
#since in python white is 255, changes the zero block to 255 elements
        #w_block = [x+255 for x in wb] 
#adds the block to the right of the original matrix
        #image = np.concatenate((image,w_block),axis=1)
        image = image[0:len(image),addwidth:len(image[0])]
#saves new width of image
        width = len(image[0])
#returns values for future functions

    #graylevmax=(2**8)-1
    #image = image/graylevmax
    return image,height,width


