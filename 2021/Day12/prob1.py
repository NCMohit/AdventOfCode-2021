edges = []
file = open("input.txt","r")
for line in file.readlines():
    edge = line.strip().split("-")
    edges.append(edge)

current = ["start"]

def find_path(current):
    neighbors = []
    paths = 0
    for edge in edges:
        if(edge[0] == current[-1]):
            if(edge[1] == "end"):
                paths += 1
            elif(edge[1]=="start"):
                pass
            elif(edge[1][0].islower()):
                if(edge[1] not in current):
                    paths += find_path(current + [edge[1]])
            else:
                paths += find_path(current + [edge[1]])
        elif(edge[1] == current[-1]):
            if(edge[0] == "end"):
                paths += 1
            elif(edge[0]=="start"):
                pass
            elif(edge[0][0].islower()):
                if(edge[0] not in current):
                    paths += find_path(current + [edge[0]])
            else:
                paths += find_path(current + [edge[0]])
    return paths

print(find_path(current))
        