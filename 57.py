

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        a0, b0 = newInterval
        res = []
        for a1,b1 in intervals:
            
            if b0<a1 or b1<a0:
                res.append([a1,b1])
            else:
                a0 = min([a0,a1])
                b0 = max([b0,b1])
        
        res.append([a0,b0])

        return sorted(res)
