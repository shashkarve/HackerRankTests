'''
class Node:
      def __init__(self,info):
          self.info = info
          self.left = None
          self.right = None


       // this is a node of the tree , which contains info as data, left , right
'''


def height(root):
    left_height = -1
    right_height = -1

    if root.left:
        left_height = height(root.left)

    if root.right:
        right_height = height(root.right)

    if left_height >= right_height:
        return left_height + 1
    else:
        return right_height + 1