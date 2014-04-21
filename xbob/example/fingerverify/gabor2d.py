import bob
import math as ma
import findsector as fs 
import sectornorm as sn 
np = bob.ip.numpy
pi = float('%.4f' %  ma.pi)
pi2 = float('%.4f' % float(pi/2))

#creates gabor filters and convolutes with normalized print and uses sectornorm to create the features for matching. Saves features in a database
def gabor2d(NormalizedPrint,fp_database,size,imagecount,data_names,data_files, mode):

    num_disk = 8
    #preforms gabor analysis of image
    gwt = bob.ip.GaborWaveletTransform(number_of_scales=1, sigma = pi, k_max= pi/num_disk)
    gabor = gwt.perform_gwt(NormalizedPrint)
    #generates fingercode based on each of the filters
    for angle in range(0,num_disk):         
        ComponentPrint=np.real(gabor[angle]);
        disk, vector = sn.sector_norms(ComponentPrint,1,0, size)
        #only sectors 0-48 matter. Sector 49 and 50 are not used for matching.
        if angle == 0:
            fingercode = vector[0:1,0:49]
            fingercode = [fingercode]
            df = data_names[imagecount][0:len(data_files[imagecount])-1] 
                
        else:
            fingercode.append(vector[0:1,0:49])           
        
    if mode == 0:
        #Add fingercode to database            
        fp_database[df] = fingercode          
        return fp_database, df
    elif mode == 1:
        return fingercode, df
