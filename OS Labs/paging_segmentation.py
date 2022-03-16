import math

process_size = int(input('\nEnter process size: '))
page_size = 2
no_of_pages = process_size // page_size
print(f"\tProcess Size: {process_size}")
print(f"\tPage Size: {page_size}")
print(f"\tNo of Pages: {no_of_pages}")
memory_size = 16
frame_size = page_size
no_of_frames = memory_size / frame_size
memory = [
['occupied','occupied'],['occupied','occupied'],['free','free'],['occupied','occupied'],
['free','free'],['free','free'],['free','free'],['free','free']
]
print(f"\tMemory Size: {memory_size}")
print(f"\tFrame Size: {frame_size}")
print(f"\tNo of Frames: {no_of_frames}")
# print(f"Memory: {memory}")
page_table = []
temp=0
for i in range(no_of_pages):
    tempArr=[]
    for j in range(len(memory)):
        if(memory[j][0]=='free'):
            for l in range(page_size):
                tempArr.append(temp)
                temp+=1
            page_table.append([tempArr,j])
            for k in range(page_size):
                memory[j][k] = 'P1'
        
            break
print(f"Process stored in memory now")
# print(f"Memory: {memory}")
# print(f"Page Table: {page_table}")
requested_byte = int(input('Which byte of process A you want to read? '))
logical_address = format(requested_byte, "b")
print(f"\tRequested Byte: {requested_byte}")
print(f"\tLogical Address: {logical_address}")
page_offset = logical_address[1]
# print(f"No of Page Offset Bits: {page_offset_bits}")
# print(f"Page No: {page_no}")
print(f"\tPage Offset: {page_offset}")
for i in range(len(page_table)):
    for j in range(page_size):
        if page_table[i][0][j]==requested_byte:
            frame_no=page_table[i][1]
            print("\tFRAME Number:",frame_no)
            frame_no=format(frame_no,"b")
frame_offset = page_offset
# print(f"Frame No: {frame_no}")
print(f"\tFrame Offset: {frame_offset}")
print(f"\tPhysical Address is: {frame_no}|{frame_offset}")