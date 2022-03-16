processes=int(input("\nEnter number of processes: "))
memory=int(input("\nEnter total memory:"))
processes_arr=[]
for i in range(processes):
    user=int(input(f"Enter process {i+1} size:"))
    processes_arr.append(user)
assigned_processes=[]
for i in range(processes):
    if processes_arr[i]<=memory:
        memory-=processes_arr[i]
        # print("Size",process_arr[i],"\n\tinternal fragmentation=",size_of_block- process_arr[i])
        assigned_processes.append(processes_arr[i])
    else:
        print(f"\n Process{i+1} of",processes_arr[i],"kb allocated no space")
print("\tProcesses",assigned_processes)
print("\tExternal fragmentation:",memory)