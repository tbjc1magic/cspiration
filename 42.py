class Solution1(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        MAX = -1
        for i, h in enumerate(height):
            if not stack:
                stack.append((h,i))
                MAX = i
            else:
                while h>=stack[-1][0] and stack[-1][1] != MAX:
                    stack.pop()
                stack.append((h,i))
                if h > height[MAX]:
                    MAX = i
        res = 0 
        stone = 0
        L = len(stack)
        p = 0
        for i in range(1,L):
            h = min(stack[i-1][0], stack[i][0]) 
            d = stack[i][1] - stack[i-1][1]
            while p<stack[i][1]:
                res += h - min(h, height[p])
                p += 1

        return res

class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        MAX = 0
        for i, h in enumerate(height):
            if h>height[MAX]:
                MAX = i

        L = len(height)
        res = 0
        p1 = 0
        while p1<MAX:
            p2 = p1
            while p2<MAX and height[p2]<=height[p1]:
                res += height[p1] - height[p2]
                p2 += 1
            p1 = p2

        p1 = L-1
        while p1>MAX:
            p2 = p1
            while p2>MAX and height[p2]<=height[p1]:
                res += height[p1] - height[p2]
                p2 -= 1
            p1 = p2

        return res

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l, r =  0, len(height)-1
        lmax, rmax = height[l], height[r]

        res = 0
        while l<r:
            lmax, rmax = max(lmax, height[l]), max(rmax, height[r]) 
            
            if lmax > rmax:
                res += rmax - height[r]
                r -= 1
            else:
                res += lmax - height[l]
                l += 1

        return res

sol = Solution()
res = sol.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print res
