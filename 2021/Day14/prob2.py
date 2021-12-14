string = ""
rules = []
couple_dict = {}
single_dict =  {}

file = open("input.txt","r")
for line in file.readlines():
    temp = line.strip().split("->")
    if(len(temp)!=2):
        if(temp!=[""]):
            string = temp[0]
    else:
        if(temp!=[""]):
            rules.append(temp)

for count in range(len(string)-1):
    if(string[count:count+2] not in couple_dict.keys()):
        couple_dict[string[count:count+2]] = 1
    else:
        couple_dict[string[count:count+2]] += 1
    if(string[count] not in single_dict.keys()):
        single_dict[string[count]] = 1
    else:
        single_dict[string[count]] += 1
if(string[-1] not in single_dict.keys()):
    single_dict[string[-1]] = 1
else:
    single_dict[string[-1]] += 1


for step in range(40):
    adding_couples = {}
    adding_singles = {}
    for pairs in couple_dict.keys():
        if(couple_dict[pairs] > 0):
            for rule in rules:
                l = rule[0][0]
                r = rule[0][1]
                s = rule[1][1]
                if(l+r == pairs):
                    if(couple_dict[l+r] != 0):
                        if(l+s in adding_couples.keys()):
                            adding_couples[l+s] += couple_dict[l+r]
                        else:
                            adding_couples[l+s] = couple_dict[l+r]
                        if(s+r in adding_couples.keys()):
                            adding_couples[s+r] += couple_dict[l+r]
                        else:
                            adding_couples[s+r] = couple_dict[l+r]
                        if(l+r in adding_couples.keys()):
                            adding_couples[l+r] -= couple_dict[l+r]
                        else:
                            adding_couples[l+r] = -(couple_dict[l+r])

                        if(s in adding_singles.keys()):
                            adding_singles[s] += couple_dict[l+r]
                        else:
                            adding_singles[s] = couple_dict[l+r]                                                  
    for key,value in adding_couples.items():
        if(key in couple_dict.keys()):
            couple_dict[key] += adding_couples[key]
        else:
            couple_dict[key] = adding_couples[key]
    for key,value in adding_singles.items():
        if(key in single_dict.keys()):
            single_dict[key] += adding_singles[key]
        else:
            single_dict[key] = adding_singles[key]

a = list(single_dict.values())
a.sort()
print(a[-1]-a[0])