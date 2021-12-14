string = ""
rules = []

file = open("input.txt","r")
for line in file.readlines():
    temp = line.strip().split("->")
    if(len(temp)!=2):
        if(temp!=[""]):
            string = temp[0]
    else:
        if(temp!=[""]):
            rules.append(temp)

count_dict = {}

step = 0
for step in range(10):
    counter = 0   
    while(counter < len(string)-1):
        # adding_possible = 0
        for rule in rules:
            if(rule[0][0]==string[counter]):
                if(rule[0][1]==string[counter+1]):
                    string = string[0:counter+1] + rule[1][1] + string[counter+1:]
                    counter +=2
                    # adding_possible = 1
                    break

for i in (list(set(string))):
    count_dict[i] = string.count(i)
a = list(count_dict.values())
a.sort()

print(a[-1]-a[0])