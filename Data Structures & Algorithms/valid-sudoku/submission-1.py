from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(list)
        col_dict = defaultdict(list)
        sqr_dict = defaultdict(list)

        for row in range(len(board)):
            for col in range(len(board)):
                # print(board[row][col])
                piece = board[row][col]
                if piece == ".":
                    continue
                if (piece in row_dict[row] or piece in col_dict[col] 
                    or piece in sqr_dict[(row // 3, col // 3)]):
                    return False

                row_dict[row].append(piece)
                col_dict[col].append(piece)
                sqr_dict[(row // 3, col // 3)].append(piece)


                # sqr_dict[(row // 3, col // 3)]

        return True
        