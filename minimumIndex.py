class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count_first= defaultdict(int)
        count_second= defaultdict(int)
        for num in nums:
            count_second[num] +=1
        for j in range(len(nums)):
            l1= (j+1)//2
            l2 =(len(nums) -1 -j)//2
            count_second[nums[j]] -=1
            count_first[nums[j]] +=1


            if count_first[nums[j]] > l1 and count_second[nums[j]] > l2:
                return j 


        return -1
