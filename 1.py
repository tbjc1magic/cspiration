class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mem = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in mem:
                return mem[diff], i
            
            mem[n] = i
            
