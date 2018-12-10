"""
This is  a program of queue in which we have to take input of people at bank counter for withdraw and deposit
enqueue them and dequeue them

To-Do
    * insert data in queue
    * delete data from a queue
    * check size of queue
    * print data


Author :
        Vijendra pratap singh

Email :
        pratap.vijendrasingh96@gmail.com

Date :
        10/12/2018
"""


#creating a class of queue
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):               #defining a method for entry of data
        self.queue.insert(0,val)

    def dequeue(self):                  #defining a method for removal of data
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):                      #checking size of queue
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0


que = Queue()

#testing


print("Enter D for deposit and W for withdrawl after name ")
person1 = input("Enter name : ")
person2 = input("Enter name : ")
person3 = input("Enter name : ")
person4 = input("Enter name : ")


que.enqueue(person1)
que.enqueue(person2)
que.enqueue(person3)
que.enqueue(person4)


print(list(que.queue))
print("Queue is empty", que.is_empty())
print("Size of current queue is :", que.size())

que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()

print(list(que.queue))

