'''
Created on Feb 19, 2017

@author: yudi
@summary: Writting test cases based on business logic!! 
'''
import unittest
from src.stringexercise1 import stringExercise1

class TestStringExercise1(unittest.TestCase):
    '''The three pars of a test: Arrange, Act, Assert'''
    
    def setUp(self):
        self.teststring = stringExercise1()

    def test_hello_name(self):
        self.assertEqual('Hello John!', self.teststring.hello_name('John'))
    
    def test_make_abba(self):
        self.assertEqual('hiwowohi', self.teststring.make_abba('hi', 'wo'))
        
    def test_make_tags(self):
        self.assertEqual('<i>Hoho</i>', self.teststring.make_tags('i', 'Hoho'))
        
    def test_make_out_word(self):
        self.assertEqual('[[word]]', self.teststring.make_out_word('[[]]', 'word'))
   
    # Good examples that test different functions of extra_end, when length is more than 1 and when 
    # is less than 1 or empty
    def test_extra_end_when_string_length_more_than_one(self):
        self.assertEqual('hohoho', self.teststring.extra_end('hoho'))
        
    def test_extra_end_when_string_length_less_than_one(self):
        self.assertEqual(None, self.teststring.extra_end(''))
        
    def test_first_two_when_string_lenth_more_than_one(self):
        self.assertEqual('he', self.teststring.first_two('hello'),'Return the string made of its first two chars')
    def test_first_two_when_string_lenth_is_one(self):
        self.assertEqual('X', self.teststring.first_two('X'), 'Return what it is')
    def test_first_two_when_string_is_empty(self):
        self.assertEqual('', self.teststring.first_two(''), 'Return empty')
        
    def test_combo_string_when_a_shorter(self):
        self.assertEqual('abcefghabc', self.teststring.combo_string('abc', 'efgh'))
    def test_combo_string_when_b_shorter(self):
        self.assertEqual('1235678123', self.teststring.combo_string('5678', '123'))
    def test_combo_string_when_a_b_same_length(self):
        self.assertEqual('error', self.teststring.combo_string('abc', 'dfg'))
    def test_combo_string_when_both_empty(self):
        self.assertEqual(None, self.teststring.combo_string('', ''))   
        
    def test_first_half_when_even(self):
        pass
    def tearDown(self):
        pass    
# 
# if __name__ == "__main__":
#     #import sys;sys.argv = ['', 'Test.testName']
#     unittest.main()