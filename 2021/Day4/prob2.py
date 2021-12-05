file = open("input.txt","r")

inputs = file.readline().strip()
inputs = inputs.split(",")
print("Inputs\n",inputs)

bingos = []
bingo = None
counter = 0
for line in file.readlines():
    line = " ".join(line.split())
    if(line==""):
        if(bingo != None):
            bingos.append(bingo)
        bingo = []
    else:
        bingo.append(line.split())
bingos.append(bingo)
print("\nBingos")
for i in bingos:
    print(i)

def is_valid_bingo(bingo,inputs):
    valid = 0
    for row in range(len(bingo)):
        counter = 0
        for col in range(len(bingo[0])):
            if(bingo[row][col] in inputs):
                counter += 1
        if(counter == 5):
            return [1,"row",row,bingo]
    for col in range(len(bingo[0])):
        counter = 0
        for row in range(len(bingo)):
            if(bingo[row][col] in inputs):
                counter += 1
        if(counter == 5):
            return [1,"col",col,bingo]
    return 0

winning_bingos = []
for counter in range(len(inputs)):
    for bingo in bingos:
        if(bingo not in winning_bingos):
            valid = is_valid_bingo(bingo,inputs[0:counter])
            if(valid):
                winning_bingos.append(bingo)
                last_input = inputs[counter-1]
                current_bingo = valid[3]
                sum_bingo = 0
                for row in range(len(current_bingo)):
                    for col in range(len(current_bingo[0])):
                        if(current_bingo[row][col] not in inputs[0:counter]):
                            sum_bingo += int(current_bingo[row][col])
print("Sum: ",sum_bingo)
print("Last input: ",last_input)
print("final score: ",int(sum_bingo)*int(last_input))
            