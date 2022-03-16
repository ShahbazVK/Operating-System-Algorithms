total_resources=[10,5,7]
process=[
    [[0,1,0],[7,5,3]],
    [[2,0,1],[3,2,2]],
    [[3,0,2],[9,0,2]],
    [[2,0,0],[4,2,2]],
    [[0,1,3],[5,3,3]]
    ]
firstAvailability=[]
totalSum=[]
sum=0
for i in range(len(total_resources)):
    sum+=process[0][0][i]
    sum+=process[1][0][i]
    sum+=process[2][0][i]
    sum+=process[3][0][i]
    sum+=process[4][0][i]
    totalSum.append(sum)
    sum=0
# print(totalSum)


# res need
temp_arr=[]
for i in range(len(process)):
    temp_arr.append(process[i][1][0]-process[i][0][0])
    temp_arr.append(process[i][1][1]-process[i][0][1])
    temp_arr.append(process[i][1][2]-process[i][0][2])
    print(temp_arr)
    process[i].append(1)
    process[i][2]=temp_arr
    
    temp_arr=[]
print(process)


# for i in range(len(process)):
#     if process[]

for i in range(len(total_resources)):
    firstAvailability.append(total_resources[i]-totalSum[i])
# print(firstAvailability)
safeQueue=[]
for i in range(len(process)):
    # print(process[i][2][0])
    # print(firstAvailability[0])
    # print(process[i][2][1])
    # print(firstAvailability[1]) 
    # print(i,process[i][2][3])
    # print(firstAvailability[3])
    if process[i][2][0]<=firstAvailability[0] and  process[i][2][1]<=firstAvailability[1] and process[i][2][2]<=firstAvailability[2]:
        for j in range(len(total_resources)):
            firstAvailability[j]+=process[i][0][j]
    else:
        safeQueue.append(i)
x=0
while len(safeQueue)!=0:
    for j in range(len(total_resources)):
        firstAvailability[j]+=process[x][0][j]
        print(firstAvailability)
    safeQueue.pop(x)
    x+=1