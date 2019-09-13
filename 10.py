class Solution1(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        mem = {}
        def helper(i, j):
            
            if (i,j) in mem:
                return mem[(i,j)]
            
            if i==len(s) and j==len(p):
                return True

            if j == len(p):
                return False

            if j<len(p)-1 and p[j+1] == '*':

                r = helper(i, j+2)
                if r: 
                    mem[(i,j)] = True
                    return True
                
                if i == len(s):
                    mem[(i,j)] = False
                    return False

                for ii in range(i, len(s)):
                    if p[j] == s[ii] or p[j] == '.':
                        r = helper(ii+1, j+2)
                        if r: 
                            mem[(i,j)] = True
                            return True
                    else:
                        break

                mem[(i,j)] = False
                return False

            elif i<len(s) and s[i] == p[j] or p[j] == '.':
                mem[(i,j)] = helper(i+1, j+1)
                return mem[(i,j)]
            
            else:
                mem[(i,j)] = False
                return False

        return helper(0,0)

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        ls, lp = len(s)+1, len(p)+1
        s, p = s[::-1], p[::-1]
            
        mem = [[0]*ls for _ in range(lp)]
        mem[0][0] = 1
        
        if p and p[0] == '*':
            mem[2][0] = 1

        for i in range(1, lp):
            if i>1 and p[i-2] == '*':
                continue

            for j in range(ls):
                if p[i-1] == '*':
                    mem[i+1][j] = mem[i-1][j] #if j>0 else 1
                    if j>0 and (p[i] == '.' or  p[i] == s[j-1]):
                        mem[i+1][j] |= (mem[i-1][j-1] | mem[i+1][j-1]) 
                elif j>0 and (p[i-1] == '.' or p[i-1] == s[j-1]):
                    mem[i][j] = mem[i-1][j-1]
                    
        return mem[lp-1][ls-1] 


def main():
    sol = Solution()
    #print sol.isMatch("abacacccbbbcbcbb" ".*.*.*ab*.*ab.*c*")
    print sol.isMatch("aba", "a.*ab.*")
    return
    #print sol.isMatch('a', 'ab*')
    #print sol.isMatch('ab', '.*')
    #print sol.isMatch('ab', 'a*b')
    s = "mississippi"
    p = "mis*is*p*."
    #s = "sipi"
    #p = "p*."
    print sol.isMatch(s,p)
    

if __name__ == "__main__":
    main()
