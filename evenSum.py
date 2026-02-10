class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(n for n in nums if n % 2 == 0)
        result = []

        for val, idx in queries:
            if nums[idx] % 2 == 0:
                even_sum -= nums[idx]

            nums[idx] += val

            if nums[idx] % 2 == 0:
                even_sum += nums[idx]

            result.append(even_sum)

        return result
