class Solution(object):
    def findThePrefixCommonArray(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        c=[]
        for i in range(1,len(A)+1):
            if i==0:
                c.append(0)
            else:
                c.append(len(set(A[:i]).intersection(set(B[:i]))))
        return c
