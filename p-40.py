from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        right = len(candidates) - 1
        left = 0
        while right>=0 and candidates[right] > target:
            right -= 1
        ans = []

        def dfs(target, tmp, idx):
            if target == 0:
                ans.append(tmp.copy())
                return
            if target <= 0 or idx > right:
                return
            step= 1
            while idx+step<=right and candidates[idx+step-1]==candidates[idx+step]:
                step+=1
            dfs(target, tmp, idx + step)

            tmp.append(candidates[idx])
            dfs(target - candidates[idx], tmp, idx + 1)
            tmp.pop()
            return

        dfs(target, [], 0)
        return ans


if __name__ == '__main__':
    a = Solution().combinationSum2(candidates=[2], target=1, )
    print(a)
