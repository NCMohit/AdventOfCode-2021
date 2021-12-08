digits_arr = []
nums_arr = []
file = open("input.txt","r")
for line in file.readlines():
    temp = line.strip().split("|")
    digits_arr.append(temp[0].strip().split(" "))
    nums_arr.append(temp[1].strip().split(" "))

# pajeet tier stuff

def find_actualstring(digits,input_str):
    f = ""
    b = ""   
    e = "" 
    c = ""
    d = ""
    a = ""
    g = ""
    for signal in ["a","b","c","d","e","f","g"]:
        count = 0
        for digit in digits:
            if(signal in digit):
                count += 1
        if(count == 9):
            f = signal
        if(count == 6):
            b = signal
        if(count == 4):
            e = signal
    for digit in digits:
        if(len(digit)==2):
            if(digit[0]==f):
                c = digit[1]
            else:
                c = digit[0]
    for digit in digits:
        if(len(digit)==4):
            temp = [ x for x in digit]
            temp.remove(f)
            temp.remove(b)
            temp.remove(c)
            d = temp[0]
    for digit in digits:
        if(len(digit)==3):
            temp = [ x for x in digit]
            temp.remove(f)
            temp.remove(c)
            a = temp[0]
    for letter in ["a","b","c","d","e","f","g"]:
        if letter not in [a,b,c,d,e,f]:
            g = letter
    letters = {a:"a",b:"b",c:"c",d:"d",e:"e",f:"f",g:"g"}
    newstr = ""
    for letter in input_str:
        newstr += letters[letter]
    return newstr

def get_num(string):    #lmao
    if("f" in string):
        if("c" in string):
            if("a" in string):
                if("d" in string):
                    if("e" in string):
                        return 8
                    else:
                        if("b" in string):
                            return 9
                        else:
                            return 3
                else:
                    if("g" in string):
                        return 0
                    else:
                        return 7
            else:
                if("b" in string):
                    return 4
                else:
                    return 1
        else:
            if("e" in string):
                return 6
            else:
                return 5
    else:
        return 2

counter = 0
for index in range(len(digits_arr)):
    digits = digits_arr[index]
    nums = nums_arr[index]
    for num in nums:
        if(get_num(find_actualstring(digits,num)) in [1,4,7,8]):
            counter += 1
print(counter)
    