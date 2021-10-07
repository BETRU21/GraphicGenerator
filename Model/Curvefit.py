import numpy as np
from scipy.optimize import curve_fit

class Curvefit:
	def __init__(self):
		self.functions = {}
		self.functionsParam = {}
		self.popt = []
		self.buildFunctions()
		self.buildFunctionsParam()

	# Public functions

	def listFunctions(self):
		"""List premade functions."""
		return list(self.functions.keys())

	def getFunction(self, key):
		if type(key) is not str:
			raise TypeError(string)
		return self.functions.get(key)

	def getAllFunction(self):
		return self.functions

	def getFunctionParam(self, key):
		if type(key) is not str:
			raise TypeError(string)
		return self.functionsParam.get(key)

	def getAllFunctionParam(self):
		return self.functionsParam

	def currentPopt(self):
		return self.popt

	def curvefit(self, dataX, dataY, function, bounds=False):
		"""Curvefit a function with data.
		Args:
			dataX()
		"""
		if type(dataX) is not np.ndarray:
			raise TypeError("dataX is not a np.ndarray.")
		if type(dataY) is not np.ndarray:
			raise TypeError("dataY is not a np.ndarray.")
		if len(dataX) != len(dataY):
			raise ValueError("data len are not equal.")

		if not bounds:
			popt, pcov = curve_fit(function, dataX, dataY)
		else:
			popt, pcov = curve_fit(function, dataX, dataY, bounds=bounds)

		if len(dataX) < 1000:
			nbPoint = 1000
		else:
			nbPoint = len(dataX)
		newDataX = np.linspace(dataX[0], dataX[-1], nbPoint)
		line = function(newDataX, *popt)
		self.popt = popt
		return line, newDataX

	# Non-public functions

	def buildFunctions(self):
		# Create a method of each function to use it in curve_fit
		self.functions["sinus"] = self.sinus
		self.functions["cosinus"] = self.cosinus
		self.functions["gaussian"] = self.gaussian
		self.functions["exponential"] = self.exponential
		self.functions["straightLine"] = self.straightLine
		self.functions["polynomial2Degree"] = self.polynomial2Degree
		self.functions["polynomial3Degree"] = self.polynomial3Degree

	def buildFunctionsParam(self):
		self.functionsParam["sinus"] = "a*np.sin((X*b)+c)+d | where popt=[a,b,c,d]"
		self.functionsParam["cosinus"] = "a*np.cos((X*b)+c)+d | where popt=[a,b,c,d]"
		self.functionsParam["gaussian"] = "a*np.exp((-(b*X+c)**2))+d | where popt=[a,b,c,d]"
		self.functionsParam["exponential"] = "a*np.exp(b*X-c)+d | where popt=[a,b,c,d]"
		self.functionsParam["straightLine"] = "a*X + b | where popt=[a,b]"
		self.functionsParam["polynomial2Degree"] = "a*X**2 + b*x + c | where popt=[a,b,c]"
		self.functionsParam["polynomial3Degree"] = "a*X**3 + b*X**2 + c*X + d | where popt=[a,b,c,d]"

	def sinus(self, X, a, b, c, d):
		return a*np.sin((X*b)+c)+d

	def cosinus(self, X, a, b, c, d):
		return a*np.cos((X*b)+c)+d

	def gaussian(self, X, a, b, c, d):
		return a*np.exp((-(b*X+c)**2))+d

	def exponential(self, X, a, b, c, d):
		return a*np.exp(b*X-c)+d

	def straightLine(self, X, a, b):
		return a*X + b

	def polynomial2Degree(self, X, a, b, c):
		return a*X**2 + b*x + c

	def polynomial3Degree(self, X, a, b, c, d):
		return a*X**3 + b*X**2 + c*X + d
