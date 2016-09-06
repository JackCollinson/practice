'''
Given a string, return a string where for every char in the original,
there are two chars.
'''

def double_char(str):
    res = ""
    for letter in str:
        res += letter + letter
    return res

'''
Return the number of times that the string "hi" appears anywhere in the given
string.
'''

def count_hi(str):
    count = 0
    for i in range(len(str)-1):
        if str[i:i+2] == 'hi':
            count += 1
    return count

'''
Return True if the string "cat" and "dog" appear the same number of times in the
given string.
'''

def cat_dog(str):
    cat = 0
    dog = 0
    for i in range(len(str)-2):
        if str[i:i+3] == 'cat':
            cat += 1
        if str[i:i+3] == 'dog':
            dog += 1
    return cat == dog

'''
Return the number of times that the string "code" appears anywhere in the given
string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
'''

def count_code(str):
    count = 0
    for i in range(len(str)-3):
        if str[i:i+2] == 'co' and str[i+3] == 'e':
            count += 1
    return count

'''
Given two strings, return True if either of the strings appears at the very end
of the other string, ignoring upper/lower case differences (in other words, the
computation should not be "case sensitive"). Note: s.lower() returns the
lowercase version of a string.
'''

def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return b.endswith(a) or a.endswith(b)

'''
Return True if the given string contains an appearance of "xyz" where the xyz is
not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does not.
'''

def xyz_there(str):
    if str.startswith('xyz'):
        return True
    for i in range(1,len(str)-3):
        if str[i] != '.' and str[i+1:i+4] == 'xyz':
            return True
    return False
