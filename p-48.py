from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ml = len(matrix)
        for i in range(ml//2):
            for j in range(ml//2):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[ml-1-i][j]
                matrix[ml-1-i][j] = matrix[ml-1-i][ml-1-j]
                matrix[ml - 1 - i][ml - 1 - j] = matrix[i][ml-1-j]
                matrix[i][ml - 1 - j] = tmp

if __name__ == '__main__':
    # m = [[1,2,3],[4,5,6],[7,8,9]]
    m = [[1,2],[3,4]]
    print(m)
    a = Solution().rotate(m)
    print(m)