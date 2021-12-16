file = open("input.txt","r")
for line in file.readlines():
    hex_string = line.strip()

def convert_hex_to_bin(hex_string):
    bin_string = ""
    for hex_char in hex_string:
        temp = str(bin(int(hex_char,16)))[2:]
        if(len(temp)!=4):
            temp = "0"*(4-len(temp)) + temp
        bin_string += temp
    return bin_string

bin_string = convert_hex_to_bin(hex_string)

version_sum = 0
counter = 0
def parse_packet(bin_string):
    global version_sum
    global counter
    version = int(bin_string[counter:counter+3],2)
    counter += 3
    version_sum += version
    type_id = int(bin_string[counter:counter+3],2)
    counter += 3
    if(type_id ==4):
        length = 6
        while True:
            literal_val = bin_string[counter:counter+5]
            counter += 5
            length += 5
            if(literal_val[0]=="0"):
                break
        return length
    else:
        templen = 7
        length_type_id = bin_string[counter]
        counter += 1
        if(length_type_id=="0"):
            length = int(bin_string[counter:counter+15],2)
            counter += 15
            templen += 15
            templen2 = 0
            while(templen2 < length):
                next_sample = parse_packet(bin_string)
                templen2 += next_sample
                templen += next_sample
        else:
            num = int(bin_string[counter:counter+11],2)
            counter += 11
            templen += 11
            for i in range(num):
                templen += parse_packet(bin_string)
        return templen
 
    
try:
    parse_packet(bin_string)
except:
    pass
print(version_sum)