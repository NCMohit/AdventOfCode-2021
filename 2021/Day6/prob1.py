fish_arr = []
file = open("input.txt","r")
fish_arr = file.readline().strip().split(",")

counter = 0
while(counter<80):
    for fish in range(len(fish_arr)):
        fish_arr[fish] = int(fish_arr[fish])-1
        if(fish_arr[fish]==-1):
            fish_arr[fish] = 6
            fish_arr.append(8)
    counter += 1

print("Length: ",len(fish_arr))