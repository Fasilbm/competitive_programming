class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0:
            return 0
        if n==1:
            return x
        if n==0:
            return 1
        if n==-1:
            return 1/x
        if (n>0 or n<0) and n%2==0:
            return self.myPow(x*x,n//2)
        else:
            return x*self.myPow(x*x,n//2)
        #Time Complexity O(logn)
        #SPace Complexity O(logn)
        
