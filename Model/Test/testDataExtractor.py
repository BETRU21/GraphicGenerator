import numpy as np
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DataExtractor import DataExtractor

filesPath = os.path.abspath("") + "/files"

dataTXT = filesPath + "/dataTXT.txt"
dataCSV = filesPath + "/dataCSV.csv"
data3Columns = filesPath + "/data3Columns.txt"
dataCutRow = filesPath + "/dataCutRow.txt"

class TestDataExtractor(unittest.TestCase):

	def setUp(self):
		self.DataExtractor = DataExtractor()

	def testImportDataExtractor(self):
		self.assertIsNotNone(DataExtractor)

	def testCreateDataExtractorInstance(self):
		self.assertIsNotNone(self.DataExtractor)

	def testDefaultDataDictIsEmpty(self):
		self.assertEqual(len(self.DataExtractor.dataDict), 0)

	def testAddDataWithDataTXT(self):
		self.DataExtractor.addData(dataTXT, "data", ",")
		self.assertEqual(len(self.DataExtractor.dataDict), 1)

	def testAddDataWithDataCSV(self):
		self.DataExtractor.addData(dataCSV, "data", ",")
		self.assertEqual(len(self.DataExtractor.dataDict), 1)

	def testAddDataWithData3Columns(self):
		self.DataExtractor.addData(data3Columns, "data", ",", xValuesPos=1, yValuesPos=2)
		self.assertEqual(len(self.DataExtractor.dataDict), 1)

	def testAddDataWithDataCutRow(self):
		self.DataExtractor.addData(dataCutRow, "data", ",", deleteFirstRow=2)
		self.assertEqual(len(self.DataExtractor.dataDict), 1)

	def testAddDataColumnsOutOfRange(self):
		self.assertRaises(IndexError, self.DataExtractor.addData, dataTXT, "data", ",", xValuesPos=1, yValuesPos=2)

	def testAddDataWithDataCutRowWithoutCuttingRow(self):
		self.assertRaises(ValueError, self.DataExtractor.addData, dataCutRow, "data", ",", deleteFirstRow=1)

	def testAddDataWrongPathArgument(self):
		WrongPath = filesPath + "/nothing.txt"
		self.assertRaises(FileNotFoundError, self.DataExtractor.addData, WrongPath, "data", ",")

	def testAddDataBadTypePathArgument(self):
		self.assertRaises(TypeError, self.DataExtractor.addData, 3, "data", ",")

	def testAddDataBadTypeFileNameArgument(self):
		self.assertRaises(TypeError, self.DataExtractor.addData, dataTXT, 3, ",")

	def testAddDataBadTypeSplitSymbolArgument(self):
		self.assertRaises(TypeError, self.DataExtractor.addData, dataTXT, "data", 3)

	def testAddDataBadTypeDeleteFirstRowArgument(self):
		self.assertRaises(TypeError, self.DataExtractor.addData, dataTXT, "data", ",", deleteFirstRow="1")

	def testAddDataBadTypexValuesPosArgument(self):
		self.assertRaises(TypeError, self.DataExtractor.addData, dataTXT, "data", ",", xValuesPos="1")

	def testAddDataBadTypeyValuesPosArgument(self):
		self.assertRaises(TypeError, self.DataExtractor.addData, dataTXT, "data", ",", yValuesPos="1")

	def testResetDataDict(self):
		self.DataExtractor.resetDataDict()
		self.assertEqual(len(self.DataExtractor.dataDict), 0)

	def testDeleteData(self):
		self.DataExtractor.addData(dataTXT, "data1", ",")
		self.DataExtractor.deleteData("data1")
		self.assertEqual(len(self.DataExtractor.dataDict), 0)

	def testDeleteDataWithoutData(self):
		self.assertRaises(KeyError, self.DataExtractor.deleteData, "data1")

	def testGetData(self):
		self.DataExtractor.addData(dataTXT, "data1", ",")
		data1 = self.DataExtractor.getData("data1")
		self.assertIsNotNone(data1)

	def testGetDataWithoutData(self):
		data1 = self.DataExtractor.getData("data1")
		self.assertIsNone(data1)

if __name__ == "__main__":
    unittest.main()