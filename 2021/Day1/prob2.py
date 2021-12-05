numbers = []
file = open("input.txt")
for line in file.readlines():
    numbers.append(int(line.strip()))

# numbers = [199,200,208,210,200,207,240,269,260,263]

answer = 0
counter = 1
while(counter<len(numbers)-2):
    current = numbers[counter]+numbers[counter+1]+numbers[counter+2]
    prev = numbers[counter-1]+numbers[counter]+numbers[counter+1]
    if(current>prev):
        answer+=1
    counter+=1
print(answer)