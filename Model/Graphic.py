import matplotlib.pyplot as plt

class Graphic:
	def __init__(self):
		plt.ion()
		self.positions = [] 

	def generateGraph(self, x, y):
		self.figure = plt.figure(figsize=(y, x), dpi=80)
		self.x = x
		self.y = y
		self.generatePositions()

	def generatePositions(self):
		self.positions = []
		for i in range(self.x):
			for j in range (self.y):
				pos = (i+1,j+1)
				self.positions.append(pos)

	def resetPlot(self):
		self.figure.clear()

	def addPlot(self, position, dataX, dataY, Color="blue", lineStyle= "solid", Marker="" ):
		posX = position[0]
		posY = position[1]
		position = (posY-1) * self.x + posX
		ax = self.figure.add_subplot(self.y, self.x, position) # hauteur, largeur, position
		ax.plot(dataX, dataY, color=Color, linestyle=lineStyle, marker=Marker)





		# supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'

		