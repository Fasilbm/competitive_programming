class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:

        count=Counter(deck)
        count=[[i,j] for i,j in count.items()]
        def gcd(a,b):
            if b==0:
                ans=a
                return ans
            return gcd(b,a%b)
        ans=count[0][1]
        for j in range(1,len(count)):
            ans=gcd(ans,count[j][1])

        if len(count)>1:
            return ans!=1
        elif count[0][1]==1:
            return False
        else:
            return True


            

        

