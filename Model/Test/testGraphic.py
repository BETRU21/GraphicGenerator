import numpy as np
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Graphic import Graphic

filesPath = os.path.abspath("") + "/files"

position = (1,1)
dataX = np.array([0,1,2,3,4])
dataY = np.array([0,2,4,6,6])
Color = "#e6e6e6"
lineStyle = "-."
Marker = "*"
Label = "This is a label"

class TestGraphic(unittest.TestCase):

	def setUp(self):
		self.graphic = Graphic()

	def testImportGraphic(self):
		self.assertIsNotNone(Graphic)

	def testCreateGraphicInstance(self):
		self.assertIsNotNone(self.graphic)

	def testGenerateGraph(self):
		self.graphic.generateGraph(1,1)
		self.assertTrue(True)

	def testGenerateGraphXError(self):
		self.assertRaises(TypeError, self.graphic.generateGraph, "1", 1)

	def testGenerateGraphYError(self):
		self.assertRaises(TypeError, self.graphic.generateGraph, 1, "1")

	def testAddPlotMinimalArguments(self):
		self.graphic.generateGraph(1,1)
		self.graphic.addPlot(position, dataX, dataY)
		self.assertTrue(True)

	def testAddPlotMaxArguments(self):
		self.graphic.generateGraph(1,1)
		self.graphic.addPlot(position, dataX, dataY, Color, lineStyle, Marker, Label)
		self.assertTrue(True)

	def testAddPlotWrongPosition(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(AttributeError, self.graphic.addPlot, (2,3), dataX, dataY)

	def testAddPlotPositionTypeError(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(TypeError, self.graphic.addPlot, [1,1], dataX, dataY)

	def testAddPlotDataDoNotHaveTheSameLength(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(ValueError, self.graphic.addPlot, position, [1,2,3], dataY)

	def testAddPlotDataInvalid(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(ValueError, self.graphic.addPlot, position, ["a",2,3], dataY)

	def testAddPlotDataXTypeError(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(TypeError, self.graphic.addPlot, position, "1", dataY)

	def testAddPlotColorInvalid(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(ValueError, self.graphic.addPlot, position, dataX, dataY, Color="That's an error")

	def testAddPlotColorTypeError(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(TypeError, self.graphic.addPlot, position, dataX, dataY, Color=1)

	def testAddPlotLineStyleInvalid(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(ValueError, self.graphic.addPlot, position, dataX, dataY, lineStyle="That's an error")

	def testAddPlotLineStyleTypeError(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(TypeError, self.graphic.addPlot, position, dataX, dataY, lineStyle=1)

	def testAddPlotMarkerInvalid(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(ValueError, self.graphic.addPlot, position, dataX, dataY, Marker="That's an error")

	def testAddPlotMarkerTypeError(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(TypeError, self.graphic.addPlot, position, dataX, dataY, Marker=1)

	def testAddPlotLabelTypeError(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(TypeError, self.graphic.addPlot, position, dataX, dataY, Label=1)

	def testDeleteSpecificPlot(self):
		self.graphic.generateGraph(1,1)
		self.graphic.addPlot(position, dataX, dataY)
		self.graphic.deleteSpecificPlot(position)
		self.assertTrue(True)

	def testDeleteSpecificPlotWithNoDataPlot(self):
		self.graphic.generateGraph(1,1)
		self.graphic.deleteSpecificPlot(position)
		self.assertTrue(True)# If there is no data it's ok it's just already "deleted".

	def testDeleteSpecificPlotPositionTypeError(self):
		self.graphic.generateGraph(1,1)
		self.assertRaises(TypeError, self.graphic.deleteSpecificPlot, [1,1])

	def testSetXRange(self):
		self.graphic.generateGraph(1,1)
		self.graphic.addPlot(position, dataX, dataY)
		self.graphic.setXRange(position, [1,2])
		self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()