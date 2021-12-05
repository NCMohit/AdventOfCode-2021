nums = []
file = open("input.txt","r")
for line in file.readlines():
    nums.append(int(line.strip()))
for i in range(len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            if(nums[i]+nums[j]+nums[k] == 2020):
                print(nums[i])
                print(nums[j])
                print(nums[k])
                print(nums[i]*nums[j]*nums[k])