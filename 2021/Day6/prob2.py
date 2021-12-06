fish_arr = []
file = open("input.txt","r")
fish_arr = file.readline().strip().split(",")

counter = 0
fish_dict = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0}
for fish in fish_arr:
    fish_dict[fish]+=1


while(counter<256):
    tempdict = fish_dict.copy()
    for i in range(0,9):
        i_str = str(i)
        if(i==6):
            fish_dict[i_str] = tempdict[str(i+1)] + tempdict["0"]
        elif(i==8):
            fish_dict[i_str] = tempdict["0"]
        else:
            i_str = str(i)
            fish_dict[i_str] = tempdict[str(i+1)]
    counter += 1

length = 0
for i in fish_dict.values():
    length += i
print("Length: ",length)