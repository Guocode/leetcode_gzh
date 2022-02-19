from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # a  = set()
        # delnum = 0
        # for i in range(len(nums)):
        #     i = i-delnum
        #     if nums[i] in a:
        #         nums.pop(i)
        #         delnum+=1
        #     else:
        #         a.add(nums[i])
        #     # print(a)
        #     # print(nums)
        # return len(nums)
        delnum = 0
        for i in range(len(nums)):
            i = i-delnum
            if i>0 and nums[i]==nums[i-1]:
                nums.remove(nums[i])
                delnum+=1
        return len(nums)
if __name__ == '__main__':
    a = Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(a)