
def matcher(fingerfile, fp_database,size, savefolder, ImageLoader, cropping, sectornorm, gabor2d, match):

    import ImageLoader as IL
    import cropping as cr
    import bob
    import os
    import sectornorm as sn
    import gabor2d as gb2
    import math
    import match as mat
    sp = bob.sp
    np = bob.ip.numpy

    #loads data and saves the fingerprint feature information into a database
    errors = []
    fp_number = len(fp_database)
    f = open(fingerfile, 'r')
    data_files = f.readlines()
    data_names = data_files
    #for imagecount2 in range(0,1):
    for imagecount2 in range(0,len(data_files)):
        toLoad = data_files[imagecount2][0:len(data_files[imagecount2])-1]
        print('Loading Image '+ toLoad)
        print('Image number ' + str(imagecount2+1) + ' of ' +str(len(data_files)))
	    #loads selected image into an array and resizes it to be divisible by 8
        loadedImage,height,width= IL.loadImage(toLoad)
        
        #Crops image around center point
        #print('Cropping image ' + toLoad)
        CroppedPrint, errors = cr.crop(height,width, loadedImage, errors, toLoad,size)
        
        #normalizes and sectorizes print
        #print('Sectorizing image ' + toLoad)
        NormalizedPrint, vector = sn.sector_norms(CroppedPrint,0,1,size)
        
        #performs gabor analysis and prepares data to be matched. Fingercode are the features and df is the name of the fingerprint in the database
        fingercode, df = gb2.gabor2d(NormalizedPrint,fp_database,size,imagecount2,data_names,data_files,1)
        
        #matches image against other images.
        best_match = mat.matcher(savefolder,fp_number,data_files, fp_database, df, fingercode,imagecount2)
                        
    print('complete')
   



