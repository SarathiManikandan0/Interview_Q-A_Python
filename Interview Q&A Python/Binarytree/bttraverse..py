#Problem:
#Given a binary tree, write a function to level order traverse the tree and return the result as a list of lists, where each inner list represents a level in the tree.
# Binary Tree:
#       1
#     /   \
#    2     3
#   / \   / \
#  4   5 6   7

# Expected Output:
# [[1], [2, 3], [4, 5, 6, 7]]

# Tree Node definition
class TreeNode:
    def __init__(self, val =0,left = None,right = None):
        self.val = val
        self.left = left
        self.right = right
def level_order_traversal(root):
    if not root:
        return[]
    result = []
    queue = []
    
    queue.append(root)
    
    while queue:
        level_nodes = []
        level_size = len(queue)
        
        for _ in range(level_size):
            node = queue.pop(0)
            level_nodes.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(level_nodes)
    return result
#Test the level order traversal function
if __name__ == "__main__":
    
 # Create the Binary tree
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)  
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
 
 # perform level order  Traversal
    traversal_result = level_order_traversal(root)
    print(traversal_result)
 
           