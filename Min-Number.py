# FIND MINIMUM NUMBER BY 1 LOOP
from timeit import default_timer as timer
def minimum(total):
    numbers=[]
    for i in range(total):
        # print(i)
        user=int(input("Enter number: "))
        numbers.append(user)
    print("\nUSER INPUT",numbers,"\n")
    start=timer()
    smallest=numbers[0]
    for i in range(total):
        # print("smallest", smallest,"\nnumbers", numbers[i])
        if (smallest>=numbers[i]):
            # print(smallest,">=",numbers[i])
            smallest=numbers[i]
    print("The minimum number is: ",smallest)
    print("The time taken by the algorithm is:", timer()-start)
total=int(input("Enter range: "))
minimum(total)