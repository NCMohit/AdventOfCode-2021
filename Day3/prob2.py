bins = []
file = open("input.txt","r")

for line in file.readlines():
    bins.append(line.strip())

def o2(bins):
    current_index = 0
    while(len(bins)!=1):
        zeroes = 0
        retain = ""
        for row in range(len(bins)):
            if(bins[row][current_index]=="0"):
                zeroes += 1
        if(zeroes > int(len(bins)/2)):
            retain = "0"
        else:
            retain = "1"
        tempbins = bins.copy()
        for num in bins:
            if(num[current_index]!=retain):
                tempbins.remove(num)
        bins = tempbins
        current_index += 1

    return int(bins[0],2)

def co2(bins):
    current_index = 0
    while(len(bins)!=1):
        zeroes = 0
        retain = ""
        for row in range(len(bins)):
            if(bins[row][current_index]=="0"):
                zeroes += 1
        if(zeroes > int(len(bins)/2)):
            retain = "1"
        else:
            retain = "0"
        tempbins = bins.copy()
        for num in bins:
            if(num[current_index]!=retain):
                tempbins.remove(num)
        bins = tempbins
        current_index += 1
    return int(bins[0],2)

print("O2: ",o2(bins))
print("CO2: ",co2(bins))
print("Life Support: ",o2(bins)*co2(bins))