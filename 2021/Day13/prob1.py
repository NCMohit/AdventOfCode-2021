matrix = []
points = []
folds= []
max_x = -1
max_y = -1

file = open("input.txt","r")
for line in file.readlines():
    temp = line.strip().split(",")
    if(len(temp)==2):
        points.append([int(temp[0]),int(temp[1])])
        if(max_x < int(temp[0])):
            max_x = int(temp[0])
        if(max_y < int(temp[1])):
            max_y = int(temp[1])
    elif(temp != [""]):
        temp2 = temp[0].replace("fold along ","").split("=")
        folds.append(temp2)
for r in range(max_y+1):
    row = []
    for c in range(max_x+1):
        row.append(".")
    matrix.append(row)

for point in points:
    matrix[point[1]][point[0]] = "#"

def yfold(matrix,y):
    max_y = len(matrix)-1
    max_x = len(matrix[0])-1
    for y_curr in range(1,(max_y-y)+1):
        for x_curr in range(max_x+1):
            if(matrix[y+y_curr][x_curr]=="#"):
                matrix[y-y_curr][x_curr] = matrix[y+y_curr][x_curr]
    matrix = matrix[:y]
    count = 0
    for l in matrix:
        for j in l:
            if(j=="#"):
                count+=1
    print(count)
    return matrix    

def xfold(matrix,x):
    max_y = len(matrix)-1
    max_x = len(matrix[0])-1
    for x_curr in range(1,(max_x-x)+1):
        for y_curr in range(max_y+1):
            if(matrix[y_curr][x+x_curr]=="#"):
                matrix[y_curr][x-x_curr] = matrix[y_curr][x+x_curr]
    tempmatrix = []
    count = 0
    for l in matrix:
        for j in l[:x]:
            if(j=="#"):
                count+=1
        tempmatrix.append(l[:x])
    print(count)
    return matrix

for fold in folds:
    if(fold[0]=="y"):
        y = int(fold[1])
        matrix = yfold(matrix,y)
        break
    elif(fold[0]=="x"):
        x = int(fold[1])
        matrix = xfold(matrix,x)
        break