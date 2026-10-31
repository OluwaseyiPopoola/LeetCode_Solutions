"""
https://leetcode.com/problems/rotate-image/
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation

"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        i, j = 0, 0
        i_end, j_end = len(matrix) - 1, len(matrix) - 1
        size = len(matrix)
                
        while i < i_end:
            print(i, j, i_end, j_end)
            new_j = j
            while new_j < i_end:
                print(f"new_j {new_j}")
                temp = matrix[i][new_j]

                matrix[i][new_j] = matrix[size - new_j - 1][i]
                matrix[size - new_j - 1][i] = matrix[size - i - 1][size - new_j - 1]
                matrix[size - i - 1][size - new_j - 1] = matrix[new_j][size - i - 1]
                matrix[new_j][size - i - 1] = temp
                new_j += 1

            print(matrix)
            # print(size)

            # size -= 2
            i += 1
            j += 1
            i_end -= 1
            j_end -= 1

            

        return matrix



        