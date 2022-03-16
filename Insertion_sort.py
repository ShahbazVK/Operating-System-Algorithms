# Time taken(Worst Case):  3.419999999999812e-05
# Time taken(Average Case):  2.8200000000005998e-05
# Time taken(Best Case):  1.3499999999999623e-05

# djdjdkdkdjjdfkdkdjkd
from timeit import default_timer as timer
import matplotlib.pyplot as plt
arr1 = [4,6,2,63,5,2,5,2,5,435,6,5,5343,3536,5,6,4,78,7,4,5,6,4,7,7,36,4,7,6,8,2,98,2,984,747,2,9,4989,3,736637,357,6,73658,7,49,6727,56277,82476,556,7392,986596,279678,64282,7,565,762579,92,259,765,929756,2,5,6,259,84964,7,6479279,625765,5967,6925,6244,628,690,25885,4,93,8,4,7,68294,8,7352,8364,829,9,3746,6,4728,8,28,7,65,6,366,4,66373,8,28,9,49,4392,9,74738,8,4655,678,387,468,392,94,848,8723,67837,67846,8676,86346,3768,63637,683,7,6,7343,78,3,7,9,8,3838,888,789,3478,9,7783,47892,4898,924,7985,77,7527,897,57,2,74754,74,7892,74,2,7479,8,4727,274,78,9,4,797,97,277,4,799,7,8,735,52,7,2684,9,4,3,90,9894,89,578,6893,44,8,993,494,72,92,91,1,101,301,1091,9,8,3,7,37,8,3,7,62,6,5,25,4,5,4,62,4657,28842,7922,87,483,9849,89,4277,48,74,8,2949,8,98,4,3759,78,93,57,57,3,99,578,57,87,8,77,3,87,36,556,25,414,4,1,41,455156,2,3,72,377,23,8,28,8,499,3900,45,31,30,615,9,18,90,56,42,412,6,21,6,198,49,41,95,61,1,33,13,12,54,93,16,4,578,97,95,46,1,981,85,46,4,9,9,764,6,6,49,19,78,62,786,5784,6,746,25,2,6,356,7,5,5,7,25,64,646,645,645,64,7,3737,828,282,38,7,7,46,4635,53,62,7,2,7,84,77,47,83,38,3,7,8,74665,68,583,3,992,9,183,70,17,37,37,6,511,41,12,12,124,24,25,3,567,48,378,38334,89,3,89,483,8376,736,37673,58,78,37676,337,658,787,3735,7836,7376,3767,82873,7837,8763,838,37837,8378,3,47,828782,782,787,287,2764,63,7637,4747,8347,847,83,8783,7878,7,8678,56,785,9949,393,9757,8,3785,783,5,78,7,4,5,6,4,7,7,36,4,7,6,8,2,98,2,984,747,2,9,4989,3,736637,357,6435,6,5,5343,3536,5,6,4,78,7,4,5,6,4,7,7,36,4,7,6,8,2,98,2,984,747,2,9,4989,3,736637,357,6,73658,7,49,6727,56277,82476,556,7392,986596,279678]
arr2=list(arr1)
arr1.sort()
arr3=arr1[::-1]
print(arr1)
print(arr2)
print(arr3)
# arr3.sort()
# arr3=arr3[::-1]
def insertionSort(A):
    for i in range(1,len(A)):
        value = A[i]
        j = i
        while j>0 and A[j-1]>value:
            A[j]=A[j-1]
            j = j-1
        A[j]=value

# print(arr1)
# print(arr2)
# print(arr3)
start1=timer()    
insertionSort(arr1)
time1=timer()-start1
print("Time taken(Best Case): ",timer()-start1)

start2=timer()    
insertionSort(arr2)
time2=timer()-start2
print("Time taken(Average Case): ",timer()-start2)

start3=timer()    
insertionSort(arr3)
time3=timer()-start3
print("Time taken(Worst Case): ",timer()-start3)

plt.xlabel("solutions")
plt.ylabel("running time in milliseconds")
plt.plot(["Best","Average","Worst"],[time1,time2,time3])
plt.show()

print(arr3)