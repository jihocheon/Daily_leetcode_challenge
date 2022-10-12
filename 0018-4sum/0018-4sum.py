class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = list()
        nums.sort()
        n = len(nums)
        for i in range(0, n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                 continue
            for j in range(i + 1, n - 2):
                if j != i + 1 and nums[j] == nums[j - 1]:
                    continue
                c = j + 1
                d = n - 1
                while c < d:
                    sum = nums[i] + nums[j] + nums[c] + nums[d]
                    if sum < target:
                        c += 1
                    elif sum > target:
                        d -= 1
                    else:
                        output.append([nums[i], nums[j], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
        return output