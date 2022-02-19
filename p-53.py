from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        slow = -1
        fast = 0
        ans = nums[0]
        tmp = 0
        while fast<len(nums):
            tmp+=nums[fast]
            ans = max(ans, tmp)
            if tmp>0:
                pass
            else:
                tmp=0
            fast+=1

        return ans

if __name__ == '__main__':
    a = Solution().maxSubArray( [-2,1,-3,4,-1,2,1,-5,4])
    print(a)