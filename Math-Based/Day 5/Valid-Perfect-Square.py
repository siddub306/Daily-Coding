class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 1:
            return False
        
        x = num ** 0.5
        return x.is_integer()
        
