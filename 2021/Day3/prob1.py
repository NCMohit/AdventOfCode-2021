bins = []
file = open("input.txt","r")

for line in file.readlines():
    bins.append(line.strip())

gamma = ""
for col in range(len(bins[0])):
    zeroes = 0
    for row in range(len(bins)):
        if(bins[row][col]=="0"):
            zeroes += 1
    if(zeroes > (len(bins)/2)):
        gamma += "0"
    else:
        gamma += "1"

epsilon = ""
for i in gamma:
    if(i=="1"):
        epsilon+="0"
    else:
        epsilon+="1"

print("Gamma: ",int(gamma,2))
print("Epsilon: ",int(epsilon,2))

print("Power: ",int(gamma,2)*int(epsilon,2))