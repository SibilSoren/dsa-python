class Stack:
    def __init__(self):
        self.stack = []
        self.sStack = []
    
    def push(self,item):
        if not self.stack:
            self.sStack.append(item)

        self.stack.append(item)

        if self.stack and self.sStack[-1] > item:
            self.sStack.append(item)
    
    def pop(self):
        if(self.stack[-1] == self.sStack[-1]):
            self.stack.pop()
            self.sStack.pop()
        else:
            self.stack.pop()
    
    def min(self):
        if not self.stack:
            return -1
        else:
            return self.sStack[-1]

class StackO1:
    def __init__(self):
        self.stack = []
        self.minEle = -1
    def push(self,item):
        if not self.stack:
            self.stack.append(item)
            self.minEle = item
        elif item > self.minEle:
            self.stack.append(item)
        elif item < self.minEle:
            self.minEle = item
            self.stack.append(2*item - self.minEle)

    def pop(self):
        if not self.stack:
            return -1
        elif self.stack[-1] >= self.minEle:
            self.stack.pop()
        elif self.stack[-1] < self.minEle:
            self.minEle = 2 * self.minEle - self.stack[-1]
            self.stack.pop()
    
    def top(self):
        if not self.stack:
            return -1
        else:
            if self.stack[-1] >= self.minEle:
                return self.stack[-1]
            elif self.stack[-1] < self.minEle:
                return self.minEle
    
    def getMin(self):
        if not self.stack:
            return -1
        return self.minEle



    

s1 = StackO1()
s1.push(13)
s1.push(12)
s1.push(11)
s1.push(19)
s1.push(10)
# s1.pop()
# s1.pop()
# s1.pop()

print(s1.getMin())