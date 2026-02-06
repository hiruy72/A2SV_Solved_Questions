class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        count= Counter(nums)

        result = []

        for i in count:
            if count[i] > n/3:
                result.append(i)
        return result
