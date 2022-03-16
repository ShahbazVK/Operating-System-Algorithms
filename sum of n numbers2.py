# SUM OF NUMBERS BY LOOPING
from timeit import default_timer as timer
def sum(n):
    start = timer()
    total=0
    for i in range(n):
        item=i
        total=total + item +1
    print(timer() - start," time taken")
    return total
user=int(input("Enter Range: "))
print("The sum of 1 to",user,"numbers is: ",sum(user))