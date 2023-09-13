class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        for i in range (len(score)-1):
            for j in range(i+1,len(score)):
                if score[i][k] <score[j][k]:
                    c=score[i]
                    score[i]=score[j]
                    score[j]=c
        return score

            
