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

    def addData(self, path, dataName, splitSymbol):
        fich = open(path, "r")
        fich_str = list(fich)
        fich.close()
        x = []
        y = []
        for i in fich_str:
            elem_str = i.replace("\n", "")
            elem = elem_str.split(splitSymbol)
            x.append(float(elem[0]))
            y.append(float(elem[1]))
        self.dataDict[dataName] = {"xValues": x, "yValues": y}

    def deleteData(self, dataName):
    	self.dataDict.pop(dataName)

    def getData(self, dataName):
        data = self.dataDict.get(dataName)
        return data
