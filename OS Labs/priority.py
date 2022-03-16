from operator import itemgetter
processes=int(input("Enter number of processes: "))
priorityOrder=int(input("Enter priority order\n1: Lowest to Highest\n0: Highest to Lowest: "))
# processes=6
list1=[]
avgTT=0
avgWT=0
for i in range(processes):
    print("------------------------------PROCESS",i+1,"--------------------------------------")
    AT=int(input(f"Enter arrival time for process {i+1}: "))
    BT=int(input(f"Enter burst time for process {i+1}: "))
    Priority=int(input(f"Enter priority for process {i+1}: "))
    list1.append([AT,BT,Priority])
# list1=[[65,43],[888,11],[3,4]]
readyQueue=[]
list2=[]

list1 = sorted(list1, key=itemgetter(0))
totalCompletionTime=list1[0][0]
# print(list1)
covered=0
while len(readyQueue)!=0 or len(list1)>0:
    while len(list1)!=0:
        if list1[0][0]<=totalCompletionTime:
            readyQueue.append(list1[0])
            list1.pop(0)
            covered+=1
        else: 
            if len(readyQueue)==0:
                readyQueue.append(list1[0])
                list1.pop(0)
                covered+=1
                totalCompletionTime+=readyQueue[0][0]-totalCompletionTime
                # print("list1",list1)
                # print("readyQueue",readyQueue)
                # print("LIST2",list2)

                if len(list1)!=0 and list1[0][0]==totalCompletionTime:
                    continue
            break
        # print("COVERED",covered)

    readyQueue=sorted(readyQueue, key=itemgetter(2))
    if priorityOrder==0:
        print(readyQueue)
        readyQueue=readyQueue[::-1]
        # readyQueue= list(reversed(readyQueue))
        print(readyQueue)

    totalCompletionTime+=readyQueue[0][1]
    # print(totalCompletionTime)
    readyQueue[0].append(totalCompletionTime)
    readyQueue[0].append(readyQueue[0][3]-readyQueue[0][0])
    readyQueue[0].append(readyQueue[0][4]-readyQueue[0][1])

    list2.append(readyQueue[0])
    readyQueue.pop(0)
    
for i in range(processes):
    avgTT+=list2[i][4]
    avgWT+=list2[i][5]
avgTT/=processes
avgWT/=processes
throughput=processes/(list2[processes-1][3]-list2[0][0])

# print(list1,readyQueue,list2,avgTT,avgWT,throughput)
print("\n\n\n")
print("\tProcess\t","Arrival Time\t","Burst Time\t","Completion Time\t","Turnaround Time\t","Waiting Time\t","       Priority\t")
for i in range(processes):
    print("\t",i+1,"\t      ",list2[i][0],"\t     ",list2[i][1],"\t\t",list2[i][3],"\t\t\t",list2[i][4],"\t\t    ",list2[i][5],"\t\t          ",list2[i][2],"\t\t    ")
print("\n")
print("Average Waiting Time:",avgWT)
print("Average Turnaround Time:",avgTT)
print("Throughput:",throughput)