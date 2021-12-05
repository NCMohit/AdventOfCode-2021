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
    count = 0
    if(word[mins-1]==char):
        count+=1
    if(word[maxs-1]==char):
        count+=1
    if(count==1):
        valids +=1
print(valids)