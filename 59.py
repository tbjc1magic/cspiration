class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
        pos = [[(r,c) for c in range(n)] for r in range(n)]
        
        res = []
        
        while pos:
            res.extend(pos[0])
            pos = zip(*pos[1:])[::-1]
            
        matrix = [[0]*n for _ in range(n)]
        for idx, (r,c) in enumerate(res):
            matrix[r][c] = idx+1
            
        return matrix
            
