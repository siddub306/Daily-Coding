class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sums = 0
        arr = []
        for i in range(len(digits)):
            sums = sums * 10 + digits[i]

        sums += 1
        while sums > 0:
            arr.insert(0, sums % 10)
            sums //= 10
        return arr
