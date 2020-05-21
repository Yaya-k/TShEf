#############################################################
# Cettte fichier se charge de lancer ou pas l'aprentissage selon la presence ou non
# du fichier data.npz.
# en l'absence de cette fichier il faut obligatoirement qui y est les bases d'images
############################################################

from utils import*
from loadImage import*
#from yyyy import *

paths='base_image/'
objets=['Apple','Banana','Grape','Orange']
rotationStarts=[327,199,327,309]
endRs=[327,200,327,327]
endR2s=[0,200,0,0]

print('Attempting to load data.')
try:
	with np.load('data.npz') as data:
		print('Loading data...')
		X_train = data['imagesLearnX']
		Y_train = data['imagesLearnY']
		X_test = data['imagesTestX']
		Y_test = data['imagesTestY']
		print('Loading existing data done.')
except:
	(imagesLearn,imagesTest) = load(paths,objets,rotationStarts,endRs,endR2s)
	print('Loading failed. Creating new data...')
	X_train,Y_train,X_test,Y_test = extractFeaturesLearnTest(
	imagesLearn,imagesTest)
	print('Data created.')
	
