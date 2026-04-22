class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        res = [1] * n

        leftProduct = 1

        for i in range(n):
            res[i] = leftProduct
            leftProduct *= nums[i]
        
        rightProduct = 1

        for i in range(n-1, -1, -1):
            res[i] *= rightProduct
            rightProduct *= nums[i]
        
        return res
        