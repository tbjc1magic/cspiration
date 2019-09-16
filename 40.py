from collections import Counter
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        con = Counter(candidates)
        can = sorted(con.keys())
        
        def helper(idx, tgt, mem):
           
            if tgt < 0:
                return

            if tgt == 0:
                res.append(mem[:])
                return

            if idx == len(can):
                return
            
            c = can[idx]
            for n in xrange(con[c]+1):
                helper(idx+1, tgt-n*c, mem+[c]*n)
       
        helper(0, target, [])
        return res

sol = Solution()
#res = sol.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8)
res = sol.combinationSum2(candidates = [1, 2, 1, 5, 6], target = 8)
print res
