class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, data):
        node = Node(data, None)
        if self.head == None:
            self.head = node
            node.next = None
        else:
            node.next = self.head
            self.head = node

    def insertAtEnd(self, data):
        node = Node(data, None)
        if self.head == None:
            self.head = node
            return
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node
            return
    
    def insertValues(self, data_list):
        self.head = None

        for data in data_list:
            self.insertAtEnd(data)
        return
    
    def getLength(self):
        curr = self.head
        size = 0
        while curr != None:
            size = size + 1
            curr = curr.next
        
        return size
    
    def removeAt(self, index):
        if index >= self.getLength() or index < 0:
            print("invalid index")
            return
        
        if self.getLength() == 1:
            self.head.next = None
            self.head = None
        elif self.getLength() > 1:
            curr = self.head
            location = 0

            if index == 0:
                self.head = self.head.next
                return
            else:
                for i in range(self.getLength()):
                    if location == index - 1:
                        curr.next = curr.next.next
                        return
                    else:
                        curr = curr.next
                        location += 1

    def print(self):
        if self.head is None:
            print("empty linked list")
            return
        else:
            curr = self.head
            print("\nstart!")
            while curr != None:
                print(curr.data)
                curr = curr.next

            print("complete!\n")



if __name__ == '__main__':
    li = LinkedList()
    li.insertAtBeginning(5)
    li.insertAtBeginning(89)
    li.insertAtEnd(69)
    li.print()

    li.insertValues([1,2,3])
    li.print()

    print(str(li.getLength()))

    li.removeAt(-1)
    li.removeAt(0)
    li.print()
