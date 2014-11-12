"""
The "treeBuilder" contain functions for building a tree.
The BinaryTree function holds the root node and the first left and right array.
The tree is created with the concept of nested arrays. Each list contains primarily 3 other lists.
For example, in tree alpha = [r,[a],[b]; "r" is the root node, "a" is the left node and "b" is the right node

"""


class treeBuilder:

    def binaryTree(self, r):
        return [r, [], []]                    # creates the root node with two children (ie, the left and rigth nodes)

    def insertLeft(self, root, newBranch):
        t = root.pop(1)   # This pops the current value occupying the list[1], then assigns it to the 't' variable.
        if len(t) > 1:
            root.insert(1, [newBranch, t, []])   # If there was already a node there the new branch would replace it. The previous parent node would be moved (push) to the left (as the left node) and an empty leaf node would be created on the right.
        else:
            root.insert(1, [newBranch, [], []])  # if there's nothing currently there, then the new branch becomes the parent node. Which would then create 2 empty leaf node as its children.
        return root

    def insertRight(self, root, newBranch):
        t = root.pop(2)
        if len(t) > 1:
            root.insert(2, [newBranch, [], t])
        else:
            root.insert(2, [newBranch, [], []])
        return root

    def getRootVal(self, root):
        return root[0]

    def setRootVal(self, root, newVal):
        root[0] = newVal

    def getLeftChild(self, root):
        return root[1]

    def getRightChild(self, root):
        return root[2]
