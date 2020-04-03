#######################################################################################################################
#######################################################################################################################


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import NearestCentroid

from sklearn.neighbors import NeighborhoodComponentsAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split


#from loadImage import*
#######################################################################################################################

#(imagesLearn,imagesTest)=load()#chargement des images

#######################################################################################################################


def quantification(imagesLearn,imagesTest):
    imagesLearnQuantifier={}
    imagesTestQuantifier={}

    #ici le code de quantifiaction
    
    return imagesLearnQuantifier,imagesTestQuantifier
#######################################################################################################################


def couleurPrincipal(imagesLearnQuantifier,imagesTestQuantifier):
    CpImagesLearnQuantifier={}
    CpImagesTestQuantifier={}

    #ici le code pour extraire la couleur principal

    return CpImagesLearnQuantifier,CpImagesTestQuantifier
#######################################################################################################################

def LBP (imagesLearnQuantifier,imagesTestQuantifier):
    LbpImagesLearnQuantifier={}
    LbpImagesTestQuantifier={}

    #ici le code pour LBP

    return LbpImagesLearnQuantifier,LbpImagesTestQuantifier
#######################################################################################################################

def extractionForm(imagesLearnQuantifier,imagesTestQuantifier):
    rapportImagesLearnQuantifier={}
    rapportImagesTestQuantifier={}

    #extraction longeur et largueur pui faire le rapport

    return rapportImagesLearnQuantifier,rapportImagesTestQuantifier

#######################################################################################################################

def extract_features(imagesLearnQuantifier,imagesTestQuantifier):
    #ici nous allons faire appelle à tous les fonction (LBP...)

    return
#######################################################################################################################

#1 Aplle
#2 Banana
#3 Grape
#4 Orange

def KPPV(X_train,y_train,X_test,y_test,k):

    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    score=knn.score(X_test, y_test)
    
    return score

def KPPVNCA(X_train,y_train,X_test,y_test,k):
    
    nca = NeighborhoodComponentsAnalysis()
    nca.fit(X_train, y_train)
    knn = KNeighborsClassifier(n_neighbors=k)

    knn.fit(nca.transform(X_train), y_train)

   
    score=knn.score(nca.transform(X_test), y_test)
    
    return score



#######################################################################################################################








