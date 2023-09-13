class Solution(object):
    def matrixSum(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """
        for i in nums:
            i.sort(reverse=True)
        s=0
        for i in range (len(nums[0])):
            c=0
            for j in range(len(nums)):
                c=max(c,nums[j][i])
            s=s+c
        return s

            
