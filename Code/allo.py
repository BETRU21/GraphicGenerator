# coding=Latin1
import matplotlib.pyplot as plt
import numpy as np
import os

def addData(path, splitSymbol, deleteFirstRow=0, xValuesPos=0, yValuesPos=1, normaliseX=False, normaliseY=False):
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
	if normaliseX == True:
		x = np.array(x)
		x = x - min(x)
		x = x/max(x)
	if normaliseY == True:
		y = np.array(y)
		y = y - min(y)
		y = y/max(y)
	return {"x": x, "y": y}

def addPlot(dataX, dataY, Color="blue", lineStyle="solid", Marker="", Label="", errorBarX=None, errorBarY=None, Ecolor="#000000", errorSize=None, errorThickness=None, percentage=False, lineWidth=2):
	#posX = position[0]
	#posY = position[1]
	#position = (posY-1) * self.x + posX
	#subplot = self.subplotsDict.get(position)
	if percentage:
		errorX = np.array(dataX)*(errorBarX/100)
		errorY = np.array(dataY)*(errorBarY/100)
		ax.errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorX, yerr=errorY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)
	else:
		ax.errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorBarX, yerr=errorBarY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)

#Import Datas
data1 = addData(r"C:\Users\Benjamin\Desktop\École\Université\4) SESSION D'HIVER 2022\Travaux Pratique d'optique Photonique\Labo 1\donneesPolarisation.txt", ",", deleteFirstRow=1)
data2 = addData(r"C:/Users/Benjamin/Desktop/École/Université/4) SESSION D'HIVER 2022/Travaux Pratique d'optique Photonique/Labo 1/dataMalus.txt", ",", deleteFirstRow=1)

#Plots
fig, ax = plt.subplots(nrows=1, ncols=1)

addPlot(data1.get("x"), data1.get("y"))
addPlot(data2.get("x"), data2.get("y"))
plt.show()
