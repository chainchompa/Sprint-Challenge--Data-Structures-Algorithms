class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def depth_first_for_each(self, cb):
    # Call the cb function on the current node. Check if there is a left child then call function. Check if there is a right child then call function.
    cb(self.value)
    if self.left:
        self.left.depth_first_for_each(cb)
    if self.right:
        self.right.depth_first_for_each(cb)

  def breadth_first_for_each(self, cb):
    # Add root node to queue. Loop over the queue and remove from the queue. If node has left children then add to queue. If node has right
    # child then add to queue. Invoke the cb function.
    queue = [self]

    while queue:
        node = queue.pop(0)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        cb(node.value)

  def insert(self, value):
    new_tree = BinarySearchTree(value)
    if (value < self.value):
      if not self.left:
        self.left = new_tree
      else:
        self.left.insert(value)
    elif value >= self.value:
      if not self.right:
        self.right = new_tree
      else:
        self.right.insert(value)

  def contains(self, target):
    if self.value == target:
      return True
    if self.left:
      if self.left.contains(target):
        return True
    if self.right:
      if self.right.contains(target):
        return True
    return False

  def get_max(self):
    if not self:
      return None
    max_value = self.value
    current = self
    while current:
      if current.value > max_value:
        max_value = current.value
      current = current.right
    return max_value
