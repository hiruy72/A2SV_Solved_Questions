class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_ransom =Counter(ransomNote)
        count_magazine =Counter(magazine)

        for i in count_ransom:
            if count_ransom[i] > count_magazine[i]:
                return False
        return True
