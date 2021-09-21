import matplotlib.pyplot as plt
import numpy as np

class Graphic:
	def __init__(self):
		plt.ion()
		self.positions = []
		self.subplotsDict = {}

	# Public Functions

	def deleteSpecificPlot(self, position):
		posX = position[0]
		posY = position[1]
		position = (posY-1) * self.x + posX
		subplot = self.subplotsDict.get(position)
		subplot.clear()

	def generateGraph(self, x, y):
		if type(x) is not int:
			raise TypeError("x argument is not int.")
		if type(y) is not int:
			raise TypeError("y argument is not int.")
		self.figure = plt.figure(figsize=(y, x), dpi=80)
		self.x = x
		self.y = y
		self.generatePositions()
		self.generateSubplots()

	def setXRange(self, position, limit):
		if type(position) is not tuple:
			raise TypeError("position argument is not a tuple.")
		if type(limit) is not list:
			raise TypeError("limit argument is not a list.")
		if len(limit) != 2:
			if len(limit) < 2:
				raise ValueError(f"limit argument is too short ({len(limit)}), len must be 2.")
			if len(limit) > 2:
				raise ValueError(f"limit argument is too long ({len(limit)}), len must be 2.")
		if type(limit[0]) is not float or type(limit[1]) is not float:
			if type(limit[0]) is not int or type(limit[1]) is not int:
				raise ValueError("elements in limit argument are not int or float.")
		posX = position[0]
		posY = position[1]
		position = (posY-1) * self.x + posX
		subplot = self.subplotsDict.get(position)
		subplot.set_xlim(limit)

	def setYRange(self, position, limit):
		if type(position) is not tuple:
			raise TypeError("position argument is not a tuple.")
		if type(limit) is not list:
			raise TypeError("limit argument is not a list.")
		if len(limit) != 2:
			if len(limit) < 2:
				raise ValueError(f"limit argument is too short ({len(limit)}), len must be 2.")
			if len(limit) > 2:
				raise ValueError(f"limit argument is too long ({len(limit)}), len must be 2.")
		if type(limit[0]) is not float or type(limit[1]) is not float:
			if type(limit[0]) is not int or type(limit[1]) is not int:
				raise ValueError("elements in limit argument are not int or float.")
		posX = position[0]
		posY = position[1]
		position = (posY-1) * self.x + posX
		subplot = self.subplotsDict.get(position)
		subplot.set_ylim(limit)

	def addSubtitle(self, position, title):
		if type(position) is not tuple:
			raise TypeError("position argument is not a tuple.")
		if type(title) is not str:
			raise TypeError("title argument is not a string.")
		posX = position[0]
		posY = position[1]
		position = (posY-1) * self.x + posX
		subplot = self.subplotsDict.get(position)
		subplot.set_title(title)

	def deleteSubtitle(self, position):
		if type(position) is not tuple:
			raise TypeError("position argument is not a tuple.")
		posX = position[0]
		posY = position[1]
		position = (posY-1) * self.x + posX
		subplot = self.subplotsDict.get(position)
		subplot.set_title("")

	def addMainTitle(self, title):
		if type(title) is not str:
			raise TypeError("title argument is not a string.")
		self.figure.set_title(title)

	def deleteMainTitle(self):
		self.figure.set_title("")

	def addLegend(self, position):
		if type(position) is not tuple:
			raise TypeError("position argument is not a tuple.")
		posX = position[0]
		posY = position[1]
		position = (posY-1) * self.x + posX
		subplot = self.subplotsDict.get(position)
		subplot.legend(loc=1, fontsize=11)

	def addLegends(self):
		for i, pos in enumerate(self.positions):
			subplot = self.subplotsDict.get(pos)
			subplot.legend(loc=1, fontsize=11)

	def addPlot(self, position, dataX, dataY, Label, Color="blue", lineStyle= "solid", Marker=""):
		"""
		Args:
			position(tuple): The position in the figure.
			dataX(list or np.ndarray): Data x to plot in the figure.
			dataY(list of np.ndarray): Data y to plot in the figure.
			Label(str): Label show when add a legend.
			[Facultative]
			Color(str): The color of the plot.
			lineStyle(str): "solid", "dotted","dashed", "dashdot"
			Marker(str): Find all possibility at : https://matplotlib.org/stable/api/markers_api.html
		Return:
			None
		"""
		if type(position) is not tuple:
			raise TypeError("position argument is not a tuple.")
		if type(dataX) is not list:
			if type(dataX) is not np.ndarray:
				raise TypeError("dataX argument is not a list or numpy.ndarray.")
		if type(dataY) is not list:
			if type(dataY) is not np.ndarray:
				raise TypeError("dataY argument is not a list or numpy.ndarray.")
		if type(Label) is not str:
			raise TypeError("Label argument is not a string.")
		if type(Color) is not str:
			raise TypeError("Color argument is not a string.")
		if type(lineStyle) is not str:
			raise TypeError("lineStyle argument is not a string.")
		if type(Marker) is not str:
			raise TypeError("Marker argument is not a string.")
		posX = position[0]
		posY = position[1]
		position = (posY-1) * self.x + posX
		subplot = self.subplotsDict.get(position)
		subplot.plot(dataX, dataY, label=Label ,color=Color, linestyle=lineStyle, marker=Marker)



	# Non-Public Functions

	def generatePositions(self):
		self.positions = []
		for i in range(self.x):
			for j in range (self.y):
				pos = (i+1,j+1)
				self.positions.append(pos)

	def generateSubplots(self):
		self.subplotsDict = {}
		for i, item in enumerate(self.positions):
			x = item[0]
			y = item[1]
			position = (y-1) * self.x + x
			self.subplotsDict[position] = self.figure.add_subplot(self.y, self.x, position)

	# https://matplotlib.org/stable/gallery/subplots_axes_and_figures/figure_title.html

		