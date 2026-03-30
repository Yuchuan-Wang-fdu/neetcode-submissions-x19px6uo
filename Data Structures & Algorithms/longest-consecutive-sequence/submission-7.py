class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        long = 0
        for num in numSet:
            if (num-1) not in numSet:
                len = 1
                while (num+len) in numSet:
                    len +=1
                long = max(long, len)

        return long

            
         
            
        