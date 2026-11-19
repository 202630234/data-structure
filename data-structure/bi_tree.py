class tree.node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

root_node = tree.node()
root_node.left = "커피"

node1 = tree.node()
node1.data = "녹차"
root_node.right = node1

node2= tree.node()
node2.data = "꿀물"
root_node.right = node2

node3=tree.node()
node3.data = "아이스티"
node1.left = node3

node4=tree.node()
node4.data = "레몬에이드"
node1.right = node4

node5=tree.node()
node5.data = "밀크티"
node2.left=node5


print(root_node.data,end=" ")
print()
print(root_node.left.data, root_node.right.data, end=" ")
print()
print(root_node.left.left.data, root_node.left.right.data, root_node.right.left.data, root_node.right.right.data, end=" ")