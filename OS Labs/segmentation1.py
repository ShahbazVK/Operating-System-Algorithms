from numpy import append


process_segments = [[0,300],[1,50],[2,500],[3,100],[4,100]]#[no,size]
memory_size = 2550
memory = [
[0,'OS'], [1500,'free'], [1800,'free'],#[address,status]
[2300,'free'], [2400,'free'], [2500,'free']
]
print(f"\nProcess Segments: {process_segments}\n")
print(f"Memory Size: {memory_size}\n")
print(f"Memory: {memory}\n")
segment_table = []
for i in range(len(process_segments)):
    for j in range(len(memory)):
        if(memory[j][1]=='free'):
            if j==len(memory)-1:
                space=memory_size-memory[j][0]
            else:
                space=memory[j+1][0]-memory[j][0]
            if(space==process_segments[i][1]):
                memory[j][1] = f"S{process_segments[i][0]}"
                segment_table.append([i,process_segments[i][1], memory[j][0]])
                break
print("Process stored in memory NOW !\n")
print(f"\tMemory: {memory}")
print(f"\tSegment Table: {segment_table}")
requested_segment = int(input('From which segment you want to read byte? '))
requested_byte = int(input(f"Which byte of segment:{requested_segment} you want to read? "))
print(f"\tRequested Segment: {requested_segment}")
print(f"\tRequested Byte of Requested Segment: {requested_byte}")
segment_no = int(format(requested_segment, "b"))
segment_offset = int(format(requested_byte, "b"))
logical_address = segment_no, segment_offset
print(f"\tSegment No: {segment_no}")
print(f"\tSegment Offset: {segment_offset}")
print(f"\tLogical Address: {logical_address}")
# entry = segment_table.find(object => object.segment_no == int(segment_no, 2))

for i in range(len(segment_table)):
    # print(segment_no)
    if segment_table[i][0]==int(str(segment_no), 2):
        entry=segment_table[i]

print(f"Concerned Entry of Segment Table: {entry}")
if (entry[1]<int(str(segment_offset),2)):
    print('Invalid address!')

physical_address = format((entry[2] + int(str(segment_offset),2)),"b")
loc = int(physical_address,2)
print(f"\tPhysical Address: {physical_address}")
print(f"\tLocation in Memory: {loc}")