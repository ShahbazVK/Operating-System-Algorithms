import sys

size_of_partition=50
memory_blocks=30
memory_blocks_arr=[size_of_partition]*memory_blocks
processes=6
processes_arr=[145,140,295,500,355,456]
processes_arr_result=[0]*processes
#We are assuming that some spaces are pre-occupied. Assume that index (3), (8), (13), (23) are pre-occupied
memory_blocks_arr[3]=0
memory_blocks_arr[8]=0
memory_blocks_arr[13]=0
memory_blocks_arr[23]=0
# print(memory_blocks_arr[19],"heeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee")

def firstFit(memory_blocks_arr,processes_arr):
    print("\n-------------------------------------------------------------FIRST FIT ALGORITHM-------------------------------------------------\n")
    for i in range(processes):
        sum=0
        temp_arr=[]
        # print("i",i)
        # while processes_arr[i][1]!=0:
        for j in range(memory_blocks):
            # print("j",j)
            sum+=memory_blocks_arr[j]
            temp_arr.append(j)
            if sum>=processes_arr[i]:
                processes_arr_result[i]=[f"{processes_arr[i]} kb", temp_arr]
                for k in range(len(temp_arr)):
                    memory_blocks_arr[temp_arr[k]]=0
                break
            elif memory_blocks_arr[j]==0:
                sum=0
                temp_arr=[]
                # processes_arr_result[i]="No Space"
            processes_arr_result[i]=f"{processes_arr[i]}kb. No Space"
    return processes_arr_result


def bestFit(memory_blocks_arr,processes_arr):
    print("\n-------------------------------------------------------------BEST FIT ALGORITHM-------------------------------------------------\n")
    new_arr=[0]*len(processes_arr)
    for i in range(processes):
        current_process=processes_arr[i]
        final_arr=[]
        sum=0
        minimum=sys.maxsize
        temp_arr=[]
        real_temp_arr=[]
        for j in range(memory_blocks):
            if memory_blocks_arr[j]==0 or j==len(memory_blocks_arr)-1:
                if j==len(memory_blocks_arr)-1:
                    # print("WORKING")
                    sum+=memory_blocks_arr[j]
                    temp_arr.append(j)
                if sum<minimum and sum>=processes_arr[i]:
                    minimum=sum
                    real_temp_arr=temp_arr
                    # print(real_temp_arr,"working")
                    sum=0
                    temp_arr=[]
                sum=0
                temp_arr=[]

            elif memory_blocks_arr[j]!=0: 
                sum+=memory_blocks_arr[j]
                temp_arr.append(j)
            # print(sum,j)
        new_arr[i]=real_temp_arr


        if len(real_temp_arr)!=0:
            x=0
            while current_process>0:
                # print(real_temp_arr)
                memory_blocks_arr[real_temp_arr[x]]=0
                # print("x= ",x)
                # print("current_process",current_process)
                # print(memory_blocks_arr)
                final_arr.append(real_temp_arr[x])
                processes_arr_result[i]=[f"{processes_arr[i]} kb",final_arr]
                x+=1
                current_process-=size_of_partition
        else:
            processes_arr_result[i]=f"{processes_arr[i]}kb. No Space"

        # print(processes_arr_result)
        # print(memory_blocks_arr)
        # print("END")

    # return new_arr
    return processes_arr_result


def worstFit(memory_blocks_arr,processes_arr):
    print("\n-------------------------------------------------------------WORST FIT ALGORITHM-------------------------------------------------\n")
    new_arr=[0]*len(processes_arr)
    for i in range(processes):
        current_process=processes_arr[i]
        final_arr=[]
        sum=0
        max=current_process
        temp_arr=[]
        real_temp_arr=[]
        for j in range(memory_blocks):
            # print(sum,j)
            if memory_blocks_arr[j]==0 or j==len(memory_blocks_arr)-1:
                if j==len(memory_blocks_arr)-1:
                    sum+=memory_blocks_arr[j]
                    temp_arr.append(j)
                if sum>max:
                    max=sum
                    real_temp_arr=temp_arr
                    # print(real_temp_arr)
                    sum=0
                    temp_arr=[]
                sum=0
                temp_arr=[]

            elif memory_blocks_arr[j]!=0: 
                sum+=memory_blocks_arr[j]
                temp_arr.append(j)
        new_arr[i]=real_temp_arr

        # print("real_temp_arrreal_temp_arrreal_temp_arrreal_temp_arr",real_temp_arr)
        if len(real_temp_arr)!=0:
            x=0
            while current_process>0:
                # print(real_temp_arr)
                # print(real_temp_arr)
                memory_blocks_arr[real_temp_arr[x]]=0
                # print("x= ",x)
                # print("current_process",current_process)
                # print(memory_blocks_arr)
                final_arr.append(real_temp_arr[x])
                processes_arr_result[i]=[f"{processes_arr[i]} kb",final_arr]

                x+=1
                current_process-=size_of_partition
        else:
            processes_arr_result[i]=f"{processes_arr[i]}kb. No Space"


        # print(processes_arr_result)
        # print("END")

    # return new_arr
    return processes_arr_result


print(firstFit(list(memory_blocks_arr),processes_arr))
print(bestFit(list(memory_blocks_arr),processes_arr))
print(worstFit(list(memory_blocks_arr),processes_arr))
print("\n")