class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        L = len(nums)
        M, I = -100000, None
        
        def helper(idx):
            
            for i in xrange(idx, L):
                for j in xrange(i+1, L):
                    if nums[i] > nums[j]:
                        nums[i], nums[j] = nums[j], nums[i] 
            

        for i in xrange(L-1, -1, -1):
            if nums[i] < M:
                mm, ii = M, I
                for j in xrange(i+1, L):
                    if nums[i]<nums[j]<mm:
                        mm, ii = nums[j], j
                nums[i], nums[ii] = nums[ii], nums[i]
                helper(i+1)
                return nums
            else:
                M, I = nums[i], i


        helper(0)
        return nums


sol = Solution()
nums = [1,2,3]
res =  sol.nextPermutation(nums)
print nums
