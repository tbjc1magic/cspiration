class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        L = len(s)
        res = (1,0,1)
        for i in range(2*L-1):
            if not i % 2:
                l = 1
                while 1:
                    left, right = i//2-l, i//2+l
                    if 0<=left<right<L and s[left]==s[right]:
                        l += 1
                    else:
                        if right-left-1 > res[0]:
                            res = (right-left-1, left+1, right)        
                        break
            else:
                l = 0
                while 1:
                    left, right = (i-1)//2-l, (i+1)//2+l
                    if 0<=left<right<L and s[left]==s[right]:
                        l += 1
                    else:
                        if right-left-1 > res[0]:
                            res = (right-left-1, left+1, right)        
                        break
                #print i, left, right, res

        return s[res[1]:res[2]]
        

def main():
    sol = Solution()
    print sol.longestPalindrome('babad') 
    print sol.longestPalindrome('cbbd') 
    print sol.longestPalindrome('caba') 

if __name__ == "__main__":
    main()
