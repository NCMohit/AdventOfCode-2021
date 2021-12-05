pwds = []
file = open("input.txt","r")
for line in file.readlines():
    pwds.append(line.strip().split(" "))
print(pwds)
valids = 0
for pwd in pwds:
    mins = int(pwd[0].split("-")[0])
    maxs = int(pwd[0].split("-")[1])
    char = pwd[1][0]
    word = pwd[2]
    count = word.count(char)
    if((count>=mins) &(count<=maxs)):
        valids += 1
print(valids)