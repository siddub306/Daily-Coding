class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return num
        elif num < 10:
            return num
        
        def convert(num):
            iter1 = []
            while num > 0:
                x = num % 10
                iter1.append(x)
                num //= 10
            return iter1[::-1]

        while num >= 10:
            iter1 = convert(num)
            num = sum(iter1)
        return num


