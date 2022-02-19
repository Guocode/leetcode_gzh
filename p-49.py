import collections
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for st in strs:
            key = "".join(sorted(st))
            if key in mp:
                mp[key].append(st)
            else:
                mp[key] = [st]

        return list(mp.values())



if __name__ == '__main__':
    a  = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    print(a)