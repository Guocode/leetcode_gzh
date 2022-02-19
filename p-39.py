from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(target, tmp, idx):
            if target == 0:
                ans.append(tmp.copy())
                return
            if target <= 0 or idx == len(candidates):
                return

            dfs(target, tmp, idx + 1)
            tmp.append(candidates[idx])
            dfs(target - candidates[idx], tmp, idx)
            tmp.pop()
            return

        dfs(target, [], 0)
        return ans


if __name__ == '__main__':
    a = Solution().combinationSum(candidates=[2, 3, 6, 7], target=7)
    print(a)
