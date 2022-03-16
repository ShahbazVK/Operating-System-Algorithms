from timeit import default_timer as timer
import matplotlib.pyplot as plt
def insertionSort(list1):
    start=timer()
    # Traverse through 1 to len(list1)
    for i in range(1, len(list1)):
 
        key = list1[i]
 
        # Move elements of list1[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < list1[j] :
                list1[j + 1] = list1[j]
                j -= 1
        list1[j + 1] = key
    print(list1)
    return timer()-start
 
 

def shellSort(list1):
    start=timer()
    # Rearrange elements at each size/2, size/4, size/8, ... intervals
    size=len(list1)
    interval = size // 2
    while interval > 0:
        for i in range(interval, size):
            temp = list1[i]
            j = i
            while j >= interval and list1[j - interval] > temp:
                list1[j] = list1[j - interval]
                j -= interval

            list1[j] = temp
        interval //= 2
    print(list1)
    return timer()-start
    
list1=[9,8,7,6,5,4,2,1]
print(insertionSort(list1))
print(shellSort(list1))

labels=["Shell Sort","Insertion Sort"]
values=[shellSort(list1),insertionSort(list1)]
plt.xlabel("Algorithms")
plt.ylabel("running time in milliseconds")
plt.plot(labels,values)
# print(len(list1))

plt.show()