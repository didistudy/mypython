'''
Created on Feb 9, 2017

@author: yudi
'''
import unittest
from exercise.mathpack import MathPack


class MathPackTest(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_oddoreven(self):
        mathpack = MathPack()
        mathpack.oddoreven()
        pass


# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()