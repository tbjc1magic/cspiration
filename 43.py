class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        s2d = {str(i):i for i in range(10)}
        d2s = {i:str(i) for i in range(10)}
        L1, L2 = len(num1), len(num2)
        LL = L1+L2
        n1 = [0]*LL
        
        for i1 in range(L1):
            d1 = s2d[num1[i1]]
            n2 = [0] * LL
            for i2 in range(L2-1, -1, -1):
                offset = L1 - i1 - 1 + L2 - i2 -1
                offset = LL-1-offset
                d2 = s2d[num2[i2]]
                p = d1*d2 + n2[offset] 
                p1, p2 = p//10, p%10
                n2[offset] = p2
                n2[offset-1] = p1

            ex = 0
            for ii in range(LL-1, -1, -1):
                p = n1[ii] + n2[ii] + ex
                p1, p2 = p//10, p%10
                ex, n1[ii] = p1, p2


        res = []
        flag = False
        for n in n1:
            if not flag and n:
                flag = True
            if flag:
                res.append(d2s[n])

        return ''.join(res) if res else '0'
    
sol = Solution()
res = sol.multiply(num1 = "123", num2 = "456")

#res = sol.multiply(num1 = "9", num2 = "9")
print res
