import numpy as np
import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from Curvefit import Curvefit

filesPath = os.path.abspath("") + "/files"

class TestCurvefit(unittest.TestCase):

	def setUp(self):
		self.Curvefit = Curvefit()

	def testImportCurvefit(self):
		self.assertIsNotNone(Curvefit)

	def testCreateCurvefitInstance(self):
		self.assertIsNotNone(self.Curvefit)

if __name__ == "__main__":
    unittest.main()