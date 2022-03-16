def hashing(word,size):
    sum=0
    for i in range(len(word)):
        sum+=ord(word[i])
    index=sum%size
    return index
size=int(input("Enter the size of an array: "))
arr=[0]*size
for i in range(size):
    word=input(f"Enter word {i+1}: ")
    print("\n")
    placement=hashing(word,size)
    if arr[placement]==0:
        arr[placement]=word
        print("After inserting word '",word,"':",arr,"\n\n")
        

    else:
        for j in range(size):
            # print("placement",placement)
            # print((placement+j+1),"<",size)
            # print(arr[placement+j+1],"==",0)
            if (placement+j+1)<size and arr[placement+j+1]==0:
                arr[placement+j+1]=word
                print("After inserting word '",word,"':",arr,"\n\n")
                break
            elif (placement+j+1)>=size and arr[(placement+j+1)-size]==0:
                arr[(placement+j+1)-size]=word
                print("After inserting word '",word,"':",arr,"\n\n")
                break
print("Final Array: ",arr)