########################################################################
# Fichier permettant de l'ancer ou non l'aprentissage:
# Cette decision et basée sur la presence ou non du fichier data
########################################################################
from utils import*
from loadImage import*

paths='base_image/'
objets=['Apple','Banana','Grape','Orange']
rotationStarts=[327,199,327,309]
endRs=[327,200,327,327]
endR2s=[0,200,0,0]

(imagesLearn,imagesTest) = load(paths,objets,rotationStarts,endRs,
endR2s)

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
	print('Loading failed. Creating new data...')
	X_train,Y_train,X_test,Y_test = extractFeaturesLearnTest(
	imagesLearn,imagesTest)
	print('Data created.')

print('Classifying...')    
scrpKPPV = KPPV(X_train,Y_train,X_test,Y_test,4)
os.system('cls')
print('Done.')   
titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]
