class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs(root):
    if root is None:
        return 
    
    stack = [root]
    visited = set()
    
    while stack:
        current = stack.pop()
        if current not in visited:
            print(current.value)
            visited.add(current) 
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
                

# Create the nodes
root = TreeNode('A')
node_b = TreeNode('B')
node_c = TreeNode('C')
node_d = TreeNode('D')
node_e = TreeNode('E')
node_f = TreeNode('F')

# Build the tree
root.left = node_b
root.right = node_c
node_b.left = node_d
node_b.right = node_e
node_c.right = node_f

dfs(root)