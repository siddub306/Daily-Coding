class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        sums = 1
        func = int((num**0.5) + 1)
        for i in range(2, func):
            if num % i == 0:
                sums += i
                if i != (num // i):
                    sums += num // i
        
        return sums == num
