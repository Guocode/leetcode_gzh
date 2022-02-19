from bisect import bisect_left
from typing import List
import bisect

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        self.ans = -1
        self.bisearch(nums, target, 0, len(nums) - 1)
        return self.ans

    def bisearch(self,nums,target,head,tail):
        if tail-head<=1:
            if nums[tail]==target:
                self.ans = tail
            if nums[head]==target:
                self.ans = head
            return
        mid = (head+tail)//2
        if nums[head]<nums[tail]:
            if target<nums[mid]:
                self.bisearch(nums,target,head,mid)
            else:
                self.bisearch(nums,target,mid,tail)
        else:
            self.bisearch(nums, target, head, mid)
            self.bisearch(nums, target, mid, tail)


if __name__ == '__main__':

    a = Solution().search(nums = [1,3,5], target = 1)
    print(a)