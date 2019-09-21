class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        mem = [0] * len(nums)
        
        def helper(i, trace):
            
            if i == len(nums):
                res.append(trace[:])
                return
            
            for k in range(len(nums)):
                if not mem[k]:
                    mem[k] = 1
                    trace.append(nums[k])
                    helper(i+1, trace)
                    trace.pop()
                    mem[k] = 0
                    
        helper(0, [])
        return res
        
