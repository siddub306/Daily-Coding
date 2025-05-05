class Solution:
    def isHappy(self, n: int) -> bool:
        def next(num):
            sums = 0
            while num > 0:
                dig = num % 10
                sums += (dig ** 2)
                num //= 10
            return sums
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = next(n)
        return n == 1
