class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        p = 1
        for i in range(1,n):
            p *= i
       
        k = k-1
        res = []
        ALL = range(1,n+1)
        while n > 2:
            idx = k//p
            res.append(ALL[idx])
            k = k-idx*p
            p = p/(n-1)
            n = n-1
            ALL = sorted(ALL[:idx]+ALL[idx+1:])

        if k == 1:
            res.extend(ALL[::-1])
        else:
            res.extend(ALL)

        return res

sol = Solution()
#res = sol.getPermutation(4, 9)
#res = sol.getPermutation(3, 3)
res = sol.getPermutation(2, 2)
print res
