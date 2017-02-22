'''
Created on Feb 19, 2017

@author: yudi
'''
import unittest
from src import warmup1
class TestWarmUp1(unittest.TestCase):


    def test_sleep_in(self):
        self.assertTrue(warmup1.sleep_in(True, True))
        self.assertTrue(warmup1.sleep_in(False,True))
        self.assertTrue(warmup1.sleep_in(False,False))
        self.assertFalse(warmup1.sleep_in(True,False))
        
    def test_monkey_trouble(self):
        self.assertTrue(warmup1.monkey_trouble(True, True))
        self.assertTrue(warmup1.monkey_trouble(False, False))
        self.assertFalse(warmup1.monkey_trouble(False, True))
    
    def test_sum_double(self):
        self.assertEqual(12, warmup1.sum_double(3, 3))
        self.assertEqual(5, warmup1.sum_double(2,3))
    
    def test_diff21(self):
        self.assertEqual(0, warmup1.diff21(21))
        self.assertEqual(2, warmup1.diff21(22))
        self.assertEqual(2, warmup1.diff21(19))
        self.assertEqual(1, warmup1.diff21(20))     
        self.assertEqual(19, warmup1.diff21(2))     
        self.assertEqual(18, warmup1.diff21(30))
    
    @unittest.skip("WIP")
    def test_parrot_trouble(self):
        pass
    
    def test_makes10(self):
        self.assertTrue(warmup1.makes10(10, 10))
        self.assertTrue(warmup1.makes10(0, 10))
        self.assertTrue(warmup1.makes10(1, 10))
        self.assertTrue(warmup1.makes10(10, 4))
        self.assertTrue(warmup1.makes10(4, 6))
        self.assertFalse(warmup1.makes10(1, 5))

    def test_near_hundred(self):
        self.assertFalse(warmup1.near_hundred(89))
        self.assertTrue(warmup1.near_hundred(90))
        self.assertTrue(warmup1.near_hundred(91))
        self.assertTrue(warmup1.near_hundred(100))
        self.assertTrue(warmup1.near_hundred(101))
        self.assertTrue(warmup1.near_hundred(110))
        self.assertFalse(warmup1.near_hundred(111))
        self.assertFalse(warmup1.near_hundred(189))
        self.assertTrue(warmup1.near_hundred(190))
        self.assertTrue(warmup1.near_hundred(191))
        self.assertTrue(warmup1.near_hundred(200))
        self.assertTrue(warmup1.near_hundred(210))
        self.assertFalse(warmup1.near_hundred(211))
        
    def test_pos_neg(self):
        self.assertTrue(warmup1.pos_neg(1, -1, False))
        self.assertFalse(warmup1.pos_neg(1, 1, False))
        self.assertFalse(warmup1.pos_neg(-1, -1, False))
        self.assertFalse(warmup1.pos_neg(1, 0, False))
        self.assertFalse(warmup1.pos_neg(1, -1, True))
        self.assertTrue(warmup1.pos_neg(-1, -1, True))
        self.assertFalse(warmup1.pos_neg(1, 1, True))
        self.assertFalse(warmup1.pos_neg(0, -1, True))

    def test_not_string(self):
            self.assertEqual("not at all", warmup1.not_string("not at all"))
            self.assertEqual("not a big issue", warmup1.not_string('a big issue'))
            self.assertEqual('not hi',warmup1.not_string('hi'))
            self.assertEqual('not ', warmup1.not_string(''))

    def test_missing_char(self):
            self.assertEqual('ello', warmup1.missing_char('hello', 0))
            self.assertEqual('hllo', warmup1.missing_char('hello', 1))
            self.assertEqual('helo', warmup1.missing_char('hello', 2))
            self.assertEqual('helo', warmup1.missing_char('hello', 3))
            self.assertEqual('hell', warmup1.missing_char('hello', 4))
            self.assertFalse(warmup1.missing_char('hello', 5))
        
    def test_front_back(self):
            self.assertEqual('a', warmup1.front_back('a'))
            self.assertEqual('ba', warmup1.front_back('ab'))
            self.assertEqual('cba', warmup1.front_back('abc'))
    
    def test_front3(self):
        self.assertEqual('aaa', warmup1.front3('a'))
        self.assertEqual('ababab', warmup1.front3('ab'))
        self.assertEqual('abcabcabc', warmup1.front3('abc'))
        self.assertEqual('abcabcabc', warmup1.front3('abcd'))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()