class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node # if no head, then this provides the address of new node to head
        else:
            new_node.next = self.head # this assigns the address of previous 1st element to the new element
            self.head = new_node # this assigns the address of the new element to the head of ll


    def insertAtIndex(self, data, index):
        new_node = Node(data)

        current_node = self.head # iterating value
        position = 0
        if index == position: # if index is 0
            self.insertAtBegin(data)
        else:
            while ((current_node != None) and (position+1 != index)): #this iterates to the node right before the required index
                position += 1
                current_node = current_node.next

            if current_node != None: # this checks if the index is valid and in bounds
                new_node.next = current_node.next
                current_node.next = new_node

            else:
                print("Index not present")



    def insertAtEnd(self, data):

        new_node = Node(data)

        if self.head in None: #checks if the list is empty
            self.head = new_node
            return

        current_node = self.head
        while current_node.next: #iterates to the end of the list
            current_node = current_node.next
        
        current_node.next = new_node


    def removeFirstNode(self):
        if self.head is None:
            return
        
        self.head = self.head.next # changes the address in head to the second element(1st index) in the list


    def removeLastNode(self):
        if self.head is None:
            return
               
        current_node = self.head
        while ((current_node.next).next): #iterates to the 2nd last element of the list
            current_node = current_node.next

        current_node.next = None
    
    def removeAtIndex(self, index):
        if self.head is None:
            return
        
        current_node = self.head # iterating value
        position = 0
        if index == position: # if index is 0 ie 1st element
            self.removeFirstNode()
        else:
            while ((current_node != None) and (position+1 != index)): #this iterates to the node right before the required index
                position += 1
                current_node = current_node.next

            if current_node != None: # this checks if the index is valid and in bounds
                current_node.next = (current_node.next).next # this assigns address of the node after skipping the next node

            else:
                print("Index not present")

    def removeNode(self, data):

        current_node = self.head

        if current_node.data == data: # if the data is of the 1st element(0 index)
            self.removeFirstNode()
            return
        
        while ((current_node is not None) and (current_node.next.data != data)): #iterates to the node before the target node
            current_node = current_node.next

        current_node.next = current_node.next.next #assigns the address of the second node from the selected node thereby skipping the target node
                

    def sizeOfLL(self):
        size = 0
        if self.head:
            current_node = self.head
            while current_node:
                size += 1
                current_node = current_node.next
            return size
        else:
            return 0


    def printLL(self):
        if self.head is None:
            print("Linked list is empty")
            return

        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        print("\n")





if __name__ == '__main__':
    ll = LinkedList()

    ll.insertAtBegin(5)
    ll.insertAtBegin(34)
    ll.insertAtBegin(9343)
    ll.insertAtBegin("Money, its a man")

    ll.printLL()

    # ll.removeFirstNode()
    ll.removeAtIndex(1)
    ll.printLL()
