# Runtime = 98.91% Better
# Memory usage = 36.49% Better

class Solution:
    def twoSum(self, nums, target):
        hashM = {}

        for i, n in enumerate(nums):
            complement = target - n
            if complement in hashM:
                return [hashM[complement], i]
            hashM[n] = i

        return None