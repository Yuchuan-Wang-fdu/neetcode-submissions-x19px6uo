class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]*n
        subfix = [1]*n
        res = [1]*n

        for i in range(1,n):
            prefix[i] = nums[i-1]*prefix[i-1]
        for i in range(n-2, -1, -1):
            subfix[i] = nums[i+1]*subfix[i+1]
        for i in range(n):
            res[i] = prefix[i]*subfix[i]
        
        return res

        

        