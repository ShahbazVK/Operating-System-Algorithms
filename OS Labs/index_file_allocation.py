import random
import math

size_of_partition=50
memory_blocks=30
memory_blocks_arr=[size_of_partition]*memory_blocks
processes=6
processes_arr=[145,140,295,500,405,500]
processes_arr_result=[-1]*processes
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

def indexFileAllocation(memory_blocks_arr):
    remaining_blocks_arr=[]
    remaining_partitions=len(memory_blocks_arr)-already_filled
    filled_array_blocks=[None]*memory_blocks
    for i in range(processes):
        current_process=processes_arr[i]

        if remaining_partitions>=math.ceil(current_process/size_of_partition):
            # print("here")
            indexFile=pickRandom(memory_blocks)
            while memory_blocks_arr[indexFile]==0:
                indexFile=pickRandom(memory_blocks)
            # print("indexfile",indexFile)
            memory_blocks_arr[indexFile]=0
            remaining_partitions-=1

            processes_arr_result[i]=indexFile
            # filled_array_blocks[indexFile]=[]
            temp_arr=[]
            while current_process>0 and remaining_partitions>=math.ceil(current_process/size_of_partition) and remaining_partitions>0:
                # print("run")
                index=pickRandom(memory_blocks)
                while memory_blocks_arr[index]==0:
                    index=pickRandom(memory_blocks)
                memory_blocks_arr[index]=0
                temp_arr.append(index)
                current_process-=size_of_partition
                remaining_partitions-=1
                # print(memory_blocks_arr)
                # print(temp_arr)
                # print(remaining_partitions,">=",math.ceil(current_process/size_of_partition))
                # print(processes_arr_result)
        filled_array_blocks[indexFile]=temp_arr
        # print(filled_array_blocks)
    for j in range(len(filled_array_blocks)):
        if filled_array_blocks[j]!=None:
            memory_blocks_arr[j]=filled_array_blocks[j]
    # print("\n",processes_arr_result)
    # print(memory_blocks_arr)

    for i in range(processes):
        print("File size",processes_arr[i],"kb")
        if processes_arr_result[i]!=-1:
            print("\tIndex file",processes_arr_result[i])
            print(f"\tAllocated blocks\n \t{memory_blocks_arr[processes_arr_result[i]]}")
        else:
            print("\tNO Space left to accomodate the file")
        print("\n\n")
        # processes_arr_result[i]
    print("Empty partitions:")
    for i in range(len(memory_blocks_arr)):
        if memory_blocks_arr[i]==size_of_partition:
            remaining_blocks_arr.append(i)
    if len(remaining_blocks_arr)>0:
        print(remaining_blocks_arr)
    else:
        print("No remaining partitions\n")

indexFileAllocation(list(memory_blocks_arr))