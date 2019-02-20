'''Question:
Write an algorithm such that if an element in an MxN matrix is 0, its entire row
 and column are set to 0.

 Can you do this in space?

clarification:
- side effect
- input and return value
'''

import copy
import unittest
from test_utils import UnitTestBase

# Solution: use the last row and last column as storage space
# Time: O(M*N)
# Space: O(1)
# assumption: matrix has M rows, N column. M and N both >= 1
def zero_matrix(matrix):
  
  m = len(matrix)
  n = len(matrix[0])

  change_last_row = False
  for i in range(n):
    if matrix[m - 1][i] == 0:
      change_last_row = True
      break

  change_last_col = False
  for i in range(m):
    if matrix[i][n - 1] == 0:
      change_last_col = True
      break

  # find out which columns and rows need to be changed
  for i in range(m - 1):
    for j in range(n - 1):
      if matrix[i][j] == 0:
        matrix[m - 1][j] = 0 # last row
        matrix[i][n - 1] = 0 # last column

  for i in range(m - 1):
    if matrix[i][n - 1] == 0:
      # change entire row
      for j in range(n - 1):
        matrix[i][j] = 0

  for i in range(n - 1):
    if matrix[m - 1][i] == 0:
      # change entire column
      for j in range(m - 1):
        matrix[j][i] = 0

  if change_last_row:
    for i in range(n):
      matrix[m - 1][i] = 0

  if change_last_col:
    for i in range(m):
      matrix[i][n - 1] = 0

class Test(UnitTestBase, unittest.TestCase):
  def data_provider(self):
    return [
      ([[1]], [[1]]), # 1*1
      ([[0]], [[0]]), # 1*1
      ([[1, 0]], [[0, 0]]), # 1*2
      ([[1, 1], [1, 1]], [[1, 1], [1, 1]]), # 2*2
      ([[0, 0], [0, 0]], [[0, 0], [0, 0]]), # 2*2
      ([[1, 0], [1, 1]], [[0, 0], [1, 0]]), # 2*2
      ([[1, 0, 1], [1, 1, 1], [0, 1, 1]],
       [[0, 0, 0], [0, 0, 1], [0, 0, 0]],
      ), # 3*3
      ([[1, 2, 3, 4, 0],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 0, 18, 19, 20],
        [21, 22, 23, 24, 25]
       ],
       [[0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [11, 0, 13, 14, 0],
        [0, 0, 0, 0, 0],
        [21, 0, 23, 24, 0]
       ]), # 5 * 5
    ]

  def func_provider(self):
    return [
      zero_matrix,
    ]

  def single_test(self, func, data):
    cpy = copy.deepcopy(data)
    matrix = data[0]
    func(matrix)
    self.expect(matrix, func, cpy)

if __name__ == '__main__':
  unittest.main()