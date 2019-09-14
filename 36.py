
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        
        w, h =  len(board[0]), len(board)
        cell, row, col = {}, {}, {}
        
        
        for r in range(h):
            for c in range(w):
                
                v = board[r][c]
                if v.isdigit():
                    v = int(v)
                else:
                    continue
                
                mask = cell.get((r//3,c//3), 0)
                if mask & (1<<v):
                    return False
                cell[(r//3,c//3)] = mask | (1<<v)
                
                mask = row.get(r, 0)
                if mask & (1<<v):
                    return False
                row[r] = mask | (1<<v)
                
                mask = col.get(c, 0)
                if mask & (1<<v):
                    return False
                col[c] = mask | (1<<v)
                
                
        return True
