'''
Created on Feb 19, 2017

@author: yudi
'''
from builtins import str
from _ast import Str

class stringExercise1(object):
    '''
    http://codingbat.com/prob/p115413
    '''


    def __init__(self):
        '''
        Constructor
        '''
    def hello_name(self, name):
        return 'Hello '+ name + '!'
    
    def make_abba(self,a, b):
        return a+b+b+a
    
    def make_tags(self, tag, word):
        return '<'+ tag + '>' + word + '<' + '/'+ tag + '>'
    
    def make_out_word(self, out, word):
        evenindex = int(len(out)/2)
        return out[:evenindex] + word + out[evenindex:]
    
    def extra_end(self, str):
        if len(str) >=2: return str[-2:]*3
        
    def first_two(self, str):
        if len(str) > 1: str = str[:2]
        return  str
    
    def first_half(self,str):
        if len(str)%2 == 0: 
            half_index = int(len(str)/2)
            return str[:half_index] 

    def without_end(self, str):
        if len(str) > 1: return str[1:-1]
        
    def combo_string(self, a, b):
        if len(a) < len(b): return a+b+a
        elif len(a) > len(b): return b+a+b
        elif len(a)==0 and len(b)==0: return None
        else: return 'error'

        # Try out raise an exception here
        
    def non_start(self, a, b):
        if len(a)>0 and len(b) >0 : return a[1:]+b[1:]
        
    def left2(self, str):
        if len(str)>1 : return str[2:]+str[:2]
        
testobject = stringExercise1()

print(testobject.left2('hellp'))

