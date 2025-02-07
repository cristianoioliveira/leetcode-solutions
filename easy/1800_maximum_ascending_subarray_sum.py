# 1800. Maximum Ascending Subarray Sum
# Given an array of positive integers nums, return the maximum possible sum of an ascending subarray in nums.
# A subarray is defined as a contiguous sequence of numbers in an array.
# A subarray [numsl, numsl+1, ..., numsr-1, numsr] is ascending if for all i where l <= i < r, numsi  < numsi+1. Note that a subarray of size 1 is ascending.

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = 0
        current_sum = nums[0]
        prev = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > prev:
                current_sum += nums[i]
            else:
                max_sum = max(max_sum, current_sum)
                current_sum = nums[i]

            prev = nums[i]

        return max(max_sum, current_sum)