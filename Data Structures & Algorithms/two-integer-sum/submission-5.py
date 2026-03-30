class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap = {}

        for i, n in enumerate(nums):
            t = target - n
            if t in preMap:
                return [preMap[t], i]
            preMap[n] = i
        
            


        