matrix = []
file = open("input.txt","r")
for line in file.readlines():
    row = []
    for i in line.strip():
        row.append(int(i))
    matrix.append(row)

tempflashes = 0
step = 1
while(tempflashes != 100):
    tempflashes = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] += 1
    flashed_points = []
    noflashes = 0
    while(noflashes == 0):
        noflashes = 1
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if([row,col] not in flashed_points):
                    if(matrix[row][col]>=10):
                        noflashes = 0
                        flashed_points.append([row,col])
                        if(row == 0):
                            if(col == 0):
                                matrix[row+1][col] += 1
                                matrix[row][col+1] += 1
                                matrix[row+1][col+1] += 1
                            elif(col == (len(matrix[0])-1)):
                                matrix[row+1][col-1] += 1
                                matrix[row+1][col] += 1
                                matrix[row][col-1] += 1
                            else:
                                matrix[row+1][col] += 1
                                matrix[row][col-1] += 1
                                matrix[row+1][col-1] += 1
                                matrix[row][col+1] += 1
                                matrix[row+1][col+1] += 1
                        elif(row == (len(matrix)-1)):
                            if(col == 0):
                                matrix[row-1][col] += 1
                                matrix[row][col+1] += 1
                                matrix[row-1][col+1] += 1
                            elif(col == (len(matrix[0])-1)):
                                matrix[row-1][col-1] += 1
                                matrix[row-1][col] += 1
                                matrix[row][col-1] += 1
                            else:
                                matrix[row-1][col] += 1
                                matrix[row][col-1] += 1
                                matrix[row-1][col-1] += 1
                                matrix[row][col+1] += 1
                                matrix[row-1][col+1] += 1
                        else:
                            if(col == 0):
                                matrix[row-1][col] += 1
                                matrix[row][col+1] += 1
                                matrix[row-1][col+1] += 1
                                matrix[row+1][col+1] += 1
                                matrix[row+1][col] += 1
                            elif(col == (len(matrix[0])-1)):
                                matrix[row-1][col-1] += 1
                                matrix[row-1][col] += 1
                                matrix[row][col-1] += 1
                                matrix[row+1][col-1] += 1
                                matrix[row+1][col] += 1
                            else:
                                matrix[row-1][col] += 1
                                matrix[row][col-1] += 1
                                matrix[row-1][col-1] += 1
                                matrix[row][col+1] += 1
                                matrix[row-1][col+1] += 1  
                                matrix[row+1][col] += 1
                                matrix[row+1][col-1] += 1 
                                matrix[row+1][col+1] += 1
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if(matrix[row][col]>=10):
                matrix[row][col] = 0
                tempflashes += 1
    if(tempflashes == 100):
        print("Step: ",step)
    step += 1