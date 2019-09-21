class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        d = {}
        for n in nums:
            d[n] = d.get(n,0) + 1
        
        res = []
        keys = d.keys()
        L = len(nums)
        
        def helper(i, trace):
            
            if i == L:
                res.append(trace[:])
            else:

                for k in keys:
                    if d[k] > 0:
                        d[k] -= 1
                        trace.append(k)
                        helper(i+1, trace)
                        trace.pop()
                        d[k] += 1
                        
        helper(0,[])
        return res
