import bob
import scipy.signal as sp
import math as m
np = bob.ip.numpy
pi = float('%.4f' %  m.pi)
pi2 = float('%.4f' % float(pi/2))
def crop(height, width, image, errors, name,size):
    #crops image to 215x215 from center of image
    imgN=len(image)
    #print(imgN)
    imgM=len(image[0])
    #print(imgM)
    img = sp.wiener(image,[3, 3])
    Gy, Gx = np.gradient(img)
    orientnum = sp.wiener(2*Gx*Gy,[3,3])
    orientden = sp.wiener((Gx**2) - (Gy**2),[3,3])
    W2 = max([len(image), len(image[0])])
    W = 8
    ll = 9
    orient = np.zeros((imgN/W+1,imgM/W+1))
    snum = []
    sden = []
#calculates orientation
    for i in range(1,(imgN/W+1)*(imgM/W+1)+1):
        #print('X and Y are')
        x = m.floor((i-1)/(imgM/W))*W
        #print(x)
        y = ((i-1)%(imgN/W))*W
        #print(y)
        numblock = orientnum[y:y+W,x:x+W]
        
        denblock = orientden[y:y+W,x:x+W]

        somma_num=sum(sum(numblock))
        snum.append(somma_num)
        somma_denom=sum(sum(denblock))
        sden.append(somma_denom)
        if somma_denom != 0:
            inside = somma_num/somma_denom
            angle = 0.5*m.atan(inside)
        else:
            angle = pi2

        if angle < 0:
            if somma_num < 0:
                angle = angle + pi2
            else:
                angle = angle + pi
        else:
            if somma_num > 0:
                angle = angle + pi2
        orient[(y)/W+1][(x)/W+1] = angle
    for si in range(0,imgM/W+1):
        orient[0][si] = pi
    for si in range(0,imgN/W+1):
        orient[si][0] = pi 
      
    #np.savetxt('/remote/filer.gx/home.active/dyambay/Bob/FingerprintRec/snum.txt',snum)
    #np.savetxt('/remote/filer.gx/home.active/dyambay/Bob/FingerprintRec/sden.txt',sden)
    #np.savetxt('/remote/filer.gx/home.active/dyambay/Bob/FingerprintRec/orient.txt',orient)
    templist = np.zeros((imgN/W+1,imgM/W+1))
    for i, j in enumerate(orient):
        for k,l in enumerate(j):
            if l < pi2:
                templist[i][k] = 1 
    #np.savetxt('/remote/filer.gx/home.active/dyambay/Bob/FingerprintRec/templist.txt',templist)
#first round of binarization
    
    by, bx = np.where(templist==1)
    #print('********Information********')

    rows = np.zeros((imgN/W+1,imgM/W+1)) #xdir
    cols = np.zeros((imgN/W+1,imgM/W+1)) #ydir
    for k in range(0,len(by)):

        ik = bx[k]
        jk = by[k]
        if orient[jk][ik] < pi2 :
            x = int(float(ll*m.cos(orient[jk][ik]-pi2)/(W/2)))
            y = int(float(ll*m.sin(orient[jk][ik]-pi2)/(W/2)))
            #print('***************Information********************')
            #print(rows.shape)
            #print(jk)
            #print(ik)
            rows[jk][ik] = ik-x
            cols[jk][ik] = jk-y 
    #np.savetxt('/remote/filer.gx/home.active/dyambay/Bob/FingerprintRec/rows.txt',rows)
    #np.savetxt('/remote/filer.gx/home.active/dyambay/Bob/FingerprintRec/cols.txt',cols)           
#binarization of image
    binarize = np.zeros((imgN/W+1,imgM/W+1))
    for k in range(0,len(by)):
        #print(bx[k])
        #print(by[k])
        xk = bx[k]
        yk = by[k]
        col_num = cols[yk][xk]
        row_num = rows[yk][xk]
        if cols[yk][xk]>=94:
           col_num = 93
        if rows[yk][xk]>=101:   
           row_num = 100  

        if not (int(rows[yk][xk]) < (1) or int(cols[yk][xk]) < (1) or int(rows[yk][xk]) > (imgM/W) or int(cols[yk][xk]) > (imgN/W)):
            #import pdb; pdb.set_trace()
            while templist[col_num][row_num]>0:

                xtemp = row_num
                ytemp = col_num
                if int(xtemp) < 1 or int(ytemp)<1 or int(xtemp) > imgM/W or int(ytemp) == imgN/W:
                    break
                xk = xtemp
                yk = ytemp
                if float(rows[yk][xk]) < 1. or float(cols[yk][xk]) < 1. or float(rows[yk][xk]) > imgM/W or float(cols[yk][xk]) > imgN/W:
                    if xk - 1 > 0:
                        while templist[yk][xk-1]>0:
                            xk=xk-1
                            if xk-1<1:
                                break
                    break
                col_num = cols[yk][xk]
                row_num = rows[yk][xk]
                if cols[yk][xk]>=94:
                   col_num = 93
                if rows[yk][xk]>=101: 
                   row_num = 100
 
        binarize[yk][xk] = binarize[yk][xk]+1
    #np.savetxt('/remote/filer.gx/home.active/dyambay/Bob/FingerprintRec/binarize.txt',binarize)

    
    j,i = np.unravel_index(binarize.argmax(), binarize.shape)
    #print(i)
    #print(j)
    #counter = 0
    while j>(imgM/W)*.85 or i>(imgN/W)*.85 or j<(imgM/W)*.15 or i<(imgN/W)*.15:
        binarize[j][i] = 0
        j,i = np.unravel_index(binarize.argmax(), binarize.shape)   
        #print(i)
        #print(j)
    angle = orient[j][i] - (pi2)
    #print(angle)
    Xcenter = int(round(i*W-(W/2)-(ll/2)*m.cos(angle)))
    Ycenter = int(round(j*W-(W/2)-(ll/2)*m.sin(angle)))
    #print(Xcenter)
    #print(Ycenter)
    
    
    #######################################
    #######################################
    #Crops image based on Xcenter and YCenter
    N = size
    M = len(image)

    imgN = len(image)
    imgM = len(image[0])

    if (Ycenter-m.floor(N/2)<1)|(Ycenter+m.floor(N/2)>imgN)|(Xcenter-m.floor(N/2)<1)|(Xcenter+m.floor(N/2)>imgM):
        message='Cropping error: when the input image is cropped an error occurs: a possible error during center point determination.'
        print(message)
        errors.append(name)   
        CroppedPrint=np.zeros((N,N))
    else:
        CroppedPrint=image[Ycenter-m.floor(N/2):Ycenter+m.floor(N/2)+1,Xcenter-m.floor(N/2):Xcenter+m.floor(N/2)+1];
    return CroppedPrint, errors
