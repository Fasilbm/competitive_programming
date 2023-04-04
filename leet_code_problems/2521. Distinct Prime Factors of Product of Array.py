class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        primes=set()
        def factorization(i):
            d = 2
            while d * d <= i:
                while i % d == 0:
                    primes.add(d)
                    i //= d
                d += 1
            if i > 1:
                primes.add(i)
        for i in nums:
            factorization(i)

        return len(primes)
