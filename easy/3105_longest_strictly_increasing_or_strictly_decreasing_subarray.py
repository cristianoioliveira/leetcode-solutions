# 3105. Longest Strictly Increasing or Strictly Decreasing Subarray
# You are given an array of integers nums. Return the length of the longest subarray of nums which is either strictly increasing or strictly decreasing.

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc_len = dec_len = 1
        max_len = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                inc_len += 1
                dec_len = 1 
            elif nums[i] < nums[i - 1]: 
                dec_len += 1
                inc_len = 1 
            else: 
                inc_len = dec_len = 1

            max_len = max(max_len, inc_len, dec_len)
        
        return max_len