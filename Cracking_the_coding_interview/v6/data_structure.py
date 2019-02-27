class Node():
  def __init__(self, data, next = None):
    self.data = data
    self.next = next
  def __str__(self):
    return str(self.data)

class LinkedList():
  def __init__(self, args = []):
    if isinstance(args, Node):
      self.head = args
      return

    cur = None
    for i in range(len(args) - 1, -1, -1):
      data = args[i]
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

  def get(self, index):
    node = self.head
    for _ in range(index):
      node = node.next
    return node

  def length(self):
    length, pt = 0, self.head
    while pt != None:
      pt = pt.next
      length += 1
    return length

