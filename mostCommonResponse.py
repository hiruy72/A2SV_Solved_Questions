class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:

        dic= defaultdict(int)
        max= 0
        word= ""
        for i in responses:
            for j in set(i):
                dic[j] +=1

        for i in dic:
            if max < dic[i]:
                max= dic[i]
                word =i
            elif dic[i] == max and i < word:
                word = i
        return word
        
