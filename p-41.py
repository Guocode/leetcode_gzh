from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        mp1 = 1
        mp2 = 2
        tmpleft = nums[0]
        tmpright = nums[0]
        tmpcnt = 0
        for n in nums:
            if n<=0:
                continue
            if n>tmpright:
                tmpright = n
                

        return mp1


if __name__ == '__main__':
    a = Solution().firstMissingPositive([3,2,1])
    print(a)