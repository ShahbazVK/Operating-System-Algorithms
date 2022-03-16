# FIND MINIMUM NUMBER BY 2 LOOPS
from timeit import default_timer as timer
def minimum(total):
    numbers=[]
    for i in range(total):
        # print(i)
        user=int(input("Enter number: "))
        numbers.append(user)
    print("\nUSER INPUT",numbers,"\n")
    start=timer()
    for i in range(total):
        for j in range(total):
        # print("smallest", smallest,"\nnumbers", numbers[i])
            if (numbers[i]<numbers[j]):
            # print(smallest,">=",numbers[i])
                temp=numbers[j]
                numbers[j]=numbers[i]
                numbers[i]=temp
        # print(numbers)
    print("The minimum number is: ",numbers[0])
    # print("FINAL",numbers)
    print("The time taken by the algorithm is:", timer()-start)
total=int(input("Enter range: "))

minimum(total)