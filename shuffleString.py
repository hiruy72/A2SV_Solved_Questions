class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        pair = []
        result = []
        for i in range(len(s)):
            pair.append([indices[i], s[i]])

        pair.sort()

        

        for j in range(len(pair)):
            result.append(pair[j][1])
        return "".join(result)