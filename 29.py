class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        
        a,b = dividend, divisor
        flag = 1 if a*b > 0 else -1
        a, b = abs(a), abs(b)
        
        l, r =  0, a
        
        
        last = (l,r)
        while l<r:
            
            m = (l+r)//2
            p = m * b
            
            if p == a:
                return m * flag
            
            if p > a:
                r = m
            else:
                l = m
                
            if last == (l,r):
                break
            
            last = (l,r)
        
        if r*b == a: return r*flag
        return l * flag

sol = Solution()
res = sol.divide(-2147483648, -1)
print res

