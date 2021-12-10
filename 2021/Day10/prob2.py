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


scores = []
for syntax in syntaxes:
    score = 0
    lol = lmao(syntax)
    if(")" in lol):
        pass
    elif("}" in lol):
        pass
    elif("]" in lol):
        pass
    elif(">" in lol):
        pass
    else:
        lol = lol[::-1]
        for i in lol:
            if(i=="("):
                score = (score*5) + 1
            if(i=="["):
                score = (score*5) + 2
            if(i=="{"):
                score = (score*5) + 3
            if(i=="<"):
                score = (score*5) + 4
        scores.append(score)              
scores.sort()

print(scores[int(len(scores)/2)])      