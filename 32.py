class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        for c in s:

            if c == ')' and stack:
                n = 0 
                while stack and type(stack[-1]) is int:
                    n += stack.pop(-1)
                
                if stack and stack[-1] == '(':
                    stack.pop()
                    stack.append(n+2)
                else:
                    stack.append(n)
                    stack.append(')')
            else:
                stack.append(c)

        res = 0
        cur = 0
        for e in stack:
            if type(e) is not int:
                cur = 0
            else:
                cur += e
            
            res = max(cur, res)

        return res

sol = Solution()
res = sol.longestValidParentheses(')()())')
res = sol.longestValidParentheses('()(()')
print res
