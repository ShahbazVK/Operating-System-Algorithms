from operator import itemgetter
processes=int(input("Enter Number Of Processes: "))
timeSlice=int(input("Enter Quantum Time: "))
list1=[]
# processes=4
# timeSlice=2
# list1=[

# [5,[1,1,0],0],
# [6,[1,1,0],0],
# [7,[1,1,0],0],
# [18,[1,1,0],0],

# ]
for i in range(processes):
    AT=int(input(f"Enter Arrival Time for process {i+1}: "))
    BT=int(input(f"Enter Burst Time for process {i+1}: "))
    list1.append([AT,[BT]])
    while timeSlice<=BT:
        list1[i][1].append(timeSlice)
        BT-=timeSlice
    if BT!=0:
        list1[i][1].append(BT)

    list1[i][1].append(0)# for checking
    list1[i].append(0)#completion time

# print(list1)
# list1=[

# [0,[4,2,2,0],0],
# [1,[5,2,2,1,0],0],
# [2,[2,2,0],0],
# [3,[1,1,0],0],
# [4,[6,2,2,2,0],0],
# [6,[3,2,1,0],0]

# ]
list1 = sorted(list1, key=itemgetter(0))
spareTime=list1[0][0]
readyQueue=[0]
totalCompletionTime=spareTime
coveredProcesses=1
i=0
while i<len(readyQueue):
    # print("I=",i)

    newProcesses=0

    if i==0:
        list1[readyQueue[i]][2]=spareTime
    # print("COVERED",coveredProcesses)
    # print("READY",readyQueue)
    # print("list1",list1)
    totalCompletionTime+=list1[readyQueue[i]][1][1]
    # print(totalCompletionTime)
    if coveredProcesses!=processes:
        for j in range(processes-coveredProcesses):
            if totalCompletionTime>=list1[j+coveredProcesses][0]:
                readyQueue.append(j+coveredProcesses)
                newProcesses+=1
            else:
                break
        coveredProcesses+=newProcesses
        # print("COVERED",coveredProcesses)
        
    list1[readyQueue[i]][2]=totalCompletionTime #+ list1[readyQueue[i]][1][1]
    list1[readyQueue[i]][1].pop(1)
    # print("LIST",list1)
    if list1[readyQueue[i]][1][1]!=0:
        readyQueue.append(readyQueue[i])
    # print(len(readyQueue),"==",i+1)
    else:
        if (len(readyQueue)==i+1) and processes!=coveredProcesses:
            # print("YES")
            readyQueue.append(coveredProcesses)
            coveredProcesses+=1
            totalCompletionTime+=list1[readyQueue[i+1]][0]-totalCompletionTime
            list1[readyQueue[i+1]][2]=totalCompletionTime #+ list1[readyQueue[i]][1][1]

    # print("\n\n\nLAST",readyQueue)
    # print("LAST",list1)
  
    i+=1
for i in range(processes):
    # print(list1[i][2])
    # print(list1[i][0])
    # print(list1[i][1])
    list1[i].append(list1[i][2] - list1[i][0])
    list1[i].append(list1[i][3] - list1[i][1][0])

# print("\n\n",list1)
avgTT=0
avgWT=0
print("\tProcess\t","Arrival Time\t","Burst Time\t","Completion Time\t","Turnaround Time\t","Waiting Time\t")
for i in range(processes):
    print("\t",i+1,"\t      ",list1[i][0],"\t     ",list1[i][1][0],"\t\t",list1[i][2],"\t\t\t",list1[i][3],"\t\t    ",list1[i][4])
    avgTT+=list1[i][3]
    avgWT+=list1[i][4]
print("Average Turnaround Time:",avgTT/processes)
print("Average Waiting Time:",avgWT/processes)
