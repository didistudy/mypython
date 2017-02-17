def string_times(str, n):
    if n >= 0:
        return str*n
    
def string_bits(str):
    new_str = ''
    i = 0
    while i < len(str):
        new_str += str[i]
        i = i + 2
    return new_str 
#    if i % 2 == 0

print(string_bits('a'))