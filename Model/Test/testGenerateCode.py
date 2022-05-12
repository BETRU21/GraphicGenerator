from typing import NamedTuple, Any
import numpy as np
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from GenerateCode import generate

filesPath = os.path.abspath("") + os.sep + "files" + os.sep

class Data(NamedTuple):
	path: str = None
	splitSymbol: str = None
	deleteFirstRow: int = 0
	xValuesColumn: int = 0
	yValuesColumn: int = 1
	normaliseX: bool = False
	normaliseY: bool = False

class Dimension(NamedTuple):
	col: int = None
	row: int = None

class Plot(NamedTuple):
	dataName: str = None
	Color: str = None
	lineStyle: str = None
	Marker: str = None
	Label: str = None
	errorBarX: Any = None
	errorBarY: Any = None
	Ecolor: str = None
	errorSize: int = None
	errorThickness: int = None
	percentage: bool = None
	lineWidth: int = None

class Fit(NamedTuple):
	function: str = None
	ID: str = None
	data: str = None

class Params(NamedTuple):
	ID: str = None
	p0: list = None

class Text(NamedTuple):
	text: str = None
	fontSize: int = None

class Infos(NamedTuple):
	datas: dict = {}
	dimension: Any = Dimension(1,1)
	plots: dict = {}
	curvefits: dict = {}
	p0s: list = []
	ID: int = 0
	legends: dict = {}
	title: Any = Text("", 12)
	xSubtitles: dict = {}
	ySubtitles: dict = {}
	fileName: str = "test1"


class TestGenerateCode():
	def generateCode(self, infos):
		functions, fits, p0s = self.clearCurvefitInfos(infos.curvefits, infos.p0s)
		generate(infos.fileName, infos.datas, infos.dimension, infos.plots, functions, fits, p0s, infos.legends, infos.title, infos.xSubtitles, infos.ySubtitles, testing=True)

	def createDatas1x1(self):
		datas = {'sinus1': Data(path=filesPath + "sinus.csv", splitSymbol=';', deleteFirstRow=1, xValuesColumn=0, yValuesColumn=1, normaliseX=False, normaliseY=False)}
		dimension = Dimension(col=1, row=1)
		plots = {'(1, 1)': [Plot(dataName='sinus1', Color='#48b0b0', lineStyle='solid', Marker='', Label='sinus1', errorBarX=None, errorBarY=None, Ecolor='#000000', errorSize=None, errorThickness=None, percentage=False, lineWidth=2)]}
		curvefits = {}
		p0s = []
		ID = 0
		legends = {'(1, 1)': 12}
		title = Text(text='1x1 Test', fontSize=24)
		xSubtitles = {"(1, 1)": Text(text="x", fontSize=20)}
		ySubtitles = {"(1, 1)": Text(text="y", fontSize=20)}
		fileName = "1x1"
		return Infos(datas, dimension, plots, curvefits, p0s, ID, legends, title, xSubtitles, ySubtitles, fileName)

	def createDatas1x2(self):
		datas = {'sinus1': Data(path=filesPath + "sinus.csv", splitSymbol=';', deleteFirstRow=1, xValuesColumn=0, yValuesColumn=1, normaliseX=False, normaliseY=False)}
		dimension = Dimension(col=1, row=2)
		plots = {'(1, 1)': [Plot(dataName='sinus1', Color='#48b0b0', lineStyle='solid', Marker='', Label='sinus1', errorBarX=None, errorBarY=None, Ecolor='#000000', errorSize=None, errorThickness=None, percentage=False, lineWidth=2)], '(1, 2)': [Plot(dataName='curvefit1', Color='#FF0202', lineStyle='solid', Marker='', Label='sinus2', errorBarX=None, errorBarY=None, Ecolor='#000000', errorSize=None, errorThickness=None, percentage=False, lineWidth=2)]}
		curvefits = {'(1, 2)': [Fit(function='sinus', ID='curvefit1', data='sinus1')]}
		p0s = [Params(ID='curvefit1', p0='None')]
		ID = 1
		legends = {'(1, 1)': 12, '(1, 2)': 12}
		title = Text(text='1x2 Test', fontSize=24)
		xSubtitles = {"(1, 1)": Text(text="x", fontSize=20)}
		ySubtitles = {"(1, 1)": Text(text="y", fontSize=20)}
		fileName = "1x2"
		return Infos(datas, dimension, plots, curvefits, p0s, ID, legends, title, xSubtitles, ySubtitles, fileName)


	def createDatas2x1(self):
		datas = {'sinus1': Data(path=filesPath + "sinus.csv", splitSymbol=';', deleteFirstRow=1, xValuesColumn=0, yValuesColumn=1, normaliseX=False, normaliseY=False)}
		dimension = Dimension(col=2, row=1)
		plots = {'(1, 1)': [Plot(dataName='sinus1', Color='#48b0b0', lineStyle='solid', Marker='', Label='sinus1', errorBarX=None, errorBarY=None, Ecolor='#000000', errorSize=None, errorThickness=None, percentage=False, lineWidth=2)], '(2, 1)': [Plot(dataName='curvefit1', Color='#FF0202', lineStyle='solid', Marker='', Label='sinus2', errorBarX=None, errorBarY=None, Ecolor='#000000', errorSize=None, errorThickness=None, percentage=False, lineWidth=2)]}
		curvefits = {'(2, 1)': [Fit(function='sinus', ID='curvefit1', data='sinus1')]}
		p0s = [Params(ID='curvefit1', p0='None')]
		ID = 1
		legends = {'(1, 1)': 12, '(2, 1)': 12}
		title = Text(text='2x1 Test', fontSize=24)
		xSubtitles = {"(1, 1)": Text(text="x", fontSize=20)}
		ySubtitles = {"(1, 1)": Text(text="y", fontSize=20)}
		fileName = "2x1"
		return Infos(datas, dimension, plots, curvefits, p0s, ID, legends, title, xSubtitles, ySubtitles, fileName)


	def createDatas3x3(self):
		datas = {'sinus1': Data(path=filesPath + "sinus.csv", splitSymbol=';', deleteFirstRow=1, xValuesColumn=0, yValuesColumn=1, normaliseX=False, normaliseY=False)}
		dimension = Dimension(col=3, row=3)
		plots = {'(1, 1)': [Plot(dataName='sinus1', Color='#48b0b0', lineStyle='solid', Marker='', Label='sinus1', errorBarX=None, errorBarY=None, Ecolor='#000000', errorSize=None, errorThickness=None, percentage=False, lineWidth=2)], '(2, 2)': [Plot(dataName='sinus1', Color='#aa00ff', lineStyle='solid', Marker='', Label='sinus1', errorBarX=0.0, errorBarY=5.0, Ecolor='#000000', errorSize=2, errorThickness=2, percentage=True, lineWidth=2)], '(3, 3)': [Plot(dataName='curvefit1', Color='#FF0202', lineStyle='solid', Marker='', Label='sinus2', errorBarX=None, errorBarY=None, Ecolor='#000000', errorSize=None, errorThickness=None, percentage=False, lineWidth=2)]}
		curvefits = {'(3, 3)': [Fit(function='sinus', ID='curvefit1', data='sinus1')]}
		p0s = [Params(ID='curvefit1', p0='None')]
		ID = 1
		legends = {'(1, 1)': 12, '(1, 2)': 12, '(1, 3)': 12, '(2, 1)': 12, '(2, 2)': 12, '(2, 3)': 12, '(3, 1)': 12, '(3, 2)': 12, '(3, 3)': 12}
		title = Text(text='3x3 Test', fontSize=24)
		xSubtitles = {"(1, 1)": Text(text="x", fontSize=20)}
		ySubtitles = {"(1, 1)": Text(text="y", fontSize=20)}
		fileName = "3x3"
		return Infos(datas, dimension, plots, curvefits, p0s, ID, legends, title, xSubtitles, ySubtitles, fileName)

	def clearCurvefitInfos(self, curvefits, P0S):
		functions = []
		validID = []
		fits = []
		for pos in list(curvefits.keys()):
			for fit in (curvefits.get(pos)):
				if not fit.function in functions:
					functions.append(fit.function)
					validID.append(fit.ID)
					fits.append(fit)
		p0s = {}
		for ID in validID:
			for params in P0S:
				if ID == params.ID:
					if params.p0 != "None":
						p0s[params.ID] = params.p0
		return functions, fits, p0s

generateModule = TestGenerateCode()
data = generateModule.createDatas3x3()
generateModule.generateCode(data)
data = generateModule.createDatas1x1()
generateModule.generateCode(data)
data = generateModule.createDatas2x1()
generateModule.generateCode(data)
data = generateModule.createDatas1x2()
generateModule.generateCode(data)

