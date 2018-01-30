def factorial(n): 
    if n == 1: 
        return 1
    else:
        return n * factorial(n-1)
 
def print_b_n_times(n):
    for x in range(0, n):
        print('b', x+1, n)



colors = ['red', 'blue', 'green']

print(colors.pop())

p = [1, 2, 3]

f = 0
for x in p:
    f += x 

# print(f) 


l = reduce((lambda x,y : x + y ), p)

# print(l)   
# print(l)

# print_b_n_times(32)

def selfDividingNumbers(num):  
    p = str(num)
    include = True
    for x in p:
        q = int(x)
        if q == 0:
            include = False 
        elif num % q != 0:
            include = False
    return include    

print(selfDividingNumbers(10))

p = list(range(1, 23))
print(p)

f = list(filter(selfDividingNumbers, p))

print(f)