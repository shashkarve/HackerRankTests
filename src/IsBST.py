""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""
distinct_elements = []
def checkBST2(root, mini = -100, maxi = 100):

    if root.left is None and root.right is None:
        return True

    if root.data in distinct_elements:
        return False
    else:
        distinct_elements.append(root.data)

    if root.left.data >= maxi or root.right.data <= mini:
        return False
    else:
        return (
            checkBST2(root.left, mini, root.data) and
            checkBST2(root.right, root.data, maxi)
        )

def checkBST(root, mini = -1000, maxi = 1000):
    if root.data in distinct_elements :
        return False
    if root.left is None and root.right is None:
        result_set.append(True)
    if root.left:
        if root.left.data >= mini:
            return False
        else :
            checkBST(root.left,root.data, maxi)
    if root.right:
        if root.right.data <= maxi:
            return False
        else:
            checkBST(root.right, mini, root.data)

    return all(result_set)