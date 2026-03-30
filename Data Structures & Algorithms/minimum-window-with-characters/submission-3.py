class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        countT, window = {},{}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        need, have = len(countT), 0
        res, reslen = [-1,-1], float("infinity")
        l = 0
        
        for r in range(len(s)):
            ch = s[r]
            window[ch] = 1 + window.get(ch, 0)
            if ch in countT and window[ch] == countT[ch]:
                have += 1
            
            while have == need:
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                
                if (r-l+1)<reslen:
                    res = [l, r]
                    reslen = r-l+1
                
                l += 1
        
        l, r = res
        
        return s[l:r+1] if reslen < float("infinity") else ""



        

