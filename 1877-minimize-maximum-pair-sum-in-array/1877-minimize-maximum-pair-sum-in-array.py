class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        output = 0
        half = len(nums)-1
        for i in range(len(nums)//2):
            output = max(output, nums[i]+nums[half] )
            half -= 1
        return output