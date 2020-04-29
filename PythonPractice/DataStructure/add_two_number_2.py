'''
1. Node class with data and next_node as parameter
2. print list : type should be Node
   value = []
   while l:
    value.append(l.item)
   l = l.next
   print("->".join(map(str, value)))

3. Add two list l1 and l2
    -> l1 = 2->5->8
    -> l2 = 5 -> 7-> 10
    -> sum = l1[0] + l2[0]
    -> carry = (sum/10)
    -> l3 = Node(sum%10)

    p1 = l1.next
    p2 = l2.next
    p3 = l3

    while (p1 != None) or (p2 != None):
        sum = carry + (p1.item if p1 else0) + (p2.item if p2 else 0)
        carry = sum/10
        p3.next = Node(sum%10)
        p1 = p1.next if p1 else None
        p2 = p2.next if p2 else None

    if carry > 0:
        p3.next = Node(carry)

    return l3


'''



class Node:
    def __init__(self,  data, nextnode=None):
        self.item = data
        self.next = nextnode


def print_list(l):
    """
    :type l: Node
    :return:
    """
    values = []
    while(l):
        values.append(l.item)
        l = l.next

    print("->".join(map(str, values)))


def add_two_list(l1, l2):
    """
    :type l1: Node
    :type l2: Node
    :rtype: Node
    """
    sum = l1.item + l2.item
    carry = int(sum/10)
    l3 = Node(sum % 10)
    p1 = l1.next
    p2 = l2.next
    p3 = l3

    while(p1 != None or p2 != None):
        #print(f"p1 : {p1.item} , p2 : {p2.item}")
        sum = carry + (p1.item if p1 else 0) + (p2.item if p2 else 0)
        #print("sum:", sum)
        carry = int(sum/10)
        p3.next = Node(sum % 10)
        p3 = p3.next
        p1 = p1.next if p1 else None
        p2 = p2.next if p2 else None
        print("p3:", p3.item, "carry :", carry)

    if carry > 0:
        p3.next = Node(carry)

    return l3



l1 = Node(6, Node(7, Node(8)))
l2 = Node(5, Node(9, Node(6)))

print_list(l1)
print_list(l2)

l3 = add_two_list(l1, l2)
print_list(l3)
