class Solution:
    def minSteps(self, n: int) -> int:
        if n==1:
            return 0
            
        first=0
        count=0
        def isPrime(n):
            d = 2
            while d * d <= n:
                if n % d == 0:
                    return
                d += 1
            return n
        ans=isPrime(n)
        if ans == n and first==0:
            return ans
        elif ans == n and first==1:
            ans=ans+count
            return ans
        elif first==1:
            return
        first=1
        import math
        def findfac(n):
            faclist = [1]
            for i in range(2, int(math.sqrt(n) + 2)):
                if n%i == 0:
                    if i not in faclist:
                        faclist.append(i)
                        if n/i not in faclist:
                            faclist.append(int(n/i))
                ans=sorted(faclist)
            return ans
        def gcd(n):
            nonlocal count
            ans=isPrime(n)
            if ans == n and first==1:
                ans=ans+count
                return ans
            if n%2==0:
                count+=2
                n//=2
                x=gcd(n)
                return x
            else:
                ans=findfac(n)
                # nonlocal count
                count+=(n//ans[-1])
                n=ans[-1]
                x=gcd(n)
                return x
                
        x=gcd(n)
        return x


class Solution:
    def minSteps(self, n: int) -> int:
        @cache
        def find_divisors(number):
            divisors = []
            for i in range(1, number//2):
                if number % i == 0:
                    divisors.append(i)
            return divisors

        def get_min(num):
            if num == 1:
                return 0
            ans = num
            for i in find_divisors(num):
                paste = (num//i)-1
                steps = get_min(i)
                ans=min(ans,steps+1+paste)
            return ans
        return get_min(n)


       

        

            

                    
