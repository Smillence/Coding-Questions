'''Question:
Given an image represented by an NxN matrix, where each pixel in the image is 
4 bytes, write a method to rotate the image by 90 degrees. 

Can you do this in place?

clarifications:
- assume rotate closewise
- input: matrix
- return: None
'''

from math import ceil
import copy
import unittest
from test_utils import UnitTestBase

# Solution:
# Hint: draw a 4x4 matrix as an example
# Time: O(N*N)
# Space: O(1)
# Hotspot: if N is odd, it will be wrong to use range(ceil(n/2)) to loop i.
# The reason is it will end up rotating twice for some cells
def rotate_matrix(matrix):
  n = len(matrix)
  for i in range(n//2):
    for j in range(ceil(n/2)):
      tmp = matrix[i][j]
      matrix[i][j] = matrix[n - 1 - j][i]
      matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
      matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
      matrix[j][n - 1 - i] = tmp

class TestStrComp(UnitTestBase, unittest.TestCase):
  def data_provider(self):
    return [
      ([], []),
      ([['1111']], [['1111']]),
      ([['1111','2222'], ['3333','4444']], [['3333','1111'], ['4444','2222']]),
      ([['1111','2222','3333'], ['4444','5555','6666'], ['7777','8888','9999']],
       [['7777','4444','1111'], ['8888','5555','2222'], ['9999','6666','3333']],
      ),
      ([['1111','2222','3333', '4444'], 
        ['5555','6666','7777', '8888'], 
        ['9999','0000','aaaa', 'bbbb'],
        ['cccc','dddd','eeee', 'ffff']],
       [['cccc','9999','5555', '1111'], 
        ['dddd','0000','6666', '2222'], 
        ['eeee','aaaa','7777', '3333'],
        ['ffff','bbbb','8888', '4444']],
      ),
    ]

  def func_provider(self):
    return [
      rotate_matrix,
    ]

  def single_test(self, func, data):
    cpy = copy.deepcopy(data)
    matrix = data[0]
    func(matrix)
    self.expect(matrix, func, cpy)

if __name__ == '__main__':
  unittest.main()