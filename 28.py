class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        L1, L2 = len(haystack), len(needle)
        
        for i in range(L1-L2+1):
            if haystack[i:i+L2] == needle:
                return i
            
        return -1
            
            
