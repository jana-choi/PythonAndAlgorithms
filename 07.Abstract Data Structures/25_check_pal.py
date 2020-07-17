from linkedlistFIFO import LinkedListFIFO
from node import Node

def isPal(l1):
    if len(l1) < 2:
        return True
    if l1[0] != l1[-1]:
        return False
    return isPal(l1[1:-1])

def checkllPal(ll):
    node = ll.head
    l = []

    while node is not None:
        l.append(node.value)
        node = node.pointer
    
    return isPal(l)

def test_checkllPal():
    ll = LinkedListFIFO()
    l1 = [1, 2, 3, 2, 1]
    for i in l1:
        ll.addNode(i)
    print(checkllPal(ll))

    ll.addNode(2)
    ll.addNode(3)
    print(checkllPal(ll))


if __name__ == "__main__":
    test_checkllPal()