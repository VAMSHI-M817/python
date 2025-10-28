class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

    def traversal(self):
        if not self.head:
            print("Nodes not available in SLL")
        else:
            temp = self.head
            while temp is not None:
                print(temp.value)
                temp = temp.next
            print()


Sll = SingleLinkedList()

n1 = Sll.append(10)
n2 = Sll.append(11)
n3 = Sll.append(12)


print(Sll.traversal())
