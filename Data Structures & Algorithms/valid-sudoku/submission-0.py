from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_dict = defaultdict(set)
        col_dict = defaultdict(set)
        sqr_dict = defaultdict(set)
        # add pieces to corresponding key on each dict
        for row in range(len(board)):
            for col in range(len(board)):
                piece = board[row][col]
                if (piece == "."):
                    continue

                if (piece in row_dict[row] or piece in col_dict[col] or piece in sqr_dict[(row // 3, col // 3)]):
                    print(row, col, piece)
                    print(col_dict)
                    print(piece in row_dict[row])
                    print(piece in col_dict[col])
                    print(piece in sqr_dict[(row // 3, col // 3)])
                    return False
                row_dict[row].add(piece)
                col_dict[col].add(piece)
                sqr_dict[(row // 3, col // 3)].add(piece)
                
        return True
                


        