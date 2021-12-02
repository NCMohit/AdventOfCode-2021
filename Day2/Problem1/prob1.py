commands = []
file = open("input.txt","r")
for line in file.readlines():
    commands.append(line.split())

horizontal = 0
depth = 0
for command in commands:
    if(command[0]=="forward"):
        horizontal += int(command[1])
    elif(command[0]=="down"):
        depth += int(command[1])
    else:
        depth -= int(command[1])

print(horizontal*depth)