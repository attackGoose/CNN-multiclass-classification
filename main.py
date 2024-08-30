from Model import TextClassification
from .HelperFunctions.Training import trainModel, testModel
from .HelperFunctions.VisualizationFunctions import createConfusionMatrix
from torchtext import datasets

#find a dataset I want to use from this: https://pytorch.org/text/stable/datasets.html


#for this file, I'll be training the files, testing it, and making a confusion matrix to showcase
#the results of the model
