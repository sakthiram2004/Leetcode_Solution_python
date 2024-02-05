class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        j=0
        for i in s:
            if s.count(i)==1:
                return j
            j+=1
        return -1
        
