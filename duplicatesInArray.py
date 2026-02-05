class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        result= []
        for i in count:
            if count[i] > 1:
                result.append(i)
        return result