class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        sufix = [0]*n
        res = [0]*n
        
        prefix[0] = sufix[n-1] = 1

        for i in range(1,n):
            prefix[i] = nums[i-1]*prefix[i-1]
        for i in range(n-2, -1, -1):
            sufix[i]= nums[i+1]*sufix[i+1]
        for i in range(n):
            res[i] = prefix[i]*sufix[i]
        return res