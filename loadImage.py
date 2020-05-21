########################################################################
########################################################################


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from utils import *
import os


########################################################################
########################################################################
# Training
    # Apple 492 0-320 0-320
    # Banana 450 0-199 0-200 0-198
    # Grape 490 0-327 0-327
    # Orange 479 0-309 0-320
# Test
    # Apple 164 0-327 0-327
    # Banana 152 0-162 0-165 0-200
    # Grape 166 0-300 0-269
    # Orange 160 0-100 0-327
########################################################################
########################################################################
    

paths='base_image/'
objets=['Apple','Banana','Grape','Orange']
rotationStarts=[327,199,327,309]
endRs=[327,200,327,327]
endR2s=[0,200,0,0]

########################################################################
########################################################################

def loadObject(paths,rotationStart,endR,obj,base,endR2):

    filename=paths+base+'/'+obj+'/'
    moon=[]
    
    for i in range(rotationStart): # load les objets sans rotation
        if os.path.isfile(filename+str(i)+'_100.jpg'):
            moon.append(mpimg.imread(filename+str(i)+'_100.jpg'))
               
    for j in range(endR+1):
        if os.path.isfile(filename+'r_'+str(j)+'_100.jpg'):
            moon.append(mpimg.imread(filename+'r_'+str(j)+'_100.jpg'))
    
    if obj=='Banana':
    
        for k in range(endR2+1):
            if os.path.isfile(filename+'r2_'+str(k)+'_100.jpg'):
                moon.append(mpimg.imread(filename+'r2_'+str(k)+'_100.jpg'))
                        
    return moon

########################################################################
########################################################################

    
def load(paths,objets,rotationStarts,endRs,endR2s):
    imagesLearn={}
    imagesTest={}
    i=0
    for j in objets:
       imagesLearn[j] = loadObject(paths,rotationStarts[i]+1,endRs[i],j,'training',endR2s[i])
       imagesTest[j] = loadObject(paths,rotationStarts[i]+1,endRs[i],j,'test',endR2s[i])
       i=i+1;
      
    return imagesLearn,imagesTest

########################################################################
########################################################################


########################################################################
########################################################################

###Image pour aprentissage 
###appleLearn=imagesLearn['Apple']
##bananaLearn=imagesLearn['Banana']
##grapeLearn=imagesLearn['Grape']
##orangeLearn=imagesLearn['Orange']
###Image pour test
##appleTest=imagesTest['Apple']
##BananaTest=imagesTest['Banana']
##grapeTest=imagesTest['Grape']
##orangeTest=imagesTest['Orange']
###Test affichage

##plt.imshow(appleLearn[1])
##plt.show()
########################################################################
########################################################################
########################################################################


