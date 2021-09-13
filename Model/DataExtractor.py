import pandas as pd
import numpy as np
import copy
import csv
import os
import re

class DataExtractor:
    def __init__(self):
        self.dataDict = {}

    def resetDataDict(self):
        self.dataDict = {}

    def addData(self, path, dataName, splitSymbol, deleteFirstRow=0, xValuesPos=0, yValuesPos=1):
        fich = open(path, "r")
        fich_str = list(fich)[deleteFirstRow:]
        fich.close()
        x = []
        y = []
        for i in fich_str:
            elem_str = i.replace("\n", "")
            elem = elem_str.split(splitSymbol)
            x.append(float(elem[xValuesPos]))
            y.append(float(elem[yValuesPos]))
        self.dataDict[dataName] = {"xValues": x, "yValues": y}

    def deleteData(self, dataName):
    	self.dataDict.pop(dataName)

    def getData(self, dataName):
        data = self.dataDict.get(dataName)
        return data
