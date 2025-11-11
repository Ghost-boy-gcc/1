#Binary Search Tree Implementation

class BST:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, root, key):
        if root is None:
            return BST(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def inorder(self, root):
        return self.inorder(root.left) + [root.key] if root else []

    def preorder(self, root):
        return [root.key] + self.preorder(root.left) + self.preorder(root.right) if root else []

    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) + [root.key] if root else []

    def get_min_node(self, node):
        while node.left:
            node = node.left
        return node

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            
            temp = self.get_min_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

# Example usage
if __name__ == "__main__":
    bst = BST(50)
    root = None
    root = bst.insert(root, 50)
    for key in [20, 30, 20, 40, 70, 60, 80]:
        root = bst.insert(root, key)

    print("Inorder Traversal:", bst.inorder(root))
    print("Preorder Traversal:", bst.preorder(root))
    print("Postorder Traversal:", bst.postorder(root))
    print("Search 40:", "Found" if bst.search(root, 40) else "Not found")

    root = bst.delete(root, 20)
    print("After deleting 20 (inorder):", bst.inorder(root))