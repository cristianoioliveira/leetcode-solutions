# 1752. Check if Array Is Sorted and Rotated
# Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
# There may be duplicates in the original array.
# Note: An array A rotated by x positions results in an array B of the same length such that A[i] == B[(i+x) % A.length], where % is the modulo operation.

class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        
        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:  # Verifica se há uma inversão na ordem
                count += 1
                if count > 1:  # Se houver mais de uma inversão, não pode ser um array rotacionado
                    return False
        
        return True
