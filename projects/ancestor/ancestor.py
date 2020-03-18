
class Queue():
  def __init__(self):
    self.queue = []
    
  def enqueue(self, value):
    self.queue.append(value)
  
  def dequeue(self):
    if self.size() > 0:
      return self.queue.pop(0)
    else:
      return None
    
  def size(self):
    return len(self.queue)
  
class Graph:
  def __init__(self):
    self.vertices = {}
    
  def add_vertex(self, vertex_id):
    if vertex_id not in self.vertices: 
      self.vertices[vertex_id] = set()
      
  def add_edges(self, v1, v2):
    if v1 in self.vertices and v2 in self.vertices:
      self.vertices[v1].add(v2)
    else:
      raise IndexError('vertex does not exist')
    
    
def earliest_ancestor(ancestors, starting_node):
  
  #path to x method
  #def pathTox(root, x):
    #if root == null:
      #return null
    #if root.value == x:
      #return Stack([x])
    #leftPath = pathTox(root.left, x)
    #if leftPath != null:
      #leftPath.add(root.value)
        #return leftPath
    #rightPath = pathTox(root.right, x):
    #if rightPath != nulll:
      #rightPath.add(root.value)
      #return rightPath
    #return null
