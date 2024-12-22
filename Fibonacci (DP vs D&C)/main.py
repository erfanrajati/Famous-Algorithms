# Non Recursive
def fib_dp(n):
    '''
    Unable to calculate higher inputs that 1477
    Highest calculated number is:
    fib(1477): 1.307e+308
    time:         0.00054
    '''
    i = 2
    last = 0
    curr = 1
    if n == 1:
        return last
    if n == 2:
        return curr

    while i < n:
        temp = curr
        curr = curr + last
        last = temp
        i += 1
    
    return curr

# Recursive
def fib_rdp(f, memo={1:0, 2:1},  i=3):
    if f == 1 or f == 2:
        return memo[f]

    memo[i] = memo[i-1] + memo[i-2]
    if f == i:
        return memo[i]
    
    return fib_rdp(f, memo, i+1)


# Divide and Conquer
def fib_dc(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    
    return fib_dc(n-1) + fib_dc(n-2)


import time
import sys
sys.setrecursionlimit(3000)
with open("result.txt", 'a') as file:

    # # Recursive Dynamic Programming
    # file.write("\n\n---- Recursive Dynamic Programming ----\n")
    # for i in range(2000, 3000):
    #     print(f"Working on: {i:>4}")
    #     begin = time.time()
    #     result = fib_rdp(i)
    #     runtime = format(time.time() - begin, ".5f")

    #     file.write(f"fib({i}): {format(format(result, '.3e'), '>10')}\n")
    #     file.write(f"time:     {runtime:>10}\n")
    #     file.write("-"*15 + "\n")

    # Non Recursive Dynamic Programming
    file.write("\n\n---- Non Recursive Dynamic Programming ----\n")
    for i in range(1000, 1477):
        print(f"Working on: {i:>4}")
        begin = time.time()
        result = fib_dp(i)
        runtime = format(time.time() - begin, ".5f")

        file.write(f"fib({i}): {format(format(result, '.3e'), '>10')}\n")
        file.write(f"time:     {runtime:>10}\n")
        file.write("-"*15 + "\n")
    
    # Recurisve Divide and Conquer
    file.write("\n\n---- Recursive Divide and Conquer ----\n")
    for i in range(20, 43):
        print(f"Working on: {i:>4}")
        begin = time.time()
        result = fib_dc(i)
        runtime = format(time.time() - begin, ".5f")

        file.write(f"fib({i}): {format(result, '>10')}\n")
        file.write(f"time:     {runtime:>10}\n")
        file.write("-"*15 + "\n")
        
    



    
    