class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
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
                
                
        def helper(idx):
            if idx == 81:
                return True
            
            r,c = idx//9, idx%9
            cha = board[r][c]
            if cha.isdigit():
                return helper(idx+1)
            else:
                row.setdefault(r,0)
                col.setdefault(c,0)
                cell.setdefault((r//3, c//3),0)
                mask = cell[(r//3, c//3)] | row[r] | col[c]
                for i in range(1,10):
                    if not(mask & (1<<i)):
                        board[r][c] = str(i)
                        cell[(r//3,c//3)] |= 1<<i
                        row[r] |= 1<<i
                        col[c] |= 1<<i
                        res = helper(idx+1)
                        if res: return True
                        cell[(r//3,c//3)] ^= 1<<i
                        row[r] ^= 1<<i
                        col[c] ^= 1<<i
                        board[r][c] = '.'
                        
                return False
            
	helper(0)
	return board

                
            

sol = Solution()
puzzle = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]    
        ]

res = sol.solveSudoku(puzzle)
print res
