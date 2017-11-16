from task_04 import BinarySearchTree


order = [1,4,6,10,0,0,0,7,0,8,0,0,2,5,0,0,3,9,0,0,0]
tree = BinarySearchTree(order)
print(tree.asArr(tree.root()))
a = tree.find_sum(13)
for path in a:
    for x in path:
        print(x.value, end=' ')
    print("\n",path)