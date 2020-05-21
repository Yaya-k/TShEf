#####################################################################
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import copy
from skimage.color import rgb2gray
from skimage.measure import label, regionprops, regionprops_table
import skimage.feature
import math
from sklearn.metrics import plot_confusion_matrix
from sklearn.neighbors import NearestCentroid
from sklearn.neighbors import NeighborhoodComponentsAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tempfile import TemporaryFile
import os
#####################################################################
objets=['Apple','Banana','Grape','Orange']
#1 Apple
#2 Banana
#3 Grape
#4 Orange

pas = 64 # pas de quantification
thresh = 0.98# seuil 

#####################################################################
#	quantification retoune une image quantifiée sur 'pas' couelurs	#
#####################################################################
# Pour une seule image
def quantification(image): 
	mask = rgb2gray(image) < thresh
	maskedImg = np.zeros_like(image)
	for i in range(3):
		maskedImg[:,:,i] = image[:,:,i] * mask
    
	return np.uint8(np.floor(maskedImg/float(pas))*pas)

# Pour toutes les images
def quantificationLearnTest(imagesLearn,imagesTest): 
	imagesLearnQuantifier={}
	imagesTestQuantifier={}

    #ici le code de quantifiaction
	for objet in imagesLearn.keys():
		if objet not in imagesLearnQuantifier:
			imagesLearnQuantifier[objet] = []
		for img in imagesLearn[objet]:
			mask = rgb2gray(img) < thresh
			maskedImg = np.zeros_like(img)
			for i in range(3):
				maskedImg[:,:,i] = img[:,:,i] * mask
			imagesLearnQuantifier[objet].append(np.uint8(np.floor(
			maskedImg/float(pas))*pas))
			
	for objet in imagesTest.keys():
		if objet not in imagesTestQuantifier:
			imagesTestQuantifier[objet] = []
		for img in imagesTest[objet]:
			mask = rgb2gray(img) < thresh
			maskedImg = np.zeros_like(img)
			for i in range(3):
				maskedImg[:,:,i] = img[:,:,i] * mask
			imagesTestQuantifier[objet].append(np.uint8(np.floor(
			maskedImg/float(pas))*pas))
    
	return imagesLearnQuantifier,imagesTestQuantifier

#####################################################################
#	couelurPrincipal retoune la liste de la couleur dominante de	#
# 	chaque image sous forme de triplet (tuple)						#
#####################################################################
# Pour une seule image
def couleurPrincipale(image):
	dictHist = {}
	(m,n,p) = image.shape
	for i in range(m):
		for j in range(n):
			couleur = tuple(image[i,j,:])
			if couleur == (0,0,0):
				continue
			if couleur not in dictHist:
				dictHist[couleur] = 0
			else:
				dictHist[couleur] += 1
	return max(dictHist, key = dictHist.get)

# Pour toutes les images
def couleurPrincipaleLearnTest(imagesLearnQuantifier,
imagesTestQuantifier):
	CpImagesLearnQuantifier={}
	CpImagesTestQuantifier={}

    #ici le code pour extraire la couleur principal
	for objet in imagesLearnQuantifier.keys():
		if objet not in CpImagesLearnQuantifier:
			CpImagesLearnQuantifier[objet] = []
		for img in imagesLearnQuantifier[objet]:
			dictLearn = {}
			(m,n,p) = img.shape
			for i in range(m):
				for j in range(n):
					couleur = tuple(img[i,j,:])
					if couleur == (0,0,0):
						continue
					if couleur not in dictLearn:
						dictLearn[couleur] = 0
					else:
						dictLearn[couleur] += 1
			CpImagesLearnQuantifier[objet].append(max(dictLearn, key = 
			dictLearn.get))
	
	for objet in imagesTestQuantifier.keys():
		if objet not in CpImagesTestQuantifier:
			CpImagesTestQuantifier[objet] = []
		for img in imagesTestQuantifier[objet]:
			dictTest = {}
			(m,n,p) = img.shape
			for i in range(m):
				for j in range(n):
					couleur = tuple(img[i,j,:])
					if couleur == (0,0,0):
						continue
					if couleur not in dictTest:
						dictTest[couleur] = 0
					else:
						dictTest[couleur] += 1
			CpImagesTestQuantifier[objet].append(max(dictTest, key = 
			dictTest.get))

	return CpImagesLearnQuantifier,CpImagesTestQuantifier

#####################################################################
#	LBP retoune la moyenne et la variance de l'image LBP de l'image	# 
#	en entrée														#
#####################################################################
# Pour une seule image
def LBP(image,radius,n_points):
	lbp = skimage.feature.local_binary_pattern(rgb2gray(
	image),n_points,radius,'uniform')
	return lbp.mean(),lbp.std()

# Pour un dico d'image
def LBPs(images,radius,n_points):
	lbpStatstics = {}

	for objet in images.keys():
		if objet not in lbpStatstics:
			lbpStatstics[objet] = []
		imagesLearn = copy.copy(images[objet])
		#lbp = skimage.feature.local_binary_pattern(rgb2gray(
		#imagesLearn[0]),n_points,radius,'uniform')
		#n_bins = int(lbp.max() + 1)
		#h1, _ = np.histogram(lbp, bins=n_bins)
		#h = np.zeros((len(imagesLearn),n_points+2),dtype=np.int64)
		#h[0] = h1
		for i in range(len(imagesLearn)):
			lbp = skimage.feature.local_binary_pattern(rgb2gray(
			imagesLearn[i]),n_points,radius,'uniform')
			#n_bins = int(lbp.max() + 1)
			# print(n_bins)
			#h1, _ = np.histogram(lbp, bins=n_bins)
			#h[i]=h1
			#h = np.asarray(h)
			lbpStatstics[objet].append(lbp.mean(),lbp.std())
        
	return lbpStatstics
    
# Pour toutes les images
def LBPLearnTest(imagesLearnQuantifier,imagesTestQuantifier,radius,n_points):
	return  LBPs(imagesLearnQuantifier,radius,n_points), 
	LBPs(imagesTestQuantifier,radius,n_points)
#####################################################################
# extracteForm calcule le rapport longueur/hauteur des objets 
# de l'image
#####################################################################
def extractForm(image):
	mask = rgb2gray(image) < thresh
	label_img = label(mask)
	
	m,n = label_img.shape
	d = float(max(m,n))

	regions = regionprops(label_img)

	distanceX =[];
	distanceY =[];
	
	for props in regions:
		y0, x0 = props.centroid
		orientation = props.orientation
		x1 = x0 + math.cos(orientation) * 0.5 * props.minor_axis_length
		y1 = y0 - math.sin(orientation) * 0.5 * props.minor_axis_length
		x2 = x0 - math.sin(orientation) * 0.5 * props.major_axis_length
		y2 = y0 - math.cos(orientation) * 0.5 * props.major_axis_length
		distanceX.append(abs(x1-x2))
		distanceY.append(abs(y1-y2))
		
	rapport = np.amax(distanceX)/np.amax(distanceY)
	if rapport <= d:
		return np.amax(distanceX)/np.amax(distanceY)/d
	else:
		return 1
	# pour un dico d'images        
def extractForms(images):
	formsDico={}
	
	for objet in images.keys():
		if objet not in formsDico:
			formsDico[objet] = []
		imgs = copy.copy(images[clas])
		tt = []
		for img in imgs:
			tt.append(form(img))
		formsDico[clas] = tt
		
	return formsDico

# pour toutes les images                        
def formsLearnTest(imagesLearn,imagesTest):  
	return  forms(imagesLearn), forms(imagesTest)

#####################################################################
# extractFeatures calcule tous les descripteur pour
# une image donnée 
#####################################################################
def extractFeatures(image):
    #ici nous allons faire appelle à tous les fonction (LBP...)
	image1 = quantification(image)
	(r,g,b) = couleurPrincipale(image1)
	(meanLBP,stdLBP) = LBP(image,1,8)
	rapportLl = extractForm(image)

	return [r,g,b,meanLBP,stdLBP,rapportLl]

def extractFeaturesLearnTest(imagesLearnQuantifier,imagesTestQuantifier):
    #ici nous allons faire appelle à tous les fonction (LBP...)
	imagesLearnX = []
	imagesLearnY = []
	imagesTestX = []
	imagesTestY = []
	
	m1 = float(len(imagesLearnQuantifier.keys()))
	m2 = float(len(imagesTestQuantifier.keys()))
	
	i = 1
	for objet in imagesLearnQuantifier.keys():
		s1 = len(imagesLearnQuantifier[objet])
		j = 1
		for img in imagesLearnQuantifier[objet]:
			print("{:.1f}".format(((i-1)/(m1+m2) + (j-1)/(m1+m2)/s1)*100)+"%")
			imagesLearnX.append(extractFeatures(img))
			imagesLearnY.append(i)
			j = j + 1
		i = i + 1
	
	i = 1
	for objet in imagesTestQuantifier.keys():
		s1 = len(imagesTestQuantifier[objet])
		j = 1
		for img in imagesTestQuantifier[objet]:
			print("{:.1f}".format(((i-1+m1)/(m1+m2) + (j-1)/(m1+m2)/s1)*100)+"%")
			imagesTestX.append(extractFeatures(img))
			imagesTestY.append(i)
			j = j + 1
		i = i + 1
	
	imagesLearnX = np.array(imagesLearnX) 
	imagesLearnY = np.array(imagesLearnY)
	imagesTestX = np.array(imagesTestX)
	imagesTestY = np.array(imagesTestY)
	
	if len(imagesLearnQuantifier) != 0:
		np.savez('data.npz', imagesLearnX = imagesLearnX, imagesLearnY = imagesLearnY, imagesTestX = imagesTestX, imagesTestY = imagesTestY)
		
	return imagesLearnX,imagesLearnY,imagesTestX,imagesTestY
#####################################################################
# Ici nous avons la fonction des kppv
# la fonction prend en entré:
#          - X_train: une liste contenant des liste de 6 descripteurs (pour les données d'entrainement)
#          - y_train: une liste contenant la classe associer a chaque liste de descripteurs(pour les données d'entrainement)
#           -----------------------------------------------------------------------------------------------------
#          - X_test: une liste contenant des liste de 6 descripteurs (pour les données test)
#          - y_test: une liste contenant la classe associer a chaque liste de descripteurs(pour les données test)
#           ----------------------------------------------------------------------------------------------------
#          - k: le nombre de voisin a prendre en compte
# En sortie:
#        -  Une matrice de confusion
#
# NB: les classe sont
#       1=> Apple
#       2=> Banana
#       3=> Grape
#       4=> Orange

######################################################################
def KPPV(X_train,y_train,X_test,y_test,k):
    knn = KNeighborsClassifier(n_neighbors=k)
    classifier = knn.fit(X_train, y_train)
    score = knn.score(X_test, y_test)
    titles_options = [("Confusion matrix, without normalization", None),
                  ("Normalized confusion matrix", 'true')]
    class_names=['Apple' ,'Banana' ,'Grape' ,'Orange']

    for title, normalize in titles_options:
        disp = plot_confusion_matrix(classifier, X_test, y_test,
                                 display_labels=class_names,
                                 cmap=plt.cm.Blues,
                                 normalize=normalize)
        disp.ax_.set_title(title)

        print(title)
        print(disp.confusion_matrix)

    plt.show()
    return score
#######################################################################################

def KPPVNCA(X_train,y_train,X_test,y_test,k):
    
    nca = NeighborhoodComponentsAnalysis()
    nca.fit(X_train, y_train)
    knn = KNeighborsClassifier(n_neighbors=k)

    knn.fit(nca.transform(X_train), y_train)

   
    score=knn.score(nca.transform(X_test), y_test)
    
    return score
####################################################################################################
# Une fonction qui predit la classe d'une image
# la fonction prend en entré:
#          - X_train: une liste contenant des liste de 6 descripteurs (pour les données d'entrainement)
#          - y_train: une liste contenant la classe associer a chaque liste de descripteurs(pour les données d'entrainement)
#           -----------------------------------------------------------------------------------------------------
#          - imageMetrques: Une liste contenant les 6 descripteurs d'une image a predire
#          
#           ----------------------------------------------------------------------------------------------------
#          - k: le nombre de voisin a prendre en compte
# En sortie:
#        -  la classe de l'image
#
# NB: les classe sont
#       1=> Apple
#       2=> Banana
#       3=> Grape
#       4=> Orange

####################################################################################################
def predict(X_train,y_train,imageMetrques,k=4):
    knn = KNeighborsClassifier(n_neighbors=k)
    classifier = knn.fit(X_train, y_train)
    
    return classifier.predict(imageMetrques)
    
#####################################################################
