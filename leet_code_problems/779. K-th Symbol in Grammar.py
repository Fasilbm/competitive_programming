class Solution:
    def kthGrammar(self, n: int, k: int) -> int:


        def checker(n,k):

            if n==1:

                return 0

            elif k <= 2**(n-2):

                ans = checker(n-1,k)

            else:

                ans = 1 - checker(n-1,k-2**(n-2))


            return  ans

        return checker(n,k)
