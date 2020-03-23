# Stack Inventory
# Evan Johanns

from LinkedListTail import LinkedList


class Stack:

    def __init__(self):
        myList = LinkedList()

    def push(self,data):
        self.myList.add_head(data)

    def pop(self):
        return self.myList.remove_head
