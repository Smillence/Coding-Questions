class Node():
  def __init__(self, data, next = None):
    self.data = data
    self.next = next
  def __str__(self):
    return str(self.data)

class LinkedList():
  def __init__(self, lst = []):
    cur = None
    for i in range(len(lst) - 1, -1, -1):
      data = lst[i]
      n = Node(data, cur)
      cur = n
    self.head = cur

  def __str__(self):
    res = []
    cur = self.head
    while cur != None:
      res.append(cur.data)
      cur = cur.next
    return str(res)