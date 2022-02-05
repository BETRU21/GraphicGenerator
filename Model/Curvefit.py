import numpy as np
from scipy.optimize import curve_fit

class Curvefit:
	def __init__(self):
		self.functions = {}
		self.functionsForm = {}
		self.functionsParams = {}
		self.popt = []
		self.pcov = []
		self.deltaValues = []
		self.buildFunctions()
		self.buildFunctionsForm()
		self.buildFunctionsParams()

	# Public functions

	def listFunctions(self):
		"""List premade functions."""
		return list(self.functions.keys())

	def getFunction(self, key):
		if type(key) is not str:
			raise TypeError("key argument is not a string.")
		return self.functions.get(key)

	def getAllFunction(self):
		return self.functions

	def getFunctionForm(self, key):
		if type(key) is not str:
			raise TypeError("key argument is not a string.")
		return self.functionsForm.get(key)

	def getFunctionParams(self, key):
		if type(key) is not str:
			raise TypeError("key argument is not a string.")
		return self.functionsParams.get(key)

	def getAllFunctionForm(self):
		return self.functionsForm

	def currentPopt(self):
		return self.popt

	def currentPcov(self):
		return self.pcov

	def currentDeltaValues(self):
		return self.deltaValues

	def curvefit(self, dataX, dataY, function, P0=False):
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

		if not P0:
			popt, pcov = curve_fit(function, dataX, dataY)
		else:
			popt, pcov = curve_fit(function, dataX, dataY, p0=P0)


		if len(dataX) < 1000:
			nbPoint = 1000
		else:
			nbPoint = len(dataX)
		newDataX = np.linspace(dataX[0], dataX[-1], nbPoint)
		line = function(newDataX, *popt)
		self.popt = popt
		self.pcov = pcov
		perr = np.sqrt(np.diag(pcov))
		self.deltaValues = []
		for i in range(len(perr)):
			self.deltaValues.append(perr[i])
		print(popt)
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
		self.functions["polynomial9Degree"] = self.polynomial9Degree
		self.functions["reflexionCoefficient"] = self.reflexionCoefficient

	def buildFunctionsForm(self):
		self.functionsForm["sinus"] = "a*np.sin((X*b)+c)+d"
		self.functionsForm["cosinus"] = "a*np.cos((X*b)+c)+d"
		self.functionsForm["gaussian"] = "a*np.exp((-(b*X+c)**2))+d"
		self.functionsForm["exponential"] = "a*np.exp(b*X-c)+d"
		self.functionsForm["straightLine"] = "a*X + b"
		self.functionsForm["polynomial2Degree"] = "a*X**2 + b*x + c"
		self.functionsForm["polynomial3Degree"] = "a*X**3 + b*X**2 + c*X + d"
		self.functionsForm["polynomial9Degree"] = "a*X**9 + b*X**8 + c*X**7 + d*X**6 + e*X**5 + f*X**4 + g*X**3 + h*X**2 + i*X + j"
		self.functionsForm["reflexionCoefficient"] = "((1-((1/N2)*np.sin(θ))**2)**(1/2)-N2*np.cos(θ))/((1-((1/N2)*np.sin(θ))**2)**(1/2)+N2*np.cos(θ))"

	def buildFunctionsParams(self):
		self.functionsParams["sinus"] = "a, b, c, d"
		self.functionsParams["cosinus"] = "a, b, c, d"
		self.functionsParams["gaussian"] = "a, b, c, d"
		self.functionsParams["exponential"] = "a, b, c, d"
		self.functionsParams["straightLine"] = "a, b"
		self.functionsParams["polynomial2Degree"] = "a, b, c"
		self.functionsParams["polynomial3Degree"] = "a, b, c, d"
		self.functionsParams["polynomial9Degree"] = "a, b, c, d, e, f, g, h, i, j"
		self.functionsParams["reflexionCoefficient"] = "N2, I0"

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

	def polynomial9Degree(self, X, a, b, c, d, e, f, g, h, i, j):
		return a*X**9 + b*X**8 + c*X**7 + d*X**6 + e*X**5 + f*X**4 + g*X**3 + h*X**2 + i*X + j

	def reflexionCoefficient(self, θ, N2, I0):
		return I0*(((1-((1/N2)*np.sin(θ*np.pi/180))**2)**(1/2)-N2*np.cos(θ*np.pi/180))/((1-((1/N2)*np.sin(θ*np.pi/180))**2)**(1/2)+N2*np.cos(θ*np.pi/180)))**2