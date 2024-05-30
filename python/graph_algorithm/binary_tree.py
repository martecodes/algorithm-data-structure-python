class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None
    
    
    def append(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._append_recursive(self.root, value)
    
    def _append_recursive(self, node, value):
        if node.value < value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._append_recursive(node.right, value)
        else:
            if node.right is None:
                node.left = Node(value)
            else:
                self._append_recursive(node.left, value)
    
    def print_in_order(self):
        self._print_in_order(self.root)

    def _print_in_order(self, root):
        if root:
            self._print_in_order(root.left)
            print(root.value, end=' ')
            self._print_in_order(root.right)
    
    
tree = BinaryTree()
tree.append(5)
tree.append(1)
tree.append(7)
tree.append(8)
tree.append(2)
tree.append(4)

tree.print_in_order()