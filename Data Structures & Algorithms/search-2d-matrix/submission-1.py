class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low_matrix, high_matrix = 0, len(matrix) - 1
        while low_matrix <= high_matrix:
            middle_matrix = (low_matrix + high_matrix) // 2
            low_index, high_index = 0, len(matrix[middle_matrix]) - 1
            while low_index <= high_index:
                middle_index = (low_index + high_index) // 2
                if matrix[middle_matrix][middle_index] == target:
                    return True
                elif matrix[middle_matrix][middle_index] > target:
                    high_index = middle_index - 1
                elif matrix[middle_matrix][middle_index] < target:
                    low_index = middle_index + 1
            if matrix[middle_matrix][0] > target:
                high_matrix = middle_matrix - 1
            elif matrix[middle_matrix][-1] < target:
                low_matrix = middle_matrix + 1
            else:
                return False
        return False