"""
This is  a program of unordered linked list in which nodes have two basic attribute one is data and other is pointer or
refrence of next data starting element of linked is called head every search and other operation start from the head of linked list

To-Do
    * insert data in unordered linked list
    * insert data at end of linked list
    * insert data in middle of linked list
    * delete data from end of linked list
    * delete data from any position of linked list
    * print data


Author :
        Vijendra pratap singh

Email :
        pratap.vijendrasingh96@gmail.com

Date :
        12/12/2018
"""

class Node:

    def __init__(self, data, next=None):

        self.data = data
        self.next = next


class LinkedList:


    def __init__(self):

        self.head = None
        self.size = 0


    def append(self,newnode):     #defining a function that will add newnodes in our list at the end of existing list

        if self.head is None:
            self.head = newnode

        else:
            currnode = self.head         #currnode is a temporary node that is starting from head

            while True:
                if currnode.next is None:
                    break

                currnode = currnode.next         #moving to next node
            currnode.next = newnode

    def remove(self, key):

        cur = self.head
        while (cur.next is not None) :

            cur = self.head
            prev = None
            try:
                while cur.data != key:
                    prev = cur
                    cur = cur.next
            except:
                return None
            if cur.data == key:

                if cur == self.head:
                    self.head = cur.next
                else:
                    prev.next = cur.next




    def search(self, x):

        current = self.head

        while current != None:
            current = current.next
            if current.data == x:
                print("found")
                return self.remove(x)
            else:
                print("not found")
                return self.append(x)


    def isempty(self):
        return self.head is None

    def printlist(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next

linklist = LinkedList()

phrase = ["this", "is", "unodered", "linked", "list"]
for i in phrase:
    new = Node(i)
    linklist.append(new)
linklist.printlist()

word1 = Node(input("Enter word you wanna search : "))
new = linklist.search(word1)
linklist.printlist()