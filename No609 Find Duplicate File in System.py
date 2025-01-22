from collections import defaultdict
import re
from typing import List


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for path in paths:
            sp = path.split(" ")
            if len(sp) <= 1:
                continue
            p = sp[0]
            fs = sp[1:]
            for f in fs:
                mp[f.split("(")[1][:-1]].append(p + "/" + f.split("(")[0])
        res = []
        for key in mp.keys():
            if len(mp[key]) > 1:
                res.append(mp[key].copy())
        return res

solution = Solution()
print(solution.findDuplicate(paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))
print(solution.findDuplicate(paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]))
