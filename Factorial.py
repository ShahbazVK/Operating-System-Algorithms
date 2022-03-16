# 1) Design the recursive function for calculating the factorial and calculate its complexity.
from timeit import default_timer as timer
def factorial(num):
    if num>0:
        return num * factorial(num-1)
    else:
        return 1
start=timer()
print(factorial(10))
print("Time taken:",timer()-start)