import re
from builtins import str
def string_times(str, n):
    if n >= 0:
        return str*n
    
def front_times(str, n):
    if n >= 0: return str[0:3]*n
    
def string_bits(str):
    new_str = ''
    i = 0
    while i < len(str):
        new_str += str[i]
        i = i + 2
    return new_str 
#    if i % 2 == 0

def string_splosion(str):
    tmp =''
    for i in range(0,len(str)+1):
        tmp = tmp + str[0:i]
    return tmp

def last2(str):
    count = 0
    if len(str) >= 2:
        word = str[-2:]
        for i in range(len(str)-2):
            if str[i:i+2] == word: count += 1   
    return count 

def str_count(str):
        if len(str) >= 2: return str.count(str[-2:],0,len(str))
        else: return 0    
# why can't str.count? Because str.count counts non-overlapping sub str
def array_count9(nums):
  return nums.count(9)
  
def array_front9(nums):
    return 9 in nums[:4]

def array123(nums):
    exist = False
    if len(nums) >= 3:
        sublist = [1,2,3]
        for i in range(len(nums)):
            if nums[i:i+3] == sublist:
                exist = True
                break
    return exist
        
def string_match(a, b):
    count = 0
    if len(a) >=2 and len(b) >= 2: 
        if len(a) < len(b): 
            length = len(a)
        else: length = len(b)
        for i in range(length-1):
            if a[i:i+2] == b[i:i+2]: count += 1
    return count
        