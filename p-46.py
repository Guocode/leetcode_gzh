from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        p = nums
        l = len(nums)
        ret = []
        def bt(tmp,p):
            if len(tmp)==l:
                ret.append(tmp)
                return
            for i in range(len(p)):
                bt(tmp+[p[i]],p[:i]+p[i+1:])
        bt([],p)
        return ret

if __name__ == '__main__':
    a = Solution().permute( [1,2,3])
    print(a)