'''
Given a string and a non-negative int n, return a larger string that is n copies
of the original string.
'''

def string_times(str, n):
    res = ""
    for i in range(n):
        res += str
    return res

'''
Given a string and a non-negative int n, we'll say that the front of the string
is the first 3 chars, or whatever is there if the string is less than length 3.
Return n copies of the front;
'''

def front_times(str, n):
    if len(str) < 4:
        front = str
    else:
        front = str[0:3]

    res = ""
    for i in range(n):
        res += front
    return res

'''
Given a string, return a new string made of every other char starting with the
first, so "Hello" yields "Hlo".
'''

def string_bits(str):
    return str[::2] # string spliced from (0):(end):(step=2)

'''
Given a non-empty string like "Code" return a string like "CCoCodCode".
'''

def string_splosion(str):
    res = ""
    for i in range(len(str)):
        res += str[:i+1]
    return res

'''
Given a string, return the count of the number of times that a substring length
2 appears in the string and also as the last 2 chars of the string, so "hixxxhi"
yields 1 (we won't count the end substring).
'''

def last2(str):
    end = str[-2:]
    count = 0
    for i in range(len(str) - 2):
        if str[i:i+2] == end:
            count += 1
    return count

'''
Given an array of ints, return the number of 9's in the array.
'''

def array_count9(nums):
    count = 0
    for num in nums:
        if num == 9:
            count += 1
    return count

'''
Given an array of ints, return True if one of the first 4 elements in the array
is a 9. The array length may be less than 4.
'''

def array_front9(nums):
    for i in range(4):
        if i < len(nums) and nums[i] == 9:
            return True
    return False

'''
Given an array of ints, return True if .. 1, 2, 3, .. appears in the array
somewhere.
'''

def array123(nums):
    for i in range(len(nums) - 2):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False

'''
Given 2 strings, a and b, return the number of the positions where they contain
the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx",
"aa", and "az" substrings appear in the same place in both strings.
'''

def string_match(a, b):
    nrange = min(len(a), len(b))
    count = 0
    for i in range(nrange - 1):
        if a[i:i+2] == b[i:i+2]:
            count += 1
    return count
