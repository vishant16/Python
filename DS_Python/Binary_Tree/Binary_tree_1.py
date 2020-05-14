
class Node:

    #function to create new node
    def __init__(self,value):
        self.left=None
        self.right=None
        self.data=value


def LevelOrder(root):
    if root is None:
        return
    queue=[]
    queue.append(root)

    while len(queue)>0:

        #print first item data and delete
        print(queue[0].data)
        node=queue.pop(0)

        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)

root=Node(10)
root.left=Node(11)
root.right=Node(9)
root.left.left=Node(7)
root.right.left=Node(15)
root.right.right=Node(8)

print(LevelOrder(root))
