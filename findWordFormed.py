class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char= Counter(chars)

        
        sum=0

        for i in words:
            count =0
            word= Counter(i)
            for j in i:
                if word[j] > char[j]:
                    continue
                else:
                    count +=1
            if count == len(i):
                sum +=count
        return sum