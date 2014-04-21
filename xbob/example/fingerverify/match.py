import bob
np = bob.ip.numpy

#Calculates Euclidian Distance between the features of loaded print against each print in the database
def matcher(savefolder,fp_number,data_files, fp_database, df, fingercode,imagecount2):
    value_d1 = np.zeros((8,1))
    best_matching = np.zeros((fp_number,1))
    for scanning in range(0,fp_number):
    #for scanning in range(0,1):
        fp = data_files[scanning][0:len(data_files[imagecount2])-1]
        fcode = fp_database[fp]
        d1 = 0
        for disco in range(0,8):
            f1 = fcode[disco]
            d1 = d1 + np.linalg.norm(fingercode[disco]-f1,2)
        best_matching[scanning][0] = d1
    best_match = np.min(best_matching)    
    saveloc = savefolder + df[len(df)-17:len(df)-4] +'.txt'
    f = open(saveloc, 'w') 
    f.write("\n".join(map(lambda x: str(x), best_matching)))
    f.close()
    
    return best_match
