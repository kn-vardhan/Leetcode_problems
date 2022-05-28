class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        count = 0
        for row in board:
            unique = []
            for i in row:
                if i not in unique and i != '.':
                    unique.append(i)
                elif i != '.' and i in unique:
                    return False
        
        for i in range(9):
            unique = []
            for top in range(9):
                if board[top][i] != '.' and board[top][i] not in unique:
                    unique.append(board[top][i])
                    top += 1
                elif board[top][i] != '.' and board[top][i] in unique:
                    return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                unique = {}
                for k in range(3):
                    for l in range(3):
                        if board[i+k][j+l] not in unique and board[i+k][j+l] != '.':
                            unique[board[i+k][j+l]] = 0
                        elif board[i+k][j+l] != '.':
                            return False        
        
        return True
