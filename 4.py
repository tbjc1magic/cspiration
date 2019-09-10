class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

	l1, l2 = len(nums1), len(nums2)
        tgt = (l1 + l2) / 2 
        isOdd = (l1 + l2) % 2  

        def helper(i):
            
            ll1, ll2 = l1, l2
            todo = l1+l2-i-1
            
            if todo == 0:
                n1 = nums1[ll1-1] if ll1 else -100000
                n2 = nums2[ll2-1] if ll2 else -100000
                return max(n1,n2)

            while todo > 1:
                cur = todo / 2
                if ll1*ll2:
                    cur = min(ll1, ll2, cur)

                n1 = nums1[ll1-cur] if ll1 else -100000
                n2 = nums2[ll2-cur] if ll2 else -100000

                if n1 > n2:
                    todo -= cur
                    ll1  -= cur

                else:
                    todo -= cur
                    ll2  -= cur
     
            n1 = nums1[ll1-1] if ll1 else -100000
            n2 = nums2[ll2-1] if ll2 else -100000

            if n1 > n2:
                ll1 -= 1
            else:
                ll2 -= 1
      
            n1 = nums1[ll1-1] if ll1 else -100000
            n2 = nums2[ll2-1] if ll2 else -100000
            
            return max(n1, n2)

        if isOdd:
            return helper(tgt)

        #return helper(tgt-1)
        return (helper(tgt) + helper(tgt-1)) / 2.
      

            


sol = Solution()
#res = sol.findMedianSortedArrays([1,2], [3,4])
#print res
#res = sol.findMedianSortedArrays([1,3], [2])
#print res
#res = sol.findMedianSortedArrays([3], [-2,-1])
#print res
#res = sol.findMedianSortedArrays([], [-2,-1])
#print res
#res = sol.findMedianSortedArrays([4], [1,2,3])
#print res
res = sol.findMedianSortedArrays([1,2,2], [1,2,3])
print res
