

def templatecreator(fingerfile, savefile,size, ImageLoader, cropping, sectornorm, gabor2d):
    import ImageLoader as IL
    import cropping as cr
    import bob
    import os
    import sectornorm as sn
    import gabor2d as gb2
    import pickle
    sp = bob.sp
    np = bob.ip.numpy

    #loads data and saves the fingerprint feature information into a database
    subtract = 0
    errors = []
    fp_database = {}
    f = open(fingerfile, 'r')
    data_files = f.readlines()
    data_names = data_files
    for imagecount in range(0,len(data_names)-subtract):
    #for imagecount in range(0,1):
        toLoad = data_files[imagecount][0:len(data_files[imagecount])-1]
        print('Loading Image '+ toLoad)
        print('Image number ' + str(imagecount+1) + ' of ' +str(len(data_names)-subtract))
	    #loads selected image into an array and resizes it to be divisible by 8
        loadedImage,height,width= IL.loadImage(toLoad)
        
        #Crops image around center point
        CroppedPrint, errors = cr.crop(height,width, loadedImage, errors, toLoad, size)      
        #normalizes and sectorizes print
        #print('Sectorizing image ' + toLoad)
        NormalizedPrint, vector = sn.sector_norms(CroppedPrint,0,0, size)
        
        #performs gabor analysis and prepares data to be entered into database
        fp_database, df = gb2.gabor2d(NormalizedPrint,fp_database,size,imagecount,data_names,data_files,0)
      #  print('Added to Database fingerprint ' + df)
    pickle.dump(fp_database, open(savefile,'wb'))
    
    return data_files, fp_database          
    
