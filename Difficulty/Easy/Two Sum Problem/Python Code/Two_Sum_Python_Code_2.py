class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        empty_set={}
        for i in range(len(nums)):
            if nums[i] in empty_set:
                return [empty_set[nums[i]],i]
            else:
                empty_set[target-nums[i]]=i
        return []
