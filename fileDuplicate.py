
from collections import defaultdict
from typing import List

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mp = defaultdict(list)

        for path in paths:
            parts = path.split(" ")
            directory = parts[0]

            for file in parts[1:]:
                name, content = file.split("(")
                content = content[:-1]   
                full_path = directory + "/" + name
                mp[content].append(full_path)

        result = []
        for files in mp.values():
            if len(files) > 1:
                result.append(files)

        return result
