from LinkedList import LinkedNode


class QueueLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self,value):
        new_node = LinkedNode(value, None)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def pop(self):
        if self.head is not None:
            pop_node = self.head
            self.head = pop_node.next
            print (pop_node.value)
        else:
            raise Exception ("Queue is empty")

    def is_empty(self):
        return print(self.head is None)

    def __iter__(self):
        n = self.head
        while n is not None:
            yield n.value
            n = n.next

    def __repr__(self):
        return "Queue :[" + "," .join(map(str,self)) + "]"

if __name__=='__main__':
    q = QueueLinkedList()
    q.is_empty()
    q.append(5)
    q.append(10)
    q.append(15)
    print (q)
