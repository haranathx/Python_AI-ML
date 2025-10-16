# factorial
m = 4

def factorial(m):
    if(m==0 or m==1):
        return 1
    else:
        return m * factorial(m-1)
    
print(factorial(m))



# fibonacci series
n = 4

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
print(fibonacci(n))