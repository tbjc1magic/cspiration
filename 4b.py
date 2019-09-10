class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        N1, N2 = len(nums1), len(nums2)
        if N1 > N2:
            N1, N2 = N2, N1
            nums1, nums2 = nums2, nums1

        
        LL, RR = 0, 2*N1
        mem = LL, RR
        while 1:
            
            m1 = (LL+RR)//2
            m2 = N1+N2-m1
            #print m1, m2
            L1 = nums1[(m1-1)//2] if m1>0 else -1000000000
            R1 = nums1[m1//2] if m1<2*N1 else 1000000000
            L2 = nums2[(m2-1)//2] if m2>0 else -1000000000
            R2 = nums2[m2//2] if m2<2*N2 else 1000000000
            
            if L1>R2:
                RR = m1-1
            elif L2>R1:
                LL = m1+1
            
            if mem == (LL, RR):
                break

            mem = (LL,RR)
            
        return (min(R1,R2)+max(L1,L2))/2.


def main():
    sol = Solution()
    res = sol.findMedianSortedArrays([1], [2,3])
    print res
    res = sol.findMedianSortedArrays([100000], [100001])
    print res
    res = sol.findMedianSortedArrays([1,2], [3,4])
    print res
    res = sol.findMedianSortedArrays([1,3], [2])
    print res
    res = sol.findMedianSortedArrays([3], [-2,-1])
    print res
    res = sol.findMedianSortedArrays([], [-2,-1])
    print res
    res = sol.findMedianSortedArrays([4], [1,2,3])
    print res
    res = sol.findMedianSortedArrays([1,2,2], [1,2,3])
    print res

if __name__ == "__main__":
    main()
