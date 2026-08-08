# doubly linked list implementation of stack

class Node:
    def __init__(self, value = None, next = None, previous = None):
        self.value = value
        self.next = next
        self.previous = previous
        return

class Stack:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        return

    def push(self, value):
        newNode = Node(value, None, None)

        if self.size == 0:
            self.head = newNode
            self.tail = newNode
            self.size += 1
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
            self.size += 1
        return

    def pop(self):
        if self.size == 0:
            print("List is empty!")
            return
        elif self.size == 1:
            value = self.tail.value
            self.head = None
            self.tail = None
            self.size -= 1 
            return value
        else:
            value = self.tail.value
            temp = self.tail.previous
            temp.next = None
            self.tail = temp
            self.size -= 1 
            return value

    def printStack(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.value)
            currentNode = currentNode.next
        return

    def peek(self):
        if self.size == 0:
            print("List is empty!")
            return
        else:
            return self.tail.value

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(6)
    s.push(15)
    s.push(17)
    value = s.pop()

    s.printStack()
    print()
    print(value)
    print(s.peek())


