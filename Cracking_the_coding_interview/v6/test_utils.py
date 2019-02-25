from abc import ABC, abstractmethod
import copy
 
class UnitTestBase(ABC):

  @abstractmethod
  def data_provider(self):
    pass

  @abstractmethod
  def func_provider(self):
    pass

  def func_eval(self, func, args):
    pass

  def test(self):
    for func in self.func_provider():
      for data in self.data_provider():
        self.single_test(func, data)

  def single_test(self, func, data):
    args = data[0]
    cpy = copy.deepcopy(data)
    self.expect(self.func_eval(func, args), func, cpy)

  def expect(self, result, func, data):
    expected = data[1]
    self.assertEqual(str(result), str(expected), self.err_msg(func, data))

  def err_msg(self, func, data):
    return  'Failed \'' + func.__name__ + '\'. args & expected: ' + str(data)
