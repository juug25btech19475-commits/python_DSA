# In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

# You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

# The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

# If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

# Example 1:

# Input: mat = [[1,2],[3,4]], r = 1, c = 4
# Output: [[1,2,3,4]]

# Example 2:

# Input: mat = [[1,2],[3,4]], r = 2, c = 4
# Output: [[1,2],[3,4]]

 

# Constraints:

#     m == mat.length
#     n == mat[i].length
#     1 <= m, n <= 100
#     -1000 <= mat[i][j] <= 1000

class Solution(object):
    def matrixReshape(self, mat, r, c):
<<<<<<< HEAD
        if len(mat) * len(mat[0]) != r * c:
            return mat

        nums = []

        for row in mat:
            for x in row:
                nums.append(x)

        ans = []

        for i in range(0, len(nums), c):
            ans.append(nums[i:i+c])

        return ans
=======
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        ans=[]
        for row in range(len(mat)):
            for col in range(len(mat)):
               ans.append(mat[row][col])
        return ans 

            
>>>>>>> 55467f02df48b046a4050269b5071aee4d578153
