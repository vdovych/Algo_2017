class BinarySearchTree:
    class Node:
        def __init__(self, value, parent, lson=None, rson=None):
            self.value = value
            self.parent = parent
            self.lson = lson
            self.rson = rson

    def __init__(self, preorder):
        def add_member(order, parent):
            if order is None:
                return None, None
            if order[0] == 0:
                if len(order) > 1:
                    return None, order[1:]
                else:
                    return None, None
            node = self.Node(order[0], parent)
            if len(order) == 1:
                return node, None
            node.lson, new_order = add_member(order[1:], node)
            node.rson, new_order = add_member(new_order[:], node)
            return node, new_order

        self.rooot = add_member(preorder, None)[0]
        order = sorted(preorder)
        while 0 in order:
            order.remove(0)
        print(order)
        curr = self.find_min(self.rooot)
        print(curr.value)
        while curr != None:
            curr.value = order[0]
            order.pop(0)
            curr = self.succ(curr)

    def asArr(self, x):
        if x != None:
            arr = [x.value]
            arr += self.asArr(x.lson)
            arr += self.asArr(x.rson)
            return arr
        return [0]

    def find_min(self, x):
        print(x.value)
        return self.find_min(x.lson) if x.lson != None else x

    def find_max(self, x):
        return self.find_max(x.rson) if x.rson != None else x

    def succ(self, x):
        if x == self.find_max(self.root()):
            return None
        if x.rson != None:
            print("rson search")
            return self.find_min(x.rson)
        else:
            while x.parent.lson != x:
                x = x.parent
            return x.parent

    def root(self):
        return self.rooot

    def parent(self, x):
        return x.parent

    def left(self, x):
        return x.lson

    def right(self, x):
        return x.rson

    def key(self, x):
        return x.value

