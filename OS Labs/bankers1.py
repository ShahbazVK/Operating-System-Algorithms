
totalRes=int(input("Enter total number of resources: "))
total=[0]*totalRes
for i in range(totalRes):
    total[i]=int(input("Enter resource: "))

totalAllocations=int(input("Enter total number of processes: "))
allocated=[]
for i in range(totalAllocations):
    temp=[]
    print("---------Entering process-------------",i+1)
    for j in range(totalRes):
        user=int(input("Enter resource: "))
        temp.append(user)
    allocated.append(temp)
    temp=[]
# allocated=[[0,1,0],[2,0,1],[3,0,2],[2,0,0],[0,1,3]]

max_need=[]
for i in range(totalAllocations):
    temp=[]
    print("---------Entering details of process-------------",i+1)
    for j in range(totalRes):
        user=int(input("Enter max resource: "))
        temp.append(user)
    max_need.append(temp)
    temp=[]
# max_need=[[7,5,3],[3,2,2],[9,0,2],[4,2,2],[5,3,3]]

res_need=[]

print("\n\nTotal Resources:",total)
for i in range(len(allocated)):
    temp_arr=[]
    for j in range(len(total)):
        temp_arr.append(max_need[i][j] - allocated[i][j])
    res_need.append(temp_arr)
print("Resouce Need:",res_need)

allocated_sum=[]

totalSum=[]
for i in range(len(total)):
    sum=0
    for j in range(len(allocated)):
        sum+=allocated[j][i]
    totalSum.append(sum)
    # print(totalSum)

availability=[]
for i in range(len(total)):
    # print(i)
    availability.append(total[i]-totalSum[i])
print("Available resources",availability)

saveQueue=[]
for i in range(len(allocated)):
    saveQueue.append(i)
print("Save Queue:",saveQueue)
x=0
while len(saveQueue)!=0:
    for j in range(len(total)):
        if availability[j]<res_need[saveQueue[x]][j]:
            temp=saveQueue.pop(x)
            saveQueue.append(temp)
            break
        elif j==len(total)-1 and availability[j]<res_need[saveQueue[x]][j]:
            temp=saveQueue.pop(x)
            saveQueue.append(temp)
        elif j==len(total)-1 and availability[j]>=res_need[saveQueue[x]][j]:
            # print("CHALA 2")
            temp=saveQueue.pop(0)
            for k in range(len(total)):
                availability[k]+=allocated[temp][k]
            print("Available resources:",availability)
            break
    print("Save Queue:",saveQueue,"\n")

    # x+=1