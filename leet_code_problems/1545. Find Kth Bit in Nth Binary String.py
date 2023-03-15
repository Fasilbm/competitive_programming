class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def checker(n,k):

            if n == 1 :

                return 0

            elif k == (2**n)//2 :

                return 1

            elif k < (2**n)//2:

                ans = checker(n-1,k)

            else:

                shift = k - (2**(n-1)-1)-1

                ans = 1 - checker(n-1, 2**(n-1)-1-shift+1)


            return ans

        return str(checker(n,k))
