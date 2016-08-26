#-*- coding: utf-8 -*-
"""
solutions to exercises from - http://www.ling.gu.se/~lager/python_exercises.html
exercises by: Torbjörn Lager
solutions by: Jack Collinson
"""

#1
def max(n, m):
    return n if n > m else m

#2
def max3(i, j, k):
    if i > j:
        return i if i > k else k
    return j if j > k else k

def __max3(i, j, k):
    return max(i, max(j,k))

#3
def length(x):
    if not x: return 0
    return 1 + length(x[1:])

#4
def isVowel(x):
    if len(x) > 1 or not x.isalpha(): return "error: enter a single letter"
    return x.lower() in ['a','e','i','o','u']

#5
def translate(str):
    result = ""
    for i in range(len(str)):
        if str[i].isalpha() and not isVowel(str[i]):
            result += str[i] + 'o' + str[i].lower()
        else:
            result += str[i]
    return result

#6
def sum(x):
    result = 0
    for i in x:
        result += i
    return result

def __sum(x):
    return 0 if len(x) == 0 else x[0] + __sum(x[1:])

def multiply(x):
    if len(x) < 1: return 0
    result = x[0]
    for i in range(1,len(x)):
        result *= x[i]
    return result

def __multiply(x):
    if len(x) < 1: return 0
    return x[0] if len(x) == 1 else x[0] * __multiply(x[1:])

#7
def reverse(str):
    result = ""
    for i in range(len(str)):
        result += str[-1 - i]
    return result

#8
def isPalindrome(str):
    for i in range(len(str)):
        if str[i] != str[-1 -i]:
            return False
    return True

#9
def isMember(a, list):
    for i in range(len(list)):
        if a == list[i]:
            return True
    return False

#10
def overlapping(a, b):
    for i in a:
        for j in b:
            if i == j:
                return True
    return False

#11
def generate_n_chars(n, c):
    if n < 0: return "error: enter non-negative number"
    if len(c) > 1: return "error: enter char (str length 1)"
    return n * c

#12
def histogram(h):
    for i in h:
        print(generate_n_chars(i,'x'))

#13
# recursive
def max_in_list(list):
    if len(list) == 0: return None
    if len(list) == 1: return list[0]
    return max(list[0],max_in_list(list[1:]))

# iterative
def __max_in_list(list):
    if len(list) == 0: return 0
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i]
    return max

#14
def length_of_words(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

#15
def find_longest_word(words):
    max = 0
    for word in words:
        if len(word) > max:
            max = len(word)
    return max

#16
def filter_long_words(words, n):
    result = []
    for word in words:
        if len(word) > n:
            result.append(word)
    return result

#17
def __isPalindrome(str):
    compress = ""
    for i in range(len(str)):
        if str[i].isalpha():
            compress += str[i]
    for i in range(len(compress)):
        if compress[i].lower() != compress[-1 -i].lower():
            return False
    return True

#18
def isPangram(sentence):
    alphabet = ['a','b','c','d','e','f','g','h','i','j',
                'k','l','m','n','o','p','q','r','s','t',
                'u','v','w','x','y','z']

    for char in sentence:
        if char.lower() in alphabet:
            alphabet.remove(char.lower())

    return len(alphabet) == 0

# print(isPangram("the quick brown fox jumps over the lazy dog"))

#19
def bottles_on_wall(n):
    if n < 1: return None

    verse = "%d green bottles hanging on the wall, \n" \
            "%d green bottles hanging on the wall, \n" \
            "And if one green bottle should accidentally fall, \n" \
            "There'll be %d green bottles hanging on the wall \n" % (n,n,n-1)

    print(verse)
    bottles_on_wall(n - 1)

def colour_bottles_on_wall(col, n):
    if n < 1: return None

    verse = "%d %s bottles hanging on the wall, \n" \
            "%d %s bottles hanging on the wall, \n" \
            "And if one %s bottle should accidentally fall, \n" \
            "There'll be %d %s bottles hanging on the wall \n" % (n,col,n,col,col,n-1,col)

    print(verse)
    colour_bottles_on_wall(col, n - 1)

#20
def translate2(str):
    christmas = {"merry":"god", "christmas":"jul",
                "and":"och", "happy":"gott",
                "new":"nytt", "year":"år"}

    result = ""
    word = ""
    for i in range(len(str)):
        if str[i].isalpha():
            word += str[i]
            if i == len(str)-1:
                result += dictGet(word,christmas)
        else:
            result += dictGet(word,christmas)
            result += str[i]
            word = ""

    return result

def dictGet(x, dictionary):
    if dictionary.has_key(x):
        return dictionary.get(x)
    return x

#21
def char_freq(str):
    freqs = {}
    for i in str:
        if freqs.has_key(i):
            freqs[i] = freqs.get(i) + 1
        else:
            freqs[i] = 1
    return freqs

# print(str(char_freq("abbabcbdbabdbdbabababcbcbab")))

#22
def caesar13(str):
    key = {'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u',
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c',
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S',
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A',
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I',
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}

    result = ""
    for i in str:
        if i.isalpha():
            result += key.get(i)
        else:
            result += i

    return result

# shifts by N, rather than 13
def caesarN(str, n):
    result = ""
    for i in str:
        result += caesarC(i,n)
    return result

# shifts a char by N, e.g. caesarC('a',3) == 'd'
def caesarC(char, n):
    if char.isalpha():
        upper = char.isupper()
        charToNum = ord(char.lower()) - 97
        numShift = (charToNum + n) % 26
        numToChar = chr(numShift + 97)
        char = numToChar
        if upper: char = char.upper()
        return char
    else:
        return char

# prints string shifted in all possible variations of caesar cipher
def printAllCaesar(str):
    print(str)
    for i in range(1,26):
        print("%d: %s") % (i, caesarN(str, i))

# print(caesar13(" Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"))
#printAllCaesar('haahjrhavujl!')

#23
def correct(str):
    result = ""

    for i in range(len(str)-1):
        if not str[i].isspace():
            result += str[i]
            if str[i+1].isspace():
                result += ' '
            elif str[i] == '.' and not str[i+1] == '.':
                result += ' '

    if not str[len(str)-1].isspace():
        result += str[len(str)-1]

    return result

#print(correct("This   is  very funny  and    cool...Indeed!. "))

#24
def make_3sg_form(word):

    if word.endswith('y') and not isVowel(word[-2]):
        return word[:len(word)-1] + 'ies'

    elif ( word.endswith('o') or word.endswith('ch') or
        word.endswith('s') or word.endswith('sh') or
        word.endswith('x') or word.endswith('z') ):
        return word + 'es'

    return word + 's'


#25

#26
def max_in_list(list):
    return reduce(lambda x, y: max(x,y), list)

"""
Exercise asks: why write function such as this and not call reduce function
directly?
Answer: improves readability of function
"""

#27

# Josephus Problem
# an interesting problem that I came across,
# I attempted solution briefly but was messy;
# found excellent solution, decided to keep here for future reference

"""
Flavius Josephus was a roman historian of Jewish origin.
During the Jewish-Roman wars of the first century AD, he was
in a cave with fellow soldiers, 40 men in all, surrounded by
enemy Roman troops. They decided to commit suicide by standing
in a ring and counting off each third man. Each man so
designated was to commit suicide... Josephus, not wanting to die,
managed to place himself in the position of the last survivor.

In the general version of the problem,
there are n soldiers numbered from 1 to n
and each k-th soldier will be eliminated.
The count starts from the first soldier.
What is the number of the last survivor?

http://mathworld.wolfram.com/JosephusProblem.html
"""

# solution - user: nneonneo, from: stackoverflow, date: Sep 16 2012
# http://stackoverflow.com/questions/12444979/josephus-problm-using-list-in-python?answertab=active#tab-top

# kill every kth man of n men
def josephus(n, k):
    men = range(1, n + 1)
    k -= 1 # pop automatically skips the dead guy
    idx = k
    while len(men) > 1:
        print 'kill', men.pop(idx) # kill prisoner at idx
        idx = (idx + k) % len(men)
    print 'survivor', men[0]
