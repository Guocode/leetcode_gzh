from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ij=[0,0]
        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        curdir = 0
        step = 0
        ans = []
        for i in range(len(matrix)*len(matrix[0])):
            ans.append(matrix[ij[0]][ij[1]])
            matrix[ij[0]][ij[1]] = None
            newi = ij[0]+dirs[curdir][0]
            newj = ij[1]+dirs[curdir][1]
            if newi<0 or newi>=len(matrix) or newj<0 or newj>=len(matrix[0]) or matrix[newi][newj] is None:
                curdir= (curdir+1)%4
            ij[0] = ij[0] + dirs[curdir][0]
            ij[1] = ij[1]+dirs[curdir][1]

        return ans

if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    print(matrix)
    mm = matrix.copy()
    mm = mm[::-1]
    print(mm)
    matrix = list(zip(*matrix))[::-1]
    print(matrix)
    a = Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
    print(a)