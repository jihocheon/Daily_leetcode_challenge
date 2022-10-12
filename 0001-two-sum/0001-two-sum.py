class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in nums and nums.index(remaining) != i:
                return [i, nums.index(remaining)]