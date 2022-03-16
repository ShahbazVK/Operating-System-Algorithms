def firstFit(processes,processArr,partitionsArr):
    processResultArr=[0]*processes
    for i in range(processes):
    # processArr[i]=int(input(f"Enter size of process {i+1}: "))
        for j in range(len(partitionsArr)):
            # print("Empty Partitions:",partitionsArr)
            # print("All Processes:",processArr)
            if processArr[i]<=partitionsArr[j]:
                processResultArr[i]=partitionsArr[j]
                partitionsArr.pop(j)
                break
            else:
                processResultArr[i]="Not Allocated"
    showOutput(processes,processArr,processResultArr)
    # return processResultArr

def bestFit(processes,processArr,partitionsArr):
    partitionsArr.sort()
    print(partitionsArr)
    processResultArr=[0]*processes
    for i in range(processes):
    # processArr[i]=int(input(f"Enter size of process {i+1}: "))
        for j in range(len(partitionsArr)):
            # print("Empty Partitions:",partitionsArr)
            # print("All Processes:",processArr)
            if processArr[i]<=partitionsArr[j]:
                processResultArr[i]=partitionsArr[j]
                partitionsArr.pop(j)
                break
            else:
                processResultArr[i]="Not Allocated"
    showOutput(processes,processArr,processResultArr)
    # return processResultArr

def worstFit(processes,processArr,partitionsArr):
    partitionsArr.sort(reverse=True)
    print("partitionsArrpartitionsArrpartitionsArrpartitionsArrpartitionsArrpartitionsArrpartitionsArrpartitionsArrpartitionsArr",partitionsArr)
    processResultArr=[0]*processes
    for i in range(processes):
    # processArr[i]=int(input(f"Enter size of process {i+1}: "))
        for j in range(len(partitionsArr)):
            # print("Empty Partitions:",partitionsArr)
            # print("All Processes:",processArr)
            if processArr[i]<=partitionsArr[j]:
                processResultArr[i]=partitionsArr[j]
                partitionsArr.pop(j)
                break
            else:
                processResultArr[i]="Not Allocated"
    showOutput(processes,processArr,processResultArr)
    # return processResultArr

def showOutput(processes,processArr,processResultArr):
    for i in range(processes):
        print(f"Process {i+1} of {processArr[i]}Kb allocated {processResultArr[i]} kb space")

memory_partitions=int(input("Enter total number of memory partitions: "))
# partioning=input("F: fixed partioning\nD: dynamic partioning:")
# if partioning=="F":
#     size_of_partition=int(input("Enter size of partition: "))
#     partitionsArr=[size_of_partition]*memory_partitions
# processes=int(input("Enter number of processes: "))
# for i in range(processes):
#     # size_of_process=int(input("Enter size of process: "))
#     length_of_process=int(input("Enter length of process: "))
#     start=int(input("Enter starting position: "))

# print(partitionsArr)
partitionsArr=[0]*memory_partitions
for i in range(memory_partitions):
    partitionsArr[i]=int(input(f"Enter size of partition {i+1}: "))
print(f"Partitions {partitionsArr}\n\n\n")
processes=memory_partitions+1
while processes>memory_partitions:
    processes=int(input(f"Enter number of processes(must be less than or equal to number of partitions i.e {memory_partitions}): "))
processArr=[0]*processes
# processResultArr=[0]*processes

for i in range(processes):
    processArr[i]=int(input(f"Enter size of process {i+1}: "))

print(firstFit(processes,processArr,partitionsArr))
# print(bestFit(processes,processArr,partitionsArr))
# print(worstFit(processes,processArr,partitionsArr))

# for i in range(processes):
#     # processArr[i]=int(input(f"Enter size of process {i+1}: "))
#     for j in range(len(partitionsArr)):
#         # print("Empty Partitions:",partitionsArr)
#         # print("All Processes:",processArr)
#         if processArr[i]<=partitionsArr[j]:
#             processResultArr[i]=partitionsArr[j]
#             partitionsArr.pop(j)
#             break
#         else:
#             processResultArr[i]="Not Allocated"

print("Empty Partitions:",partitionsArr)
print("All Processes:",processArr)
