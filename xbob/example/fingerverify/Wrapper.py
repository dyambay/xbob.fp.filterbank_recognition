#import csv
import templates
import matching
#import pickle

#Wrapper function to run the fingerprint recognition algorithm for filterbank recognition. #fingerfile is the input text file of image names
#savefile is the location of the saved pickle file for the fingerprint templates (allows you to skip template building in future runs using commented out code on bottom)
#size is the image size that will cropped out of the original fingerprint image. Min is 184. Default is suggested size
#savefolder is the output folder where result text files will be saved
#Imageloader is the python program used for loading the image. Default ImageLoader loads the image and makes sure the dimensions are divisible by 8
#cropping locates the centerpoint of the fingerprint and returns a cropped image of size, sizexsize around the centerpoint
#sectornorm is used for creating the normalized image as well as the eventual feature disks
#gabor2d creates gabor filters and convolutes with normalized print and uses sectornorm to create the features for matching. Saves features in a database
#match is used for comparing two images and saving results

def Wrapper(fingerfile,savefile,size = 215,savefolder,ImageLoader = 'ImageLoader',cropping = 'cropping',sectornorm = 'sectornorm',gabor2d = 'gabor2d',match = 'match)
    fingerfile = '/remote/filer.gx/home.active/dyambay/Bob/FingerprintRec/CrossmatchTrain_Live.txt'
    savefile = "/remote/filer.gx/home.active/dyambay/Bob/FingerprintRec/Fp_database3.p"
    #size = 215
    savefolder = '/remote/filer.gx/home.active/dyambay/Bob/FingerprintRec/Results3'

    '''ImageLoader = 'ImageLoader' 
    cropping = 'cropping'
    sectornorm = 'sectornorm'
    gabor2d = 'gabor2d'
    match = 'match''''


    data_files, fp_database = templates.templatecreator(fingerfile,savefile, size, ImageLoader, cropping, sectornorm, gabor2d)
    
        #fp_database = pickle.load(open(savefile, 'rb'))
        
    matching.matcher(fingerfile, fp_database, size, savefolder, ImageLoader, cropping, sectornorm, gabor2d, match)
