
# 栈完全可以用list代替

class Stack:
    def __init__(self):
        self.sk = []
    def push(self,x):
        self.sk.append(x)
    def pop(self):
        self.sk.pop()
    def size(self):
        return len(self.sk)
    def isEmpty(self):
        return len(self.sk) == 0