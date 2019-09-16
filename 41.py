class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        for i in xrange(L):
            n = nums[i]
            nums[i] = -1
            while 0<n<=L:
                tmp = nums[n-1]
                if tmp == n: break
                nums[n-1] = n
                n = tmp
        
        for i in xrange(L):
            if nums[i] <= 0:
                return i+1
        
        return L+1



sol = Solution()
res = sol.firstMissingPositive([3,4,-1,1])
print res
