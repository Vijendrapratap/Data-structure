"""
This is  a program of singly linked list in which we are creating several nodes and performing different operations
linked list is a type of data structure in which data are stored at random locations in memory but all data are
connected with pointer or we can say that that preceding data have address of next data.

To-Do
    * insert data at starting of list
    * insert data at end of list
    * insert data in between list
    * delete data at starting of list
    * delete data at end of list
    * delete data in between list
    * print data


Author :
        Vijendra pratap singh

Email :
        pratap.vijendrasingh96@gmail.com

Date :
        08/12/2018
"""


class Node:                               #creating a node class that store data and refrence
    def __init__(self,data = None):
        self.data = data
        self.next = None


class LinkedList:                      #creating a class named linked list by which we will perform different operation
    def __init__(self):
        self.head = None            #initially we are taking head empty

    def insertend(self,newnode):     #defining a function that will add newnodes in our list at the end of existing list
        if self.head is None:
            self.head = newnode
        else:
            currnode = self.head         #currnode is a temporary node that is starting from head
            while True:
                if currnode.next is None:
                    break
                currnode = currnode.next         #moving to next node
            currnode.next = newnode

    def islistempty(self):                     #defining a method to check if our list is empty or not
        if self.head is None:
            return True
        else:
            return False


    def inserthead(self, newnode):     #defining a method to add node at the begining of the list
        currnode = self.head
        self.head = newnode
        self.head.next = currnode
        del currnode

    def listlength(self):                  #defining a method to find length of list
        currnode = self.head
        length = 0
        while currnode is not None:
            length += 1
            currnode = currnode.next
        return length


    def insertat(self, newnode, position) :       #defining a method to add node at given position
        currentposition = 0                        #This function taking input of position integer
        tempnode = None
        currnode = self.head

        if position < 0 or position > self.listlength():
            print("Invalid Position")
            return
        if position is 0:
            self.inserthead(newnode)
            return


        while True:

            #when we reach to our position
            if currentposition == position:
                tempnode.next = newnode
                newnode.next = currnode
                break

            #saving currnode into tempnode
            tempnode = currnode

            #moving next node
            currnode = currnode.next
            currentposition += 1


    def delethead(self):                            #defining a method for deletion of starting head of list
        if self.islistempty() is False:
            temphead = self.head
            self.head = self.head.next
            temphead.next = None
        else:
            print("Linked list is Empty")


    def deletend(self):                            #defining a method for deletion of last element from list
        lastnode = self.head
        while lastnode.next is not None:

            previuosnode = lastnode    #saving lastnode data into previousnode
            lastnode = lastnode.next

        if previuosnode:
            previuosnode.next = None


    def deletelist(self, position):                       #defining a method for deletion of node at given position
        if position < 0 or position > self.listlength():
            print("Invalid position for deletion")

        if self.islistempty() is False:
            if position is 0:
                self.delethead()
                return

            tempnode = self.head
            while position - 1 > 0:
                self.head = self.head.next
                position -= 1

            self.head.next = self.head.next.next
            return tempnode



    def printlist(self):                              #defining a method for printing out put
        if self.head is None:
            print("The list is empty")
            return
        currentnode = self.head
        while True:
            if currentnode is None:
                break
            print(currentnode.data)
            currentnode = currentnode.next


#creating objecting of class Linkedlist
linklist = LinkedList()


firstnode = Node("Alfa")
linklist.insertend(firstnode)

secondnode = Node("Beta")
linklist.insertend(secondnode)

thirdnode = Node("Gama")
linklist.inserthead(thirdnode)

forthnode = Node("Delta")
linklist.insertat(forthnode,2)
linklist.printlist()

linklist.deletend()
linklist.printlist()

linklist.deletelist(2)
linklist.printlist()
