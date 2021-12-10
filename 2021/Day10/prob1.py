class Stack:
    def __init__(self):
        self.stack = []
    def push(self,val):
        self.stack.append(val)
    def pop(self):
        val = self.stack[-1]
        self.stack = self.stack[:-1]
        return val
    def top(self):
        return self.stack[-1]

syntaxes = []
file = open("input.txt","r")
for line in file.readlines():
    syntaxes.append(line.strip())


def lmao(string):
    mystack = Stack()
    iscorrupt = 0

    for i in string:
        if(i in ["{","(","[","<"]):
            mystack.push(i)
        elif(i in ["}",")","]",">"]):
            if( (i=="}") & (mystack.top()=="{")):
                mystack.pop()
            elif( (i==")") & (mystack.top()=="(")):
                mystack.pop()
            elif( (i=="]") & (mystack.top()=="[")):
                mystack.pop()
            elif( (i==">") & (mystack.top()=="<")):
                mystack.pop()
            else:
                mystack.push(i)
    return mystack.stack


score = 0
for syntax in syntaxes:
    brekloop = 0
    for i in lmao(syntax):
        if(brekloop==0):
            if(i==")"):
                score+= 3
                brekloop = 1
            if(i=="]"):
                score += 57
                brekloop = 1
            if(i=="}"):
                score += 1197
                brekloop = 1
            if(i==">"):
                score += 25137
                brekloop = 1    

print(score)      