import numpy as np
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Graphic import Graphic

filesPath = os.path.abspath("") + "/files"

class TestGraphic(unittest.TestCase):

	def setUp(self):
		self.Graphic = Graphic()

	def testImportGraphic(self):
		self.assertIsNotNone(Graphic)

	def testCreateGraphicInstance(self):
		self.assertIsNotNone(self.Graphic)

if __name__ == "__main__":
    unittest.main()