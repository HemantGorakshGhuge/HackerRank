

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left, right
'''
def getHeight(root, treeHeight, maxTreeHeight):

    if not(root):
        maxTreeHeight = max(maxTreeHeight, treeHeight)
        treeHeight = 0
        return maxTreeHeight
    else:
        treeHeight += 1
        maxTreeHeight = getHeight(root.left, treeHeight = treeHeight, maxTreeHeight = maxTreeHeight)
        maxTreeHeight = getHeight(root.right, treeHeight = treeHeight, maxTreeHeight = maxTreeHeight)

    return maxTreeHeight


def height(root):
    maxTreeHeight = 0
    treeHeight =  0
    maxTreeHeight = getHeight(root, treeHeight, maxTreeHeight)
    return maxTreeHeight - 1


