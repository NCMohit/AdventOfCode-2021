import math, sys
matrix = []

file = open("input.txt","r")
for line in file.readlines():
    row = []
    temp = line.strip()
    for i in temp:
        row.append(int(i))
    matrix.append(row)

node_cost = {(0,0):0}
visited = []
visited_temp = [[0,0]]

# Got filtered Sadge, had to learn Dijkstra's algorithm

while(len(visited_temp) != 0 ):
    chosen_node = None
    chosen_node_cost = math.inf
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
    for node in neighbors:
        if((node[0],node[1]) in node_cost.keys()):
            temp = chosen_node_cost + matrix[node[0]][node[1]]
            if(temp < node_cost[(node[0],node[1])]):
                node_cost[(node[0],node[1])] = temp
        else:
            node_cost[(node[0],node[1])] = chosen_node_cost + matrix[node[0]][node[1]]

print(node_cost[len(matrix)-1,len(matrix[0])-1])

# position = [0,0]
# cost_remember = {}
# visited = [] 

# def recursive_cost(pos,matrix,visited):
#     visited_temp = visited.copy()
#     visited_temp.append(pos)
#     if((pos[0]==0) & (pos[1]==0) ):
#         cost = 0
#     elif( (pos[0]==(len(matrix)-1)) & (pos[1]==(len(matrix[0])-1)) ):
#         return matrix[pos[0]][pos[1]]
#     else:
#         cost = matrix[pos[0]][pos[1]]
#     cost_right =math.inf
#     cost_bottom = math.inf
#     cost_up = math.inf
#     cost_left = math.inf

#     if(pos[1] != (len(matrix[0])-1)):
#         if([pos[0],pos[1]+1] not in visited_temp):
#             if((pos[0],pos[1]+1) in cost_remember.keys()):
#                 cost_right = cost_remember[(pos[0],pos[1]+1)]
#             else:
#                 cost_right = recursive_cost([pos[0],pos[1]+1],matrix,visited_temp)
#                 cost_remember[(pos[0],pos[1]+1)] = cost_right
#     if(pos[1] != 0):
#         if([pos[0],pos[1]-1] not in visited_temp):
#             if((pos[0],pos[1]-1) in cost_remember.keys()):
#                 cost_left = cost_remember[(pos[0],pos[1]-1)]
#             else:
#                 cost_left = recursive_cost([pos[0],pos[1]-1],matrix,visited_temp)
#                 cost_remember[(pos[0],pos[1]-1)] = cost_left
#     if(pos[0] != (len(matrix)-1)):
#         if([pos[0]+1,pos[1]] not in visited_temp):
#             if((pos[0]+1,pos[1]) in cost_remember.keys()):
#                 cost_bottom = cost_remember[(pos[0]+1,pos[1])]
#             else:
#                 cost_bottom = recursive_cost([pos[0]+1,pos[1]],matrix,visited_temp)
#                 cost_remember[(pos[0]+1,pos[1])] = cost_bottom
#     if(pos[0] != 0):
#         if([pos[0]-1,pos[1]] not in visited_temp):
#             if((pos[0]-1,pos[1]) in cost_remember.keys()):
#                 cost_top= cost_remember[(pos[0]-1,pos[1])]
#             else:
#                 cost_top= recursive_cost([pos[0]-1,pos[1]],matrix,visited_temp)
#                 cost_remember[(pos[0]-1,pos[1])] = cost_top
#     # if((pos[0]==0) & (pos[1]==0) ):
#     #     print(visited_temp)
#     min_cost = min([cost_left,cost_right,cost_bottom,cost_up])
#     cost+=min_cost
#     return cost

# ans = recursive_cost(position,matrix,visited)
# print(ans)
