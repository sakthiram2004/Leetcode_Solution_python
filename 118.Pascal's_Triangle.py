class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r=[]
        for i in range(1,numRows+1,1):
            t=[]
            if i==1 or i==2:
                for i in range(i):
                    t.append(1)
                r.append(t)
            else:
                t.append(1)
                for j in range(i-2):
                    s=r[i-2][j]+r[i-2][j+1]
                    t.append(s)
                t.append(1)
                r.append(t)
        return r
