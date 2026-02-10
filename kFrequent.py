class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        k_frequent= count.most_common(k)

        return [k_frequent[i][0] for i in range(len(k_frequent))]