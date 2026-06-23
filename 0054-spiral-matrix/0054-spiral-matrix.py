from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []
            
        n = len(matrix)
        m = len(matrix[0])

        total = n * m
        ans = []
        c = 0
        
        # 1. Corrected initial boundaries
        colstart = 0
        rowstart = 0
        colend = m - 1
        rowend = n - 1

        while c < total:
            # Move Right
            for i in range(colstart, colend + 1):
                ans.append(matrix[rowstart][i])
                c += 1
            rowstart += 1  # Move the top boundary down
            if c == total: break

            # Move Down
            for i in range(rowstart, rowend + 1):
                ans.append(matrix[i][colend])
                c += 1
            colend -= 1    # Move the right boundary left
            if c == total: break

            # Move Left
            for i in range(colend, colstart - 1, -1):
                ans.append(matrix[rowend][i])
                c += 1
            rowend -= 1    # Move the bottom boundary up
            if c == total: break

            # Move Up
            for i in range(rowend, rowstart - 1, -1):
                ans.append(matrix[i][colstart])
                c += 1
            colstart += 1  # Move the left boundary right
            
        return ans



        
        