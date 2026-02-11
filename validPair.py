class Solution:
    def findValidPair(self, s: str) -> str:
        result = set()
        n = len(s)
        
        
        for i in range(n - 1):
            if s[i] != s[i + 1] and s.count(s[i]) == int(s[i]):
                result.add(s[i])
        
        
        if n >= 2:
            if s[n - 1] != s[n - 2] and s.count(s[n - 1]) == int(s[n - 1]):
                result.add(s[n - 1])
        
        return "".join(list(result))
