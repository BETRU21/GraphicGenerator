import os
applicationPath = os.path.abspath("")[:-5] + "Code" + os.sep
print(applicationPath)

datas = {"data1": "C:{0}Users{0}Benjamin{0}Desktop{0}École{0}Université{0}4) SESSION D'HIVER 2022{0}Travaux Pratique d'optique Photonique{0}Labo 1{0}donneesPolarisation.txt".format(os.sep), "data2": "C:/Users/Benjamin/Desktop/École/Université/4) SESSION D'HIVER 2022/Travaux Pratique d'optique Photonique/Labo 1/dataMalus.txt".format(os.sep)}
splitSymbol = ","
deletefirstrow = 1
dimension = (1,1)



def generate(name):
    with open(applicationPath + name + ".py", "w+") as file:
        file.write('''# coding=Latin1\n''')
        importStatement(file)
        functionData(file)
        functionPlot(file)
        file.write('''#Import Datas\n''')
        importData(file, datas)
        file.write('''\n''')
        file.write('''#Plots\n''')
        file.write(f'''fig, ax = plt.subplots(nrows={dimension[0]}, ncols={dimension[1]})\n''')
        file.write('''\n''')
        plotData(file, datas)
        file.write('''plt.show()\n''')
        file.close()

def plotData(file, datas):
	if dimension == (1,1):
		for i in list(datas.keys()):
			place = 0
			file.write(f'''addPlot({i}.get("x"), {i}.get("y"))\n''')
	else:
		for i in list(datas.keys()):
			place = 0
			file.write(f'''addPlot({place}, {i}.get("x"), {i}.get("y"))\n''')

def importData(file, datas):
	for i in list(datas.keys()):
		file.write(f'''{i} = addData(r"{datas.get(i)}", "{splitSymbol}", deleteFirstRow={deletefirstrow})\n''')

def importStatement(file):
    file.write('''import matplotlib.pyplot as plt\n''')
    file.write('''import numpy as np\n''')
    file.write('''import os\n''')

def functionData(file):
	file.write('''\n''')
	file.write('''def addData(path, splitSymbol, deleteFirstRow=0, xValuesPos=0, yValuesPos=1, normaliseX=False, normaliseY=False):\n''')
	file.write('''	fich = open(path, "r")\n''')
	file.write('''	fich_str = list(fich)[deleteFirstRow:]\n''')
	file.write('''	fich.close()\n''')
	file.write('''	x = []\n''')
	file.write('''	y = []\n''')
	file.write('''	for i in fich_str:\n''')
	file.write('''		elem_str = i.replace("\\n", "")\n''')
	file.write('''		elem = elem_str.split(splitSymbol)\n''')
	file.write('''		x.append(float(elem[xValuesPos]))\n''')
	file.write('''		y.append(float(elem[yValuesPos]))\n''')
	file.write('''	if normaliseX == True:\n''')
	file.write('''		x = np.array(x)\n''')
	file.write('''		x = x - min(x)\n''')
	file.write('''		x = x/max(x)\n''')
	file.write('''	if normaliseY == True:\n''')
	file.write('''		y = np.array(y)\n''')
	file.write('''		y = y - min(y)\n''')
	file.write('''		y = y/max(y)\n''')
	file.write('''	return {"x": x, "y": y}\n''')
	file.write('''\n''')

def functionPlot(file):
	if dimension == (1,1):
		file.write('''def addPlot(dataX, dataY, Color="blue", lineStyle="solid", Marker="", Label="", errorBarX=None, errorBarY=None, Ecolor="#000000", errorSize=None, errorThickness=None, percentage=False, lineWidth=2):\n''')
		file.write('''	#posX = position[0]\n''')
		file.write('''	#posY = position[1]\n''')
		file.write('''	#position = (posY-1) * self.x + posX\n''')
		file.write('''	#subplot = self.subplotsDict.get(position)\n''')
		file.write('''	if percentage:\n''')
		file.write('''		errorX = np.array(dataX)*(errorBarX/100)\n''')
		file.write('''		errorY = np.array(dataY)*(errorBarY/100)\n''')
		file.write('''		ax.errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorX, yerr=errorY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)\n''')
		file.write('''	else:\n''')
		file.write('''		ax.errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorBarX, yerr=errorBarY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)\n''')
		file.write('''\n''')
	else:
		file.write('''def addPlot(position, dataX, dataY, Color="blue", lineStyle="solid", Marker="", Label="", errorBarX=None, errorBarY=None, Ecolor="#000000", errorSize=None, errorThickness=None, percentage=False, lineWidth=2):\n''')
		file.write('''	#posX = position[0]\n''')
		file.write('''	#posY = position[1]\n''')
		file.write('''	#position = (posY-1) * self.x + posX\n''')
		file.write('''	#subplot = self.subplotsDict.get(position)\n''')
		file.write('''	if percentage:\n''')
		file.write('''		errorX = np.array(dataX)*(errorBarX/100)\n''')
		file.write('''		errorY = np.array(dataY)*(errorBarY/100)\n''')
		file.write('''		ax[position].errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorX, yerr=errorY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)\n''')
		file.write('''	else:\n''')
		file.write('''		ax[position].errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorBarX, yerr=errorBarY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)\n''')
		file.write('''\n''')




generate("allo")
