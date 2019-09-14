class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l,r = -1, len(nums)
        
        last = None
        while l<r:
            
            m = (l+r)//2
            if m<0:
                num = -1000
            elif m==len(nums):
                num = 1000
            else:
                num = nums[m]
                
            if num == target:
                return m
            elif num > target:
                r = m
            else:
                l = m
                
            if last == (l,r):
                break
            last = (l,r)

        return l + 1


sol = Solution()
res = sol.searchInsert([1,3,5,6], 2)
print res
