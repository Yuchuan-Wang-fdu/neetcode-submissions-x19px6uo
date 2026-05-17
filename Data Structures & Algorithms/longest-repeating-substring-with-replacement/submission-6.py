class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l, freq = 0, 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            freq = max(freq, count[s[r]])
            while (r-l+1)-freq>k:
                count[s[l]] -= 1
                l += 1  
        return (r-l+1)

        