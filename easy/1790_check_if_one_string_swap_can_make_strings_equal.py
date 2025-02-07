# 1790. Check if One String Swap Can Make Strings Equal
# You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.
# Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2 :
            return True 

        diffs = [(a, b) for a, b in zip(s1, s2) if a != b]

        return len(diffs) == 2 and diffs[0] == diffs[1][::-1]