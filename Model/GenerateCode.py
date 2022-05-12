import os
dirPath = os.path.abspath("") + os.sep + "Code" + os.sep # With the GUI

def generate(name, datas, dimension, plots, functions, fits, p0s, legends, title, xSubtitles, ySubtitles, testing=True):
    if testing:
    	dirPath = os.path.abspath("")[:-10] + os.sep + "Code" + os.sep
    with open(dirPath + name + ".py", "w+") as file:
        file.write('''# coding=Latin1\n''')
        if len(functions) >= 1:
        	file.write('''from scipy.optimize import curve_fit\n''')
        importStatement(file)
        file.write('''plt.style.use("https://raw.githubusercontent.com/dccote/Enseignement/master/SRC/dccote-errorbars.mplstyle")\n''')
        functionData(file)
        functionPlot(file, dimension)
        if len(functions) >= 1:
        	file.write('''\n''')
        	functionCurvefit(file, functions)
        file.write('''#Import Datas\n''')
        importData(file, datas)
        file.write('''\n''')
        if len(functions) >= 1:
        	file.write('''#Curvefits\n''')
        	curvefitData(file, fits, p0s)
        	file.write('''\n''')
        file.write('''#Plots\n''')
        file.write(f'''fig, ax = plt.subplots(nrows={dimension.row}, ncols={dimension.col})\n''')
        file.write('''\n''')
        plotData(file, dimension, plots)
        file.write('''\n''')
        if not title.text == "":
        	addTitle(file, title)
        if len(list(xSubtitles.keys())) != 0:
        	addXSubtitles(file, dimension, xSubtitles)
        if len(list(ySubtitles.keys())) != 0:
        	addYSubtitles(file, dimension, ySubtitles)
        if len(list(legends.keys())) != 0:
        	addLegends(file, dimension, legends)
        file.write('''plt.show()''')
        file.close()

# Always Executed

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

def functionPlot(file, dimension):
	if dimension.col == 1 and dimension.row == 1:
		file.write('''def addPlot(dataX, dataY, Color="blue", lineStyle="solid", Marker="", Label="", errorBarX=None, errorBarY=None, Ecolor="#000000", errorSize=None, errorThickness=None, percentage=False, lineWidth=2):\n''')
		file.write('''	if percentage:\n''')
		file.write('''		errorX = np.array(dataX)*(errorBarX/100)\n''')
		file.write('''		errorY = np.array(dataY)*(errorBarY/100)\n''')
		file.write('''		ax.errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorX, yerr=errorY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)\n''')
		file.write('''	else:\n''')
		file.write('''		ax.errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorBarX, yerr=errorBarY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)\n''')
		file.write('''\n''')
	elif dimension.col == 1 or dimension.row == 1:
		file.write('''def addPlot(position, dataX, dataY, Color="blue", lineStyle="solid", Marker="", Label="", errorBarX=None, errorBarY=None, Ecolor="#000000", errorSize=None, errorThickness=None, percentage=False, lineWidth=2):\n''')
		file.write('''	if percentage:\n''')
		file.write('''		errorX = np.array(dataX)*(errorBarX/100)\n''')
		file.write('''		errorY = np.array(dataY)*(errorBarY/100)\n''')
		file.write('''		ax[position].errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorX, yerr=errorY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)\n''')
		file.write('''	else:\n''')
		file.write('''		ax[position].errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorBarX, yerr=errorBarY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)\n''')
		file.write('''\n''')
	else:
		file.write('''def addPlot(position, dataX, dataY, Color="blue", lineStyle="solid", Marker="", Label="", errorBarX=None, errorBarY=None, Ecolor="#000000", errorSize=None, errorThickness=None, percentage=False, lineWidth=2):\n''')
		file.write('''	if percentage:\n''')
		file.write('''		errorX = np.array(dataX)*(errorBarX/100)\n''')
		file.write('''		errorY = np.array(dataY)*(errorBarY/100)\n''')
		file.write('''		ax[position].errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorX, yerr=errorY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)\n''')
		file.write('''	else:\n''')
		file.write('''		ax[position[0]][position[1]].errorbar(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker, label=Label, xerr=errorBarX, yerr=errorBarY, barsabove=True, ecolor=Ecolor, capsize=errorSize, capthick=errorThickness, linewidth=lineWidth)\n''')
		file.write('''\n''')

# Executed if needed

def addTitle(file, title):
	file.write(f'''fig.suptitle("{title.text}", fontsize={title.fontSize})\n''')

def addXSubtitles(file, dimension, subtitles):
	if dimension.col == 1 and dimension.row == 1:
		subtitle = subtitles[str(list(subtitles.keys())[0])]
		file.write(f'''ax.set_xlabel("{subtitle.text}", fontsize={subtitle.fontSize})\n''')
	elif dimension.col == 1 or dimension.row == 1:
		if dimension.col == 1:
			index = 1
		else:
			index = 0
		for pos in list(subtitles.keys()):
			title = subtitles.get(pos)
			valueMin = pos.find("(")
			valueMax = pos.find(")")
			position = pos[valueMin+1:valueMax]
			position = position.split(",")
			position = int(float(position[index]))
			position = position - 1
			file.write(f'''ax[{position}].set_xlabel("{title.text}", fontsize={title.fontSize})\n''')
	else:
		for pos in list(subtitles.keys()):
			title = subtitles.get(pos)
			valueMin = pos.find("(")
			valueMax = pos.find(")")
			position = pos[valueMin+1:valueMax]
			position = position.split(",")
			posY = int(float(position[1])) - 1
			posX = int(float(position[0])) - 1
			file.write(f'''ax[{posX}][{posY}].set_xlabel("{title.text}", fontsize={title.fontSize})\n''')

def addYSubtitles(file, dimension, subtitles):
	if dimension.col == 1 and dimension.row == 1:
		subtitle = subtitles[str(list(subtitles.keys())[0])]
		file.write(f'''ax.set_ylabel("{subtitle.text}", fontsize={subtitle.fontSize})\n''')
	elif dimension.col == 1 or dimension.row == 1:
		if dimension.col == 1:
			index = 1
		else:
			index = 0
		for pos in list(subtitles.keys()):
			title = subtitles.get(pos)
			valueMin = pos.find("(")
			valueMax = pos.find(")")
			position = pos[valueMin+1:valueMax]
			position = position.split(",")
			position = int(float(position[index]))
			position = position - 1
			file.write(f'''ax[{position}].set_ylabel("{title.text}", fontsize={title.fontSize})\n''')
	else:
		for pos in list(subtitles.keys()):
			title = subtitles.get(pos)
			valueMin = pos.find("(")
			valueMax = pos.find(")")
			position = pos[valueMin+1:valueMax]
			position = position.split(",")
			posY = int(float(position[1])) - 1
			posX = int(float(position[0])) - 1
			file.write(f'''ax[{posX}][{posY}].set_ylabel("{title.text}", fontsize={title.fontSize})\n''')

def addLegends(file, dimension, legends):
	if dimension.col == 1 and dimension.row == 1:
		fontSize = legends[str(list(legends.keys())[0])]
		file.write(f'''ax.legend(loc=1, fontsize={fontSize}).set_draggable(state=True)\n''')
	elif dimension.col == 1 or dimension.row == 1:
		if dimension.col == 1:
			index = 1
		else:
			index = 0
		for pos in list(legends.keys()):
			fontSize = legends.get(pos)
			valueMin = pos.find("(")
			valueMax = pos.find(")")
			position = pos[valueMin+1:valueMax]
			position = position.split(",")
			position = int(float(position[index]))
			position = position - 1
			file.write(f'''ax[{position}].legend(loc=1, fontsize={fontSize}).set_draggable(state=True)\n''')
	else:
		for pos in list(legends.keys()):
			fontSize = legends.get(pos)
			valueMin = pos.find("(")
			valueMax = pos.find(")")
			position = pos[valueMin+1:valueMax]
			position = position.split(",")
			posY = int(float(position[1])) - 1
			posX = int(float(position[0])) - 1
			file.write(f'''ax[{posX}][{posY}].legend(loc=1, fontsize={fontSize}).set_draggable(state=True)\n''')

def curvefitData(file, fits, p0s):
	for fit in fits:
		if fit.ID in list(p0s.keys()):
			file.write(f'''{fit.ID} = curvefit({fit.data}, {fit.function}, P0={p0s.get(fit.ID)})\n''')
		else:
			file.write(f'''{fit.ID} = curvefit({fit.data}, {fit.function})\n''')

def plotData(file, dimension, plots):
	if dimension.col == 1 and dimension.row == 1:
		for plot in plots.get(list(plots.keys())[0]):
			file.write(f'''addPlot({plot.dataName}.get("x"), {plot.dataName}.get("y"), "{plot.Color}", "{plot.lineStyle}", "{plot.Marker}", "{plot.Label}", {plot.errorBarX}, {plot.errorBarY}, "{plot.Ecolor}", {plot.errorSize}, {plot.errorThickness}, {plot.percentage}, {plot.lineWidth})\n''')
	elif dimension.col == 1 or dimension.row == 1:
		if dimension.col == 1:
			index = 1
		else:
			index = 0
		for pos in list(plots.keys()):
			for plot in plots.get(pos):
				valueMin = pos.find("(")
				valueMax = pos.find(")")
				position = pos[valueMin+1:valueMax]
				position = position.split(",")
				position = int(float(position[index]))
				position = position - 1
				file.write(f'''addPlot({position}, {plot.dataName}.get("x"), {plot.dataName}.get("y"), "{plot.Color}", "{plot.lineStyle}", "{plot.Marker}", "{plot.Label}", {plot.errorBarX}, {plot.errorBarY}, "{plot.Ecolor}", {plot.errorSize}, {plot.errorThickness}, {plot.percentage}, {plot.lineWidth})\n''')
	else:
		for pos in list(plots.keys()):
			for plot in plots.get(pos):
				valueMin = pos.find("(")
				valueMax = pos.find(")")
				position = pos[valueMin+1:valueMax]
				position = position.split(",")
				posY = int(float(position[1])) - 1
				posX = int(float(position[0])) - 1
				position = (posY, posX)
				file.write(f'''addPlot({position}, {plot.dataName}.get("x"), {plot.dataName}.get("y"), "{plot.Color}", "{plot.lineStyle}", "{plot.Marker}", "{plot.Label}", {plot.errorBarX}, {plot.errorBarY}, "{plot.Ecolor}", {plot.errorSize}, {plot.errorThickness}, {plot.percentage}, {plot.lineWidth})\n''')

def importData(file, datas):
	for dataName in list(datas.keys()):
		data = datas.get(dataName)
		file.write(f'''{dataName} = addData(r"{data.path}", "{data.splitSymbol}", {data.deleteFirstRow}, {data.xValuesColumn}, {data.yValuesColumn}, {data.normaliseX}, {data.normaliseY})\n''')

def functionCurvefit(file, functions):
	for function in functions:
		writeFunction(file, function)
		file.write('''\n''')
	file.write('''def curvefit(data, function, P0=False):\n''')
	file.write('''	if not P0:\n''')
	file.write('''		popt, pcov = curve_fit(function, data.get("x"), data.get("y"))\n''')
	file.write('''	else:\n''')
	file.write('''		popt, pcov = curve_fit(function, data.get("x"), data.get("y"), p0=P0)\n''')
	file.write('''	if len(data.get("x")) < 1000:\n''')
	file.write('''		nbPoint = 1000\n''')
	file.write('''	else:\n''')
	file.write('''		nbPoint = len(data.get("x"))\n''')
	file.write('''	newDataX = np.linspace(data.get("x")[0], data.get("x")[-1], nbPoint)\n''')
	file.write('''	newDataY = function(newDataX, *popt)\n''')
	file.write('''	newData = {"x": newDataX, "y": newDataY}\n''')
	file.write('''	perr = np.sqrt(np.diag(pcov))\n''')
	file.write('''	deltaValues = []\n''')
	file.write('''	for i in range(len(perr)):\n''')
	file.write('''		deltaValues.append(perr[i])\n''')
	file.write('''	print("Optimal Parameters: ",popt)\n''')
	file.write('''	print("Variance :", deltaValues)\n''')
	file.write('''	return newData\n''')
	file.write('''\n''')

def writeFunction(file, function):
	if function == "sinus":
		file.write('''def sinus(X, a, b, c, d):\n''')
		file.write('''	return a*np.sin((X*b)+c)+d\n''')
	elif function == "cosinus":
		file.write('''def cosinus(X, a, b, c, d):\n''')
		file.write('''	return a*np.cos((X*b)+c)+d\n''')
	elif function == "gaussian":
		file.write('''def gaussian(X, a, b, c, d):\n''')
		file.write('''	return a*np.exp((-(b*X+c)**2))+d\n''')
	elif function == "exponential":
		file.write('''def exponential(X, a, b, c, d):\n''')
		file.write('''	return a*np.exp(b*X-c)+d\n''')
	elif function == "":
		file.write('''def straightLine(X, a, b):\n''')
		file.write('''	return a*X + b\n''')
	elif function == "polynomial2Degree":
		file.write('''def polynomial2Degree(X, a, b, c):\n''')
		file.write('''	return a*X**2 + b*x + c\n''')
	elif function == "polynomial3Degree":
		file.write('''def polynomial3Degree(X, a, b, c, d):\n''')
		file.write('''	return a*X**3 + b*X**2 + c*X + d\n''')
	elif function == "polynomial9Degree":
		file.write('''def polynomial9Degree(X, a, b, c, d, e, f, g, h, i, j):\n''')
		file.write('''	return a*X**9 + b*X**8 + c*X**7 + d*X**6 + e*X**5 + f*X**4 + g*X**3 + h*X**2 + i*X + j\n''')
	elif function == "":
		file.write('''def reflexionCoefficient(θ, N2, I0):\n''')
		file.write('''	return I0*(((1-((1/N2)*np.sin(θ*np.pi/180))**2)**(1/2)-N2*np.cos(θ*np.pi/180))/((1-((1/N2)*np.sin(θ*np.pi/180))**2)**(1/2)+N2*np.cos(θ*np.pi/180)))**2\n''')
	else:
		print("error in function: ", function)
