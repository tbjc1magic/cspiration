class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = x < 0
        x = abs(x)
        res = 0
        while x > 0:
            d = x%10
            x = x//10
            res = res*10 + d

        res = res * -1 if neg else res
        
        if -(1<<31) <= res <= (1<<31)-1:
            return res
        else:
            return 0



def main():
    sol = Solution()
    print sol.reverse(321)


if __name__ == "__main__":
    main()
