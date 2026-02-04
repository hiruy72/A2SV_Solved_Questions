
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        for i in b:
            if i in a:
                a.remove(i)
            else:
                return False
        return True
    
    