# SUM OF NUMBERS BY LOOPING
from timeit import default_timer as timer

def sum(n):
    start = timer()
    total=0
    for i in range(n):
        total=total + i+1
    # end = timer()
    print(timer() - start," time taken")
    print("The sum of 1 to",n,"numbers is: ",total)

user=int(input("Enter Range: "))
sum(user)