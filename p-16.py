from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        a = 0
        ans = 9999
        nums.sort()
        b = a+1
        c = a+2

            if nums[a]+nums[b]+nums[c]<target:
        return

if __name__ == '__main__':
    a = Solution().threeSumClosest([-49,-1,0,1,100],0)
    print(a)