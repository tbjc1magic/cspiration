class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        mem = [0] * 256
        l, r = 0, 0

        res = 0
        while r < len(s):
            
            lr = s[r]
            while mem[ord(lr)]:
                ll = s[l]
                mem[ord(ll)] -= 1
                l += 1

            mem[ord(lr)] += 1
            r += 1
            res = max(res, r-l)
        
        return res


sol = Solution()
res = sol.lengthOfLongestSubstring('abcabcbb')
print res
