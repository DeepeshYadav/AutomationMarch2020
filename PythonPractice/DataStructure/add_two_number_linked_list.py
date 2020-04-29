class Node:
    def __init__(self, x, nextnode=None):
        self.val = x
        self.next = nextnode


def print_list(l):
    values = []
    while (l):
        values.append(l.val)
        l = l.next
    print(" -> ".join(map(str, values)))


l1 = Node(9, Node(3, Node(5)))
print_list(l1)