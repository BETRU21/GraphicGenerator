import numpy as np
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Curvefit import Curvefit

filesPath = os.path.abspath("") + "/files"
dataX = np.array([0,1,2,3])
dataY = np.array([0,2,4,6])

class TestCurvefit(unittest.TestCase):

	def setUp(self):
		self.curvefit = Curvefit()

	def testImportCurvefit(self):
		self.assertIsNotNone(Curvefit)

	def testCreateCurvefitInstance(self):
		self.assertIsNotNone(self.curvefit)

	def testListFunctions(self):
		functions = self.curvefit.listFunctions()
		self.assertListEqual(functions, ["sinus", "cosinus", "gaussian", "exponential", "straightLine", "polynomial2Degree", "polynomial3Degree"])
	
	def testGetFunction(self):
		sinus = self.curvefit.listFunctions()[0]
		function = self.curvefit.getFunction(sinus)
		self.assertIsNotNone(function)

	def testGetFunctionTypeError(self):
		self.assertRaises(TypeError, self.curvefit.getFunction, 1)

	def testGetAllFunctions(self):
		functions = self.curvefit.getAllFunction()
		self.assertTrue(len(functions), 7)

	def testGetFunctionParam(self):
		param = self.curvefit.getFunctionParam("exponential")
		self.assertTrue(len(param), 1)

	def testGetFunctionParamType(self):
		param = self.curvefit.getFunctionParam("exponential")
		self.assertTrue(type(param), type("str"))

	def testGetFunctionParamTypeError(self):
		self.assertRaises(TypeError, self.curvefit.getFunctionParam, 1)

	def testGetAllFunctionParam(self):
		param = self.curvefit.getAllFunctionParam()
		self.assertTrue(len(param), 7)

	def testCurvefitDataXTypeError(self):
		function = self.curvefit.getFunction("straightLine")
		self.assertRaises(TypeError, self.curvefit.curvefit, 1, dataY, function)

	def testCurvefitDataYTypeError(self):
		function = self.curvefit.getFunction("straightLine")
		self.assertRaises(TypeError, self.curvefit.curvefit, dataX, 1, function)

	def testCurvefitFunctionTypeError(self):
		self.assertRaises(TypeError, self.curvefit.curvefit, dataX, dataY, 1)

	def testCurvefitBoundsTypeError(self):
		function = self.curvefit.getFunction("straightLine")
		self.assertRaises(TypeError, self.curvefit.curvefit, dataX, dataY, function, 1)

	def testCurvefitDataValueError(self):
		NewDataY = np.array([0,2,4])
		function = self.curvefit.getFunction("straightLine")
		self.assertRaises(ValueError, self.curvefit.curvefit, dataX, NewDataY, function)

	def testCurvefit(self):
		function = self.curvefit.getFunction("straightLine")
		dataCurvefitY, dataCurvefitX = self.curvefit.curvefit(dataX, dataY, function)
		self.assertTrue(len(dataCurvefitX), len(dataCurvefitY))

	def testCurvefitWithBounds(self):
		function = self.curvefit.getFunction("straightLine")
		dataCurvefitY, dataCurvefitX = self.curvefit.curvefit(dataX, dataY, function, (-4,4))
		self.assertTrue(len(dataCurvefitX), len(dataCurvefitY))

	def testCurrentPopt(self):
		function = self.curvefit.getFunction("straightLine")
		dataCurvefitY, dataCurvefitX = self.curvefit.curvefit(dataX, dataY, function)
		popt = self.curvefit.currentPopt()
		popt = popt.round()
		popt = list(popt)
		self.assertListEqual(popt, [2, 0])

if __name__ == "__main__":
    unittest.main()
