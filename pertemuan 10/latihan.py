class Stacklist:
  def __init__(self):
    self.stack = []

  def isEmpty(self):
    return len(self.stack) == 0
    
  def push(self, url):
    self.stack.append(url)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

 

  def size(self):
    return len(self.stack)

myStack = Stacklist()

myStack.push('1')
myStack.push('2')
myStack.push('3')

print("Stack: ", myStack.stack)
print("Pop: ", myStack.pop())
print("Stack after Pop: ", myStack.stack)
print("Peek: ", myStack.peek())
print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())

class Node:
    def __init__(self, url):
        self.url = url
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None
        self.count = 0

    def isEmpty(self):
        return self.top is None

    def push(self, url):
        new_node = Node(url)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        popped_node = self.top
        self.top = self.top.next   
        self.count -= 1
        return popped_node.url

    def peek(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.top.url

    def size(self):
        return self.count

    def traverseAndPrint(self):
        current = self.top
        while current:
            print(current.url, end=" -> ")
            current = current.next
        print("None")



myStack = StackLinkedList()   

myStack.push('wattpad')
myStack.push('webtoon')
myStack.push('facebook')

print("LinkedList: ", end="")
myStack.traverseAndPrint()

print("Peek: ", myStack.peek())
print("Pop: ", myStack.pop())

print("LinkedList after Pop: ", end="")
myStack.traverseAndPrint()

print("isEmpty: ", myStack.isEmpty())
print("Size: ", myStack.size())