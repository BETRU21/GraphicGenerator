import matplotlib.pyplot as plt
import numpy as np

class Graphic:
	def __init__(self):
		plt.ion()
		self.positions = [] 

	def generateGraph(self, x, y):
		if type(x) is not int:
			raise TypeError("x argument is not int.")
		if type(y) is not int:
			raise TypeError("y argument is not int.")
		self.figure = plt.figure(figsize=(y, x), dpi=400)
		self.x = x
		self.y = y
		self.generatePositions()

	def generatePositions(self):
		self.positions = []
		for i in range(self.x):
			for j in range (self.y):
				pos = (i+1,j+1)
				self.positions.append(pos)

	def addPlot(self, position, dataX, dataY, Color="blue", lineStyle= "solid", Marker=""):
		"""
		Args:
			position(tuple): The position in the figure.
			dataX(list or np.ndarray): Data x to plot in the figure.
			dataY(list of np.ndarray): Data y to plot in the figure.
			[Facultative]
			Color(str): The color of the plot.
			lineStyle(str): "solid", "dotted","dashed", "dashdot"
			Marker(str): Find all possibility at : https://matplotlib.org/stable/api/markers_api.html
		Return:
			None
		"""
		if type(position) is not tuple:
			raise TypeError("position argument is not a tuple.")
		if type(dataX) is not np.ndarray:
            raise TypeError("dataX argument is not a list or numpy.ndarray.")
        if type(dataY) is not np.ndarray:
            raise TypeError("dataY argument is not a list or numpy.ndarray.")
        if type(Color) is not str:
        	raise TypeError("Color argument is not a string.")
        if type(lineStyle) is not str:
        	raise TypeError("lineStyle argument is not a string.")
        if type(Marker) is not str:
        	raise TypeError("Marker argument is not a string.")
		posX = position[0]
		posY = position[1]
		position = (posY-1) * self.x + posX
		ax = self.figure.add_subplot(self.y, self.x, position)
		ax.plot(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker)

	def resetPlot(self):
		self.figure.clear()
		