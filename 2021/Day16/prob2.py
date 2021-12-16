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
        value = ""
        length = 6
        while True:
            literal_val = bin_string[counter:counter+5]
            value += literal_val[1:]
            counter += 5
            length += 5
            if(literal_val[0]=="0"):
                break
        value = int(value,2)
        return [length,[value]]
    else:
        templen = 7
        length_type_id = bin_string[counter]
        counter += 1
        final_value = []
        values = []
        if(length_type_id=="0"):
            length = int(bin_string[counter:counter+15],2)
            counter += 15
            templen += 15
            templen2 = 0
            while(templen2 < length):
                next_sample = parse_packet(bin_string)
                values += next_sample[1]
                templen2 += next_sample[0]
                templen += next_sample[0]
        else:
            num = int(bin_string[counter:counter+11],2)
            counter += 11
            templen += 11
            for i in range(num):
                next_sample = parse_packet(bin_string)
                templen += next_sample[0]
                values += next_sample[1]
        if(type_id == 0):
            final_value.append(sum(values))
        elif(type_id == 1):
            tempval = 1
            for val in values:
                tempval *= val
            final_value.append(tempval)
        elif(type_id == 2):
            final_value.append(min(values))
        elif(type_id == 3):
            final_value.append(max(values))
        elif(type_id == 5):
            if(values[0]>values[1]):
                final_value.append(1)
            else:
                final_value.append(0)
        elif(type_id == 6):
            if(values[0]<values[1]):
                final_value.append(1)
            else:
                final_value.append(0)
        elif(type_id == 7):
            if(values[0]==values[1]):
                final_value.append(1)
            else:
                final_value.append(0)
        return [templen,final_value]

a = parse_packet(bin_string)
print(a[1][0])
