from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while right-left>1:
            mid = (left+right)//2
            if nums[left]

        return


if __name__ == '__main__':
    Solution().searchInsert(nums = [1,3,5,6], target = 5)