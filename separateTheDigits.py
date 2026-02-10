class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result =[]
        
        
        for i in nums:
            result.append(str(i))
        result2= "".join(result)
        result3= [0] * len(result2)
        for i in range(len(result2)):
            result3[i]= int(result2[i])
        return result3
        