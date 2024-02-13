class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=-1
        r=0
        for i in list(set(nums)):
            if(max < nums.count(i)):
                max=nums.count(i)
                r=i
        return r

        
