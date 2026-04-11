class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        ma = 1
        mi = 1
        for n in nums: 
            if n == 0: 
                ma = 1
                mi = 1
            else:
                tmp = ma
                ma = max(tmp*n,mi*n,n)
                mi = min(tmp*n,mi*n,n)
                res = max(res, ma)
        return res