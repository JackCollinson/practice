# Practicing lambda expressions

# 1. hello world
print (lambda x, y : x + y)('hello ', 'world!')

# 2. x squared
def square(x):
    return x * x
print 'x^2', square(9)

f = (lambda x : x * x)
print 'x^2', f(10)

# 3. maximum difference between two of three numbers
maxDiff = (lambda x, y, z : max( max(abs(z - x), abs(z - y)), abs(y - x) ))
print 'max diff:', maxDiff(20,43,-60)

# 4. concatenate words to form sentence
def sentence(words):
    result = ""
    for word in words:
        result += word  + ' '
    return result
print 'sentence:', sentence(['this','is','a','sentence'])

g = reduce(lambda x, y :  x + ' ' + y, ['lambda','functions','are','very','easy'])
print 'sentence:', g

# 5. print sum of numbers
nums = [1,2,3,4,5]
print 'sum of numbers:', reduce(lambda x, y : x + y, nums)

# 6. flatten list of lists
l = [[1, 2, 3], [4, 5, 6], [7], [8, 9]]
print 'flat:', reduce(lambda x, y: x + y, l)

#print reduce x, y : x * y,
