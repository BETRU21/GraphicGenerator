# coding=Latin1
import matplotlib.pyplot as plt
import numpy as np
import os
plt.style.use("https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle")

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
	if percentage:
		errorX = np.array(dataX)*(errorBarX/100)
		errorY = np.array(dataY)*(errorBarY/100)
		ax.errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorX, yerr=errorY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)
	else:
		ax.errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorBarX, yerr=errorBarY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)

#Import Datas
sinus1 = addData(r"C:\Users\Benjamin\Desktop\GithubProjects\GraphicGenerator\Model\Test\files\sinus.csv", ";", 1, 0, 1, False, False)

#Plots
fig, ax = plt.subplots(nrows=1, ncols=1)

addPlot(sinus1.get("x"), sinus1.get("y"), "#48b0b0", "solid", "", "sinus1", None, None, "#000000", None, None, False, 2)

fig.suptitle("1x1 Test", fontsize=24)
ax.set_xlabel("x", fontsize=20)
ax.set_ylabel("y", fontsize=20)
ax.legend(loc=1, fontsize=12).set_draggable(state=True)
plt.show()