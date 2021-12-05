points = []
file = open("input.txt","r")
for line in file.readlines():
    temp = line.strip().split("->")
    a = temp[0].strip().split(",")
    b = temp[1].strip().split(",")
    points.append([a,b])
print(points)
max_x = 0
max_y = 0
for point_pair in points:
    for point in point_pair:
        if(int(point[0]) > max_y):
            max_y = int(point[0])
        if(int(point[1]) > max_x):
            max_x = int(point[1])
matrix = []
for i in range(max_x+2):
    row = []
    for j in range(max_y+2):
        row.append(".")
    matrix.append(row)

max_val = 0

for point_pair in points:
    if(point_pair[0][0]==point_pair[1][0]):
        y = int(point_pair[0][0])
        x1 = int(point_pair[0][1])
        x2 = int(point_pair[1][1])
        if(x1 < x2):
            for x in range(x1,x2+1):
                if(matrix[x][y]=="."):
                    matrix[x][y]=1
                    if(matrix[x][y] > max_val):
                        max_val = matrix[x][y]
                else:
                    matrix[x][y]+=1
        else:
            for x in range(x2,x1+1):
                if(matrix[x][y]=="."):
                    matrix[x][y]=1
                else:
                    matrix[x][y]+=1
    elif(point_pair[0][1]==point_pair[1][1]):    
        x = int(point_pair[0][1])
        y1 = int(point_pair[0][0])
        y2 = int(point_pair[1][0])
        if(y1 < y2):
            for y in range(y1,y2+1):
                if(matrix[x][y]=="."):
                    matrix[x][y]=1
                else:
                    matrix[x][y]+=1
        else:
            for y in range(y2,y1+1):
                if(matrix[x][y]=="."):
                    matrix[x][y]=1
                else:
                    matrix[x][y]+=1
    elif(abs(int(point_pair[0][0])-int(point_pair[1][0])) == abs(int(point_pair[0][1])-int(point_pair[1][1]))):
        if(int(point_pair[1][1])<int(point_pair[0][1])):
            left_x = int(point_pair[1][1])
            left_y = int(point_pair[1][0])
            right_x = int(point_pair[0][1])
            right_y = int(point_pair[0][0])          
        else:
            left_x = int(point_pair[0][1])
            left_y = int(point_pair[0][0])
            right_x = int(point_pair[1][1])
            right_y = int(point_pair[1][0])
        if(left_y < right_y):         
            increase_y = 1
        else:
            increase_y = 0
        tempy = left_y
        tempx = left_x
        while(tempx<=right_x):
            if(matrix[tempx][tempy]=="."):
                matrix[tempx][tempy] = 1
            else:
                matrix[tempx][tempy] += 1
            tempx += 1
            if(increase_y):
                tempy+=1
            else:
                tempy-=1
        
counter = 0
for row in matrix:
    for col in row:
        print(col,end=" ")
        if(col=="."):
            pass
        else:
            if(col>=2):
                counter+=1
    print()
print("overlaps: ",counter)