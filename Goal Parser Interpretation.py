class Solution(object):
    def interpret(self, c):
        """
        :type command: str
        :rtype: str
        """
        c=c.replace("(al)","al")
        c=c.replace("()","o")
        return c
        
