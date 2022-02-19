from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # cnt = [0]+[len(nums)]*(len(nums)-1)
        # # print(cnt)
        # for i in range(len(nums)):
        #     for j in range(i+1,min(i+nums[i]+1,len(nums))):
        #         cnt[j]=min(cnt[j],cnt[i]+1)
        # return cnt[-1]
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


if __name__ == '__main__':
    ret = Solution().jump(nums = [2,3,1,1,4])
    print(ret)