class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        def helper(s):
            
            l,c = None, 0
            res = []
            for a in s:
                if a == l:
                    c += 1
                else:
                    res.append((l,c))
                    l,c = a, 1
                    
            res.append((l,c))
            
            ans = []
            for l,c in res[1:]:
                ans.append(str(c)+l)
            
            return ''.join(ans)
        
        s = '1'
        
        for i in range(n-1):
            s = helper(s)
            
        return s
        
