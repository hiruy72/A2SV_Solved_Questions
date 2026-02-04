class Solution:    
    def findUnion(self, a, b):
        # code here
        union= set(a) | set(b)
        return list(union)