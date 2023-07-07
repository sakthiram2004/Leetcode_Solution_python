class Solution(object):
    def findGCD(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mi=min(nums)
        mx=max(nums)
        c=0
        for i in range(1,mx+1):
            if mi%i==0 and mx%i==0:
                c=i
        return c
