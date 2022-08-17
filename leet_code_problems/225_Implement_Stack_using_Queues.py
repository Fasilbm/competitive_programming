class MyStack:

    def __init__(self):
        self.list1=[]
        self.list2=[]
        

    def push(self,x: int) -> None:
        self.list1.append(x)
        

    def pop(self) -> int:
                for i in range(len(self.list1)-2):
                    for j in range(len(self.list2)-1):
                        temp=self.list1[i]
                        self.list1[i]=self.list2[j]
                        self.list2[j]=temp
                return self.list1.pop()
                self.list1=self.list2.copy()
            
    def top(self) -> int:
            
            return self.list1[-1]

    def empty(self) -> bool:
        if len(self.list1)==0:
            return True
        else:
            return False
    
'''
obj = MyStack()
obj.push(x)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()

'''        
