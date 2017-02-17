from builtins import str
def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
    #return(not weekday or vacation)
def monkey_trouble(a_smile, b_smile):
    if (a_smile and b_smile) or (not a_smile and not b_smile):
        return True
    else: return False
#    return (a_smile == b_smile)
def sum_double(a, b):
    if a==b: sum = (a+b)*2
    else: sum = a+b
    return sum

def diff21(n):
    if n<21: diffvalue = 21-n
    else: diffvalue = 2*(n-21)
    return diffvalue

def parrot_trouble(talking, hour):
    if (not talking): return False
    elif (talking and hour in range(7,21)):return False
    else: return True
   # Test the boundary value when writting Unit Test 

def makes10(a, b):
    if (a + b == 10) or a == 10 or b ==10:
        return True
    else: return False 
    #  return (a == 10 or b == 10 or a+b == 10)
def near_hundred(n):
    return((abs(100-n) <= 10) or (abs(200-n) <= 10))

def pos_neg(a, b, negative):
    if(a*b < 0 and not negative): return True
    elif negative and a<0 and b<0: return True
    else: return False

def not_string(str):
    if str.find('not',0,3) == -1: return('not '+ str)
    else: return str
    
def missing_char(str, n):
    if n in range(0,len(str)):
        str = str[0:n]+ str[n+1:len(str)]
        return str
    else: return False 
#     front = str[:n]   # up to but not including n 
#     back = str[n+1:]  # n+1 through end of string
#     return front + back

def front_back(str):
    if len(str) > 1: 
        str = str[-1] + str[1:-1] + str[0]
    return str
# I think my code is better than the solution ～～～

def front3(str):
    front_end = 3
    if len(str) >= front_end :
        str = str[0:front_end]*3
    else : str = str*3
    return str
print(front3('ab'))