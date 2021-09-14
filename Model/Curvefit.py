import numpy as np
from scipy.optimize import curve_fit


class Curvefit:
	def __init__(self):
		self.functions = {}
		self.buildFunctions()

	# Public functions

	def listFunctions(self):
		self.functions.key()

	def getFunction(self, key):
		if type(key) is not str:
			tyype = type(key)
			string = f"key is not a string. key is {tyype}"
			raise TypeError(string)
		return self.functions.get(key)

	def curvefit(self, dataX, dataY, function, bounds=False):
		if type(dataX) is not list:
			if type(dataX) is not np.ndarray:
				raise TypeError("dataX is not a list or np.ndarray.")
		if type(dataY) is not list:
			if type(dataY) is not np.ndarray:
				raise TypeError("dataY is not a list or np.ndarray.")
		if len(dataX) != len(dataY):
			raise ValueError("data len are not equal.")

		if not bounds:
			popt, pcov = curve_fit(function, dataX, dataY)
		else:
			popt, pcov = curve_fit(function, dataX, dataY, bounds=bounds)

		line = function(dataX, *popt)
		return (line, popt)

	# Non-public functions

	def buildFunctions(self):
		self.functions["sinus"] = self.sinus
		self.functions["cosinus"] = self.cosinus
		self.functions["gaussian"] = self.gaussian
		self.functions["exponential"] = self.exponential
		self.functions["straightLine"] = self.straightLine
		self.functions["polynomial2Degree"] = self.polynomial2Degree
		self.functions["polynomial3Degree"] = self.polynomial3Degree

	def exponential(self, X, a, b, c, d):
		return a*np.exp(b*X-c)+d

	def sinus(self, X, a, b, c, d):
		return a*np.sin((X*b)+c)+d

	def cosinus(self, X, a, b, c, d):
		return a*np.cos((X*b)+c)+d

	def gaussian(self, X, a, b, c, d):
		return a*np.exp((-(b*X+c)**2))+d

	def straightLine(self, X, a, b):
		return a*X + b

	def polynomial2Degree(self, X, a, b, c):
		return a*X**2 + b*x + c

	def polynomial3Degree(self, X, a, b, c, d):
		return a*X**3 + b*X**2 + c*X + d
