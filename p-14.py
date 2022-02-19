from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        for i,_s in enumerate(strs[0]):
            for j in range(len(strs)-1):
                if len(strs[j+1])<i+1:
                    return strs[0][:i]
                if strs[j+1][i]!= _s:
                    return strs[0][:i]
        return strs[0]


if __name__ == '__main__':
    a = Solution().longestCommonPrefix( ["flower","flow","flight"])
    print(a)