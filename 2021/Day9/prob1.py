matrix = []
file = open("input.txt","r")
for line in file.readlines():
    row = []
    for num in line.strip():
        row.append(int(num))
    matrix.append(row)

def is_low_point(row,col,matrix):
    max_row = len(matrix)-1
    max_col = len(matrix[0]) -1
    is_low = 1
    #left
    if(col != 0):
        if(matrix[row][col-1] <= matrix[row][col]):
            is_low = 0
    #right
    if(col != max_col):
        if(matrix[row][col+1] <= matrix[row][col]):
            is_low = 0
    # top
    if(row != 0):
        if(matrix[row-1][col] <= matrix[row][col]):
            is_low = 0
    # bottom
    if(row != max_row):
        if(matrix[row+1][col] <= matrix[row][col]):
            is_low = 0 
    return is_low
        
ans = []
for row in range(len(matrix)):
    for col in range(len(matrix[0])):
        if(is_low_point(row,col,matrix)):
        # print(is_low_point(row,col,matrix),end=" ")
            ans.append(matrix[row][col]+1)
    # print()
print(ans)
final_ans = 0
for i in ans:
    final_ans += i
print(final_ans)