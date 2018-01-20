class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            if target - nums[i] in nums and i != nums.index(target - nums[i]):
                return [i, nums.index(target - nums[i])]

        """

        d={}
        i=0
        for n in nums:
            d[n]=i
            i=i+1
        for i in range(0, len(nums))
            if target-nums[i] in d.keys() and i!=nums.index(target-num[i]):
                return [i, nums.index(target-nums[i])]






        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
