class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        c=0
        f=0
        r=0
        i=1
        while f==0:
            if i not in arr:
                c+=1
            if c==k:
                r=i
                break
            i+=1
        return r

