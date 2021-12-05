nums = []
file = open("input.txt","r")
for line in file.readlines():
    nums.append(int(line.strip()))
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if(nums[i]+nums[j] == 2020):
            print(nums[i]*nums[j])