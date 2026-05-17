class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        count1, count2 = [0]*26, [0]*26
        match, l = 0, 0
        for c in s1:
            count1[ord(c)-ord('a')] += 1
        for i in range(len(s1)):
            count2[ord(s2[i])-ord('a')] += 1
        for i in range(26):
            if count1[i] == count2[i]:
                match += 1
        
        for r in range(len(s1), len(s2)):
            if match == 26:
                return True
            rindex = ord(s2[r])-ord('a')
            count2[rindex] += 1
            if count1[rindex] == count2[rindex]:
                match += 1
            elif count1[rindex] + 1 == count2[rindex]:
                match -= 1
            
            lindex = ord(s2[l]) - ord('a')
            count2[lindex] -= 1
            if count1[lindex] == count2[lindex]:
                match += 1
            elif count1[lindex] == count2[lindex] + 1:
                match -= 1
            l += 1
        return match == 26
            
            
            
            
        

        
        
        