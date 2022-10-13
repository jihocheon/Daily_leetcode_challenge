class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeat = Counter(s)
        for c in s :
            if repeat[c] == 1 :
                return s.index(c)
            
        return -1