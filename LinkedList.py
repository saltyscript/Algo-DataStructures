class LinkedNode:
    def __init__(self, value, tail = None):
        self.value = value
        self.next = tail


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend (self, value):
        new_node = LinkedNode(value , self.head)
        self.head = new_node

    def pop(self):
        if self.head is not None:
            node  = self.head
            self.head = node.next
            print (node.value)
        else:
            raise Exception ("LinkedList is empty")

    def __iter__(self):
        n = self.head
        while n is not None:
            yield n.value
            n = n.next

    def __repr__(self):
        return " LinkedList = [" + "," .join(map(str,self)) + "]"

if __name__ == '__main__':
    a=LinkedList()
    a.prepend(5)
    print(a)
    a. prepend(10)
    print(a)
    a.pop()
    print(a)
    a.pop()
    print(a)
    a.pop()



