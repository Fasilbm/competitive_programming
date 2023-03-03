class StockSpanner:

    def __init__(self):

        self.stack=[]
        
    def next(self, price: int) -> int:

        if not self.stack:

            self.stack.append([price,1])

            return 1

        else:
            count=1

            if self.stack[-1][0]>price:

                self.stack.append([price,count])

                return count

            else:

                while self.stack and self.stack[-1][0]<=price:

                    count+=self.stack[-1][1]
                    self.stack.pop()

                self.stack.append([price,count])
                return count

                
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
