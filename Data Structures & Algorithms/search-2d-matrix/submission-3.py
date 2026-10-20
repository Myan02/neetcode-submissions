class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0])
        i = 0

        while i < len(matrix):
            if matrix[i][n - 1] > target:
                break
            elif matrix[i][n - 1] == target:
                return True
            
            i += 1
        
        if i >= len(matrix):
            return False
        
        L, R = 0, n - 1
        while L <= R:
            mid = (L + R) // 2

            if matrix[i][mid] < target:
                L = mid + 1
            elif matrix[i][mid] > target:
                R = mid - 1
            else:
                return True
        
        return False

        