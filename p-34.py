from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.ans = [-1,-1]
        left = 0
        right = len(nums)-1

        # self.bisearchRange(nums,target,0,len(nums)-1)
        return self.ans

    # def bisearchRange(self, nums: List[int], target: int,left,right) -> List[int]:
    #     if left
    #     return
if __name__ == '__main__':

    a = Solution().searchRange(nums = [5,7,7,8,8,10], target = 8)
    print(a)