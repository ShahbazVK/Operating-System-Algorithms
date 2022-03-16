size_of_block=int(input("Size of single partition: "))
processes=int(input("Enter total processes: "))
memory_blocks=[size_of_block]*processes
process_arr=[]
for i in range(processes):
    user=int (input("enter process size: "))
    process_arr.append(user)
assigned_processes=[]
for i in range(processes):
    # print(i)
    if process_arr[i]<=size_of_block:
        print("Size",process_arr[i],"kb\n\tinternal fragmentation=",size_of_block- process_arr[i])
        assigned_processes.append(process_arr[i])
    else:
        print(process_arr[i],"allocated no space")