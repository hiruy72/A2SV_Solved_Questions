class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        result = []

        for num in nums1:
            seen[num]= True
        for num in nums2:
            if num in seen:
                result.append(num)
                del seen[num]
        return result
