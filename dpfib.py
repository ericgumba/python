# Dynamic programming solution for computing fib


def bot_up_fib(n):
    if n == 1:
        return 1
    if n == 2: 
        return 1
    solution = []
    solution.append(1)
    solution.append(1)
 

    for i in range(3,n):
        p = solution[i-2] + solution[i-3]
        solution.append(p)
    
    return solution
    

f = bot_up_fib(50)
print(f)