class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        a = (n * (n + 1)) / 2
        x = int(a)
        s = 0
        for num in nums:
            s += num
        return (x - s)