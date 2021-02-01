# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
  def __init__(self, handler):
    # Initialize the trie with an root node and a handler, this is the root path or home page node
    self.root = RouteTrieNode()
    self.root.children['/'] = RouteTrieNode('root handler')

  def insert(self, path, handler):
    current_node = self.root
    for subPath in path:
      if subPath == '':
        continue
      if subPath not in current_node.children:
        current_node.children[subPath] = RouteTrieNode()
      current_node = current_node.children[subPath]
    current_node.handler = handler
  def find(self, path):
    if len(path) == 0:
      return None
    current_node = self.root
    for sub_path in path:
      if sub_path not in current_node.children:
        return None
      current_node = current_node.children[sub_path]
    return current_node.handler

class RouteTrieNode:
  def __init__(self, handler=None):
      # Initialize the node with children, plus a handler
      self.children = {}
      self.handler = handler

  def insert(self, path, handler):
    self.children[path] = RouteTrieNode(handler)
  # The Router class will wrap the Trie and handle 
class Router(RouteTrie):
  def __init__(self, root_handler):
    RouteTrie.__init__(self, root_handler)


  def add_handler(self, path, handler):

    path_list = self.split_path(path)
    self.insert(path_list, handler)

  def lookup(self, path):
    path_list = self.split_path(path)
    return self.find(path_list)

  def split_path(self, path):
    if path == "/":
      return ["/"]
    path_pieces = path.split('/')
    path_pieces.remove('')
    return path_pieces

      
# TESTING
router = Router("root handler") 
router.add_handler("/home", "home handler")  
router.add_handler("/home/about", "about handler")  
router.add_handler("/contactus", "contactUs handler")  
router.add_handler("", "Empty handler")


print(router.lookup("/")) 
print(router.lookup("/home")) 
print(router.lookup("/home/about")) 
print(router.lookup("/home/about/")) 
print(router.lookup("/home/about/me")) 
print(router.lookup("/home/about/"))  
print(router.lookup(""))  

