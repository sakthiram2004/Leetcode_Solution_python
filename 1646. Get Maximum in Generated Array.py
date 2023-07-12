class Solution(object):
    def getMaximumGenerated(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=[]
        for i in range(n+1):
            if i==0:
                l.append(0)
            elif i==1:
                l.append(1)
            elif i%2==0:
                l.append(l[i//2])
            else:
                l.append(l[i//2]+l[(i//2)+1])
        return max(l)

        
