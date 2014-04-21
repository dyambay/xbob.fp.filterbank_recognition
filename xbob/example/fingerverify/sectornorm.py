import bob
import math as m
import findsector as fs
np = bob.ip.numpy

#computes information about each of the sectors of the cropped image
def sector_norms(image, mode, mix, size):
    #image = np.asarray(((image/255)-1)/255, dtype = 'float') 
    #size of image 215x215    
    N = size
    #number of sectors in image
    M = 50
    #size
    size_im = N*N

    
    #creates 50x1 arrays of zeros to be filled with information from each
    #sector
    mean_s=np.zeros((1,M))
    varn_s=np.zeros((1,M))
    num_s=np.zeros((1,M))
    #initializes zero array for image
    image1=np.zeros((N,N))
    Mo=50
    Vo=50
    #print('*****Information******')
    #calculates initial mean values for each sector
    for i in range(0,size_im):
        #print('Mean locations')
        y = (i%N)
        #print(y)
        x = (i-y)/N
        #print(x)
        tmp = fs.findsector(i,N)
        #print(tmp)
        if (tmp>=0):
            #print(mean_s.shape)
            #print(image.shape)
            mean_s[0][tmp] = mean_s[0][tmp] + image[y][x]
            num_s[0][tmp] = num_s[0][tmp]+1
    #calculates actual mean for each sector
    for i in range(0,M):
        mean_s[0][i] = mean_s[0][i]/num_s[0][i]
    #np.savetxt('/remote/filer.gx/home.active/dyambay/Bob/FingerprintRec/SectorMeans' + str(0) +'.txt',mean_s)
    #calculates initial variance values for each sector
    for i in range(0,size_im):
        y = (i%N)
        x = (i-y)/N
        tmp = fs.findsector(i,N)
        if (tmp>=0):
            varn_s[0][tmp] = varn_s[0][tmp] + (image[y][x]-mean_s[0][tmp])**2
    #calculates actual mean for each sector
    for i in range(1,M):
        varn_s[0][i] = varn_s[0][i]/num_s[0][i] 

    if mix == 0 or mix ==1:
        for i in range(0,size_im):
            y = (i%N)
            x = (i-y)/N
            tmp = fs.findsector(i,N)
            image1[y][x] = varn_s[0][tmp]
            
    if mode == 0:
        for i in range(0,size_im):
            y = i%N
            x = (i-y)/N
            tmp = fs.findsector(i,N)
            if tmp>=0 and abs(varn_s[0][tmp])>1:
                if (image[y][x] - mean_s[0][tmp])<0:
                    if tmp ==48 or tmp ==49 and mix == 0:
                        image1[y][x] = 50
                    else:
                        image1[y][x] = Mo - (Vo/varn_s[0][tmp]*((image[y][x] - mean_s[0][tmp])**2))**.5
                        
                else:
                    if tmp ==49 or tmp ==48 and mix == 0:
                        image1[y][x] = 50
                    else:
                        image1[y][x] = Mo + (Vo/varn_s[0][tmp]*((image[y][x] - mean_s[0][tmp])**2))**.5      
            else:
                image1[y][x] = Mo
                
        disk = image1
        vector = varn_s
    else:
        disk = image1
        vector = varn_s  
        
    return disk, vector  
       
