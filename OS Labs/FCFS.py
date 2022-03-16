from operator import itemgetter
process=int(input("Enter total number of processes: "))
list1=[]# arrival time and burst time sorted by arrival time
list2=[]# all 5 calculations
sumAvgWT=0
sumAvgTT=0
for i in range(process):
    A_T=int(input("Enter arrival time for processes: "))
    B_T=int(input("Enter burst time for processes: "))
    list1.append([A_T,B_T])
list1 = sorted(list1, key=itemgetter(0))
for i in range(process):
    if i==0:
        C_T=list1[i][0]+list1[i][1]
    elif list2[i-1][2]>=list1[i][0]:
        C_T=list2[i-1][2]+list1[i][1]
    else:
        C_T=list1[i][0]+list1[i][1]
    T_T=C_T-list1[i][0]
    W_T=T_T-list1[i][1]
    list2.append([list1[i][0],list1[i][1],C_T,T_T,W_T])
throughput=process/(list2[len(list2)-1][2]-list2[0][0])
for i in range(len(list2)):
    sumAvgWT = sumAvgWT + list2[i][4]
    sumAvgTT = sumAvgTT + list2[i][3]
avgWT=sumAvgWT/process
avgTT=sumAvgTT/process
for i in range(process):
    print("\n\nProcess",i+1)
    print("Arrival Time:",list2[i][0])
    print("Burst Time:",list2[i][1])
    print("Completion Time:",list2[i][2])
    print("Turnaround Time:",list2[i][3])
    print("Waiting Time:",list2[i][4])
    print("--------------------------------------------------")
print("\nThroughput=",throughput)
print("\nAverage Waiting Time=",avgWT)
print("\nAverage Turnaround Time=",avgTT,"\n")

# for i in range(process):
#     for j in range(5):
#         print(list2[i][j])


# completion time must be greater than arrival time