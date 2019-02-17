from abc import ABC, abstractmethod
 
class UnitTestBase(ABC):

  @abstractmethod
  def data_provider(self):
    pass

  @abstractmethod
  def func_provider(self):
    pass

  @abstractmethod
  def func_eval(self, func, args):
    pass

  def test(self):
    for func in self.func_provider():
      for data in self.data_provider():
        args = data[0]
        self.expect(self.func_eval(func, args), func, data)

  def expect(self, result, func, data):
    expected = data[1]
    self.assertEqual(result, expected, self.err_msg(func, data))

  def err_msg(self, func, data):
    return  'Failed \'' + func.__name__ + '\'. args & expected: ' + str(data)
