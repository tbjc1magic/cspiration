
import heapq
class Solution1(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        L = len(nums)
        hp = [[0,0]]
        
        
        for i in range(L):
            
            while hp[0][1] < i:
                heapq.heappop(hp)
            
            heapq.heappush(hp, [hp[0][0]+1, nums[i]+i])
            
                
                
        return hp[0][0] 


class Solution2(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l,r = 0,0
        L = len(nums)

        jump = 0
        while r<L-1:
            
            nxt = -1
            for i in range(l,r+1):
                nxt = max(nums[i]+i, nxt)
            
            jump += 1
            l,r = r+1, nxt

        return jump

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        l,r = 0,0
        L = len(nums)

        jump = 0

        far = nums[0]
        for i in range(L):
            
            if i>l:
                jump += 1
                l,r = r+1, far
            
            far = max(far, nums[i]+i)

        return jump


sol = Solution()
res = sol.jump([2,3,1,1,4])
print res
