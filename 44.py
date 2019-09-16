class Solution1(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        mem = {} 
        def helper(i,j):
            
            if (i,j) in mem: return mem[(i,j)]

            if i==len(s) and j==len(p):
                mem[(i,j)] = True 
                return True
            

            if j==len(p):
                mem[(i,j)] = False
                return False
            

            if i<len(s) and s[i] == p[j] or p[j] == '?':
                mem[(i,j)] = helper(i+1, j+1)
                return mem[(i,j)]

            elif p[j] == '*':
                for ii in range(i, len(s)+1):
                    r = helper(ii, j+1)
                    if r:
                        mem[(i,j)] = True
                        return True

            mem[(i,j)] = False
            return False
        
        return helper(0,0)

class Solution1(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        ls, lp = len(s), len(p)
        #dp = np.zeros([lp+1, ls+1])
        dp = [[0]*(ls+1) for _ in xrange(lp+1)]
        dp[0][0] = 1
        if p[0] == '*':
            dp[1][0] = 1
            #for i in range(ls+1):
            #    dp[1][i] = 1

        for i in range(1,lp+1):
            for j in range(ls+1):
                if j>0 and (p[i-1] == '?' or s[j-1] == p[i-1]):
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    for k in range(j, -1, -1):
                        if dp[i-1][k]:
                            dp[i][j] = 1
                            break

        #print dp
        return dp[len(p)][len(s)]

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        ls, lp = len(s), len(p)

        dp = [[0]*(ls+1) for _ in range(lp+1)]
        dp[0][0] = 1
        if p and p[0] == '*':
            dp[1][0] = 1

        prefix = p.split('*')[0].split('?')[0]
        if s[:len(prefix)] != prefix:
            return False
        suffix = p.split('*')[-1].split('?')[-1]
        if suffix and s[-len(suffix):] != suffix:
            return False        
        
        for i in range(1,lp+1):
            for j in range(ls+1):
                if j>0 and (p[i-1] == '?' or s[j-1] == p[i-1]):
                    dp[i][j] = dp[i-1][j-1]
                elif p[i-1] == '*':
                    for k in xrange(j, -1, -1):
                        if dp[i-1][k]:
                            dp[i][j] = 1
                            break

        return dp[len(p)][len(s)]


sol = Solution()
#res = sol.isMatch(s="", p="**")
#res = sol.isMatch(s="ho", p="**ho")
#res = sol.isMatch(s="adceb", p="*a*b")
res = sol.isMatch(s="aa", p="*")
#res = sol.isMatch(s="cb", p="?a")
#res = sol.isMatch(s="acdcb", p="a*c?b")
#res = sol.isMatch(s="", p="*")
s = "abaabababbbababbbababaaababbaaabbabaaabbbaaabbbaaabbabbababbababbbabbbaabaaaaabaaabbbbbabababababbbbabbaaaaaabaabbbaaaaaaaababbbbaabaabaaaaabaabbabaaaabaaaababaaaaaabaabaabaaaaababbaabaabbababbabbbabb"
p = "ab*bbab*bb*b****ba*ab*ba*aba**b***aa*b*a*bbbaaa*a**bb*b*****aab**b*****a*abaab*a*aba**a*a*aaab*****abba"
s = "babbaabaabaaaaabbbbabaababbababbbaabbbbbbbbbababaabbabbaaabaaabbababbaaabbbbababbbaaababbbbababababaaaabbbbabbbabbabbbaaabaabaababbababbbabaaabbbbaaabbbabbabbbbaabaabbabaabababbbababaaabaaabbbabbaaaabab"
p = "baa*b*ab*aa**bb*bbbaab***b*abbb*bbb*b*aa*b*b*ab*********ab*b***abb***a*bbb***a*a*b*baa*b***bb*b**ba*b*"
import time
start = time.time()
res = sol.isMatch(s,p)
print time.time() - start
print res
