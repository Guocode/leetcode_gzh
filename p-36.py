from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in row:
                        return False
                    else:
                        row.add(board[i][j])
        for j in range(9):
            col = set()
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in col:
                        return False
                    else:
                        col.add(board[i][j])
        for i in range(3):
            for j in range(3):
                nine = set()
                for m in range(3):
                    for n in range(3):
                        tmp = board[i * 3 + m][j * 3 + n]
                        if tmp != '.':
                            if tmp in nine:
                                return False
                            else:
                                nine.add(tmp)

        return True


if __name__ == '__main__':
    board = [[".", ".", "4", ".", ".", ".", "6", "3", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             ["5", ".", ".", ".", ".", ".", ".", "9", "."],
             [".", ".", ".", "5", "6", ".", ".", ".", "."],
             ["4", ".", "3", ".", ".", ".", ".", ".", "1"],
             [".", ".", ".", "7", ".", ".", ".", ".", "."],
             [".", ".", ".", "5", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."],
             [".", ".", ".", ".", ".", ".", ".", ".", "."]]
    a = Solution().isValidSudoku(board)
    print(a)
