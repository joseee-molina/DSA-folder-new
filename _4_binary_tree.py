class TreeNode:
    def __init__(self, item=-1, left=None, right=None):
        self.item = item
        self.left=left
        self.right=right

class BinaryTree:

    def __init__(self, root=None):
        self.root=root

    def printPreOrder(self):
        print("Pre order:")
        self.printPreOrderHelper( self.root)

    def printInOrder(self):
        print("In order:")
        self.printInOrderHelper(self.root)
    
    def printPostOrder(self):
        print("Post order:")
        self.printPostOrderHelper(self.root)
    

    def printPreOrderHelper(self,node):
        if node == None:
            return

        print(node.item)
        self.printPreOrderHelper(node.left)
        self.printPreOrderHelper(node.right)
    
    def printInOrderHelper(self,node):
        if node == None:
            return

        self.printPreOrderHelper(node.left)
        print(node.item)
        self.printPreOrderHelper(node.right)
    
    def printPostOrderHelper(self,node):
        if node == None:
            return

        self.printPreOrderHelper(node.left)
        self.printPreOrderHelper(node.right)
        print(node.item)

    def DFS(self):
        stack = []
        self.DFSHelper(self.root, stack)

    def BFS(self):
        queue = []
        self.BFSHelper(self.root, queue)

    def DFSHelper(self,node,stack):
        if(node!=None):
            print(node.item)
            stack.append(node.right)
            stack.append(node.left)

        if(len(stack)>0):
          self.DFSHelper(stack.pop(),stack)

    def BFSHelper(self,node,queue):
        if(node!=None):
            
            print(node.item)
            queue.append(node.left)
            queue.append(node.right)
        if(len(queue)>0):
          self.BFSHelper(queue.pop(0),queue)

def test():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right= TreeNode(4)
    root.right = TreeNode(3)
    root.right.left=TreeNode(5)
    root.right.left.left= (TreeNode(6))
    tree = BinaryTree(root)
    #tree.printPreOrder()
    #tree.printInOrder()
    #tree.printPostOrder()
    #tree.DFS()
    tree.BFS()

if __name__ == "__main__":
    test()