def hashing(word,size):
    sum=0
    for i in range(len(word)):
        sum+=ord(word[i])+i
    index=(sum%size)
    return index
size=int(input("Enter the size of an array: "))
arr=[0]*size
for i in range(size):
    word=input(f"Enter word {i+1}: ")
    index=hashing(word,size)
    arr[index]=word
    print(index)
print(arr)