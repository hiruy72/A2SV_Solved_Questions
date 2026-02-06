class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        result = defaultdict(int)
        l1= {value : i for i,value in enumerate(list1)}
        final = []

        least = float('inf')

        for j, val in enumerate(list2):
            if val in l1:
                result[val] += j + l1[val]
                if result[val] <= least:
                    least = result[val]
        for k in result:
            if result[k]==least:
                final.append(k)
        return final

        