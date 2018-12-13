"""
This is  a program of ordered linked list, it is called ordered linked list because element addition in linked list in sorted
order new element compare it with rest of element and place in such order

To-Do
    * insert data in ordered linked list
    * delete data from ordered linked list
    * print data


Author :
        Vijendra pratap singh

Email :
        pratap.vijendrasingh96@gmail.com

Date :
        12/12/2018
"""

class Node:
  
    # Constructor to initialize the node object 
    def __init__(self, data): 
        self.data = data 
        self.next = None
  
class OderedLinkedList:
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None

    def islistempty(self):  # defining a method to check if our list is empty or not
        if self.head is None:
            return True
        else:
            return False


    def listlength(self):                  #defining a method to find length of list
        currnode = self.head
        length = 0
        while currnode is not None:
            length += 1
            currnode = currnode.next
        return length

    def sortedinsert(self, new_node):
          
        # Special case for the empty linked list  
        if self.head is None: 
            new_node.next = self.head 
            self.head = new_node 
  
        # Special case for head at end 
        elif self.head.data >= new_node.data: 
            new_node.next = self.head 
            self.head = new_node 
  
        else : 
  
            # Locate the node before the point of insertion 
            current = self.head 
            while(current.next is not None and
                 current.next.data < new_node.data): 
                current = current.next
              
            new_node.next = current.next
            current.next = new_node

    def remove(self, value):

        prev = None
        curr = self.head
        while curr:
            if curr.data == value:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True

            prev = curr
            curr = curr.next

        return False

    def search(self, x):

        current = self.head

        while current != None:

            if current.data == x:
                print("found")
                return self.remove(x)
            else:
                print("not found")
                return self.sortedinsert(x)


            current = current.next

        return False

  
    # Utility function to print the linked LinkedList
    def printList(self): 
        temp = self.head 
        while(temp):
            print(temp.data)
            temp = temp.next
            if temp.next is None:
                break
  
  
# Driver program 
oll = OderedLinkedList()

new_node = Node(5) 
oll.sortedinsert(new_node)

new_node = Node(10) 
oll.sortedinsert(new_node)

new_node = Node(7)
oll.sortedinsert(new_node)

new_node = Node(3) 
oll.sortedinsert(new_node)

new_node = Node(1)
oll.sortedinsert(new_node)

new_node = Node(9)
oll.sortedinsert(new_node)

new_nmb = Node(int(input("Enter a number")))
# oll.search(new_node)

print("Create Linked List")
oll.printList()