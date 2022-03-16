import sys
import random
import math

size_of_partition=50
# print("Size of single partition:",size_of_partition,"\n")
memory_blocks=30
memory_blocks_arr=[size_of_partition]*memory_blocks
processes=6
processes_arr=[145,140,295,500,405,500]
processes_arr_result=[0]*processes
#We are assuming that some spaces are pre-occupied. Assume that index (3), (8), (13), (23) are pre-occupied
memory_blocks_arr[3]=0
memory_blocks_arr[8]=0
memory_blocks_arr[13]=0
memory_blocks_arr[23]=0
already_filled=4

print("\n\nSize of single partition:",size_of_partition)
print("Total blocks",memory_blocks)
print("Following blocks are already filled",[3,8,13,23])
print("Total processes",processes)
print("\n\n")

def pickRandom(memory_blocks):
    return random.randrange(0,memory_blocks)

def link_file_allocation(processes_arr,memory_blocks_arr,already_filled):
    filled_blocks_arr=[0]*len(memory_blocks_arr)
    remaining_partitions=memory_blocks-already_filled
    for i in range(processes):
        # print("PROCESS",processes_arr[i],"kb")
        current_process=processes_arr[i]
        random_partition=pickRandom(memory_blocks)
        isFirstPartition=True
        # print( math.ceil(current_process/size_of_partition),"<=",remaining_partitions)
        while current_process>0 and remaining_partitions>0 and math.ceil(current_process/size_of_partition)<=remaining_partitions:

            while memory_blocks_arr[random_partition]==0:
                random_partition=pickRandom(memory_blocks)

            if isFirstPartition:
                processes_arr_result[i]=random_partition
                # print("IF")
            else:
                # print("ELSE")
                filled_blocks_arr[prev]=random_partition
                # print(prev,random_partition)

            # print(random_partition,end=" ")
            current_process-=size_of_partition
            isFirstPartition=False
            prev=random_partition
            memory_blocks_arr[random_partition]=0
            remaining_partitions-=1
            # print("current_process",current_process)
            # print("remaining_partitions",remaining_partitions)
            # print( math.ceil(current_process/size_of_partition),"<=",remaining_partitions)
        
        # memory_blocks_arr[random_partition]=0
        if current_process<=0:
            filled_blocks_arr[random_partition]=-1
        else:
            processes_arr_result[i]=-1
        # print("\nprocesses_arr_result",processes_arr_result)
        # print("filled_blocks_arr",filled_blocks_arr)
        # print("memory_blocks_arr",memory_blocks_arr)
        # print("END\n")
        
    fetching_processes(list(processes_arr),list(processes_arr_result),list(filled_blocks_arr),list(memory_blocks_arr))


def fetching_processes(processes_arr, processes_arr_result,filled_blocks_arr,memory_blocks_arr):
    remaining_blocks_arr=[]
    for i in range(len(processes_arr_result)):
        print(f"Process P{i+1}")
        print(f"\tSize: {processes_arr[i]} kb")
        if processes_arr_result[i]!=-1:
            print("\tProcess allocated in the following partitions: ")
        else:
            print("NO Space Left to Accomodate")
        index=processes_arr_result[i]
        print("\t",end="")
        while index!=-1:
            print(index, end="")
            index=filled_blocks_arr[index]
            if index!=-1:
                
                print(", ",end="")
        print("\n")
    print("Empty partitions:")
    for i in range(len(memory_blocks_arr)):
        if memory_blocks_arr[i]==size_of_partition:
            remaining_blocks_arr.append(i)
    if len(remaining_blocks_arr)>0:
        print(remaining_blocks_arr)
    else:
        print("No remaining partitions\n")
link_file_allocation(list(processes_arr),list(memory_blocks_arr),already_filled)