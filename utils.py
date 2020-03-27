#######################################################################################################################
#######################################################################################################################


import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from loadImage import*
#######################################################################################################################

(imagesLearn,imagesTest)=load()#chargement des images

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

def KPPV(metriquesImageLearn,metriquesImageTest):
    #implementer le kppv avec scikit learn et faire un plot de la matrice de confusion

    return matriceConfusion

#######################################################################################################################








