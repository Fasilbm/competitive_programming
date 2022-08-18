class MyQueue:

    def __init__(self):
        self.list1=[]
        self.list2=[]
        

    def push(self, x: int) -> None:
         for i in range(len(self.list1)):
            for j in range(len(self.list2)):
                    temp=self.list1[((len(self.list1)-i))]
                    self.list1[((len(self.list1))-i)]=self.list2[j]
                    self.list2[j]=temp
         self.list1.append(x)

    def pop(self) -> int:
        self.list1.reverse()
        temp = self.list1.pop()
        self.list1.reverse()
        return temp

    def peek(self) -> int:
        return self.list1[0]
        

    def empty(self) -> bool:
        return len(self.list1)==0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
