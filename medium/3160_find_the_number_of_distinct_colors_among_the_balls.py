# 3160. Find the Number of Distinct Colors Among the Balls
# You are given an integer limit and a 2D array queries of size n x 2.
# There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.
# Return an array result of length n, where result[I] denotes the number of distinct colors after ith query.
# Note that when answering a query, lack of a color will not be considered as a color.

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_map = {}  
        color_count = {}  
        distinct_colors = 0
        result = []
        
        for ball, color in queries:
            if ball in color_map:
                prev_color = color_map[ball]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    distinct_colors -= 1
            
            color_map[ball] = color
            if color in color_count:
                if color_count[color] == 0:
                    distinct_colors += 1
                color_count[color] += 1
            else:
                color_count[color] = 1
                distinct_colors += 1
            
            result.append(distinct_colors)
        
        return result