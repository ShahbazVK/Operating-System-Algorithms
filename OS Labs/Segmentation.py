
memory = [
{'Name':'OS', 'Base Address': 1000,'Size': 500},
{'Name':'S1', 'Base Address': 1500,'Size': 300},
{'Name':'S3', 'Base Address': 1800,'Size': 500},
{'Name':'S5', 'Base Address': 2300,'Size': 100},
{'Name':'S7', 'Base Address': 2400,'Size': 300},
{'Name':'S4', 'Base Address': 2700,'Size': 400},
{'Name':'S2', 'Base Address': 3100,'Size': 800},
]
print("Enter Base Address and reading size (For example: 1500 400 or 230050)\nInput:",end=" ")
inputs = input() ; inputs = inputs.split(" ")
for i in range(len(inputs)):
    inputs[i]=int(inputs[i])
for m in memory:
    if inputs[0] == m['Base Address']:
        print(m['Name'],"at address",m['Base Address'],"of size",m['Size'],end=".\n")
        print("\nChecking for offset...\n")
        if inputs[1] <= m['Size']:
            print(m['Name'],"successfully read.")
        else:
            print("ERROR 404: OFFSET NOT FOUND.\nThe given offset %d is greater thanthe size of the segment i.e. %d." % (inputs[1],m['Size']))