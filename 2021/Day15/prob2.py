import math, sys
matrix = []

file = open("input.txt","r")
for line in file.readlines():
    row = []
    temp = line.strip()
    for i in temp:
        row.append(int(i))
    matrix.append(row)

beeg_matrix = []
for row in matrix:
    temprow = row.copy()
    for temp in range(1,5):
        for j in row:
            if(j+temp > 9):
                temprow.append((j+temp)%9)
            else:
                temprow.append(j+temp)
    beeg_matrix.append(temprow)
matrix = beeg_matrix.copy()
for temp in range(1,5):
    for row in beeg_matrix:
        temprow = []
        for j in row:
            if(j+temp > 9):
                temprow.append((j+temp)%9)
            else:
                temprow.append(j+temp)
        matrix.append(temprow)

for i in matrix:
    for j in i:
        print(j,end="")
    print()

print()

node_cost = {(0,0):0}
visited = []
visited_temp = [[0,0]]

# Got filtered Sadge, had to learn Dijkstra's algorithm
# Only works on example

next_chosen_node = None
next_chosen_node_cost = math.inf

while(len(visited_temp) != 0 ):
    chosen_node = next_chosen_node
    chosen_node_cost = next_chosen_node_cost
    for node in visited_temp:
        if(node_cost[(node[0],node[1])]<chosen_node_cost):
            chosen_node = node
            chosen_node_cost = node_cost[(node[0],node[1])]
    visited.append(chosen_node)
    visited_temp.remove(chosen_node)
    neighbors = []
    if(chosen_node[0] != 0):
        if([chosen_node[0]-1,chosen_node[1]] not in visited+visited_temp):
            visited_temp.append([chosen_node[0]-1,chosen_node[1]])
            neighbors.append([chosen_node[0]-1,chosen_node[1]])
    if(chosen_node[0] != (len(matrix)-1) ):
        if([chosen_node[0]+1,chosen_node[1]] not in visited+visited_temp):
            visited_temp.append([chosen_node[0]+1,chosen_node[1]])
            neighbors.append([chosen_node[0]+1,chosen_node[1]])
    if(chosen_node[1] != 0):
        if([chosen_node[0],chosen_node[1]-1] not in visited+visited_temp):
            visited_temp.append([chosen_node[0],chosen_node[1]-1])
            neighbors.append([chosen_node[0],chosen_node[1]-1])
    if(chosen_node[1] != (len(matrix[0])-1) ):
        if([chosen_node[0],chosen_node[1]+1] not in visited+visited_temp):
            visited_temp.append([chosen_node[0],chosen_node[1]+1])
            neighbors.append([chosen_node[0],chosen_node[1]+1])
    next_chosen_node = None
    next_chosen_node_cost = math.inf
    for node in neighbors:
        if((node[0],node[1]) in node_cost.keys()):
            temp = chosen_node_cost + matrix[node[0]][node[1]]
            if(temp < node_cost[(node[0],node[1])]):
                node_cost[(node[0],node[1])] = temp
                if(temp < next_chosen_node_cost):
                    next_chosen_node = node
                    next_chosen_node_cost = temp
        else:
            node_cost[(node[0],node[1])] = chosen_node_cost + matrix[node[0]][node[1]]
            if(node_cost[(node[0],node[1])] < next_chosen_node_cost):
                next_chosen_node = node
                next_chosen_node_cost = node_cost[(node[0],node[1])]
            print("Cost: ",[node[0],node[1]],chosen_node,chosen_node_cost,matrix[node[0]][node[1]])
    print(len(visited))

print(node_cost[len(matrix)-1,len(matrix[0])-1])

