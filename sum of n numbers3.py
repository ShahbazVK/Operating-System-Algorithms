# SUM OF N NUMBERS BY FORMULA
from timeit import default_timer as timer
def sum(n):
    start = timer()
    print(int(n*(n+1)/2))
    print(timer() - start,"time taken")

user=int(input("Enter Range: "))
print("The sum of 1 to",user,"numbers is: ",end="")
sum(user)