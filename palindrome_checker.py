"""
This is  a program of queue in which we have to check if the entered string is a palindrome or not
palindrome are strings that read same from forward and backward
Example:
    madam its same if we reverse the oder

To-Do
    * insert string from user
    * check if entered string is palindrome or not

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

    def addfront(self,val):               #defining a method for entry of data at front
        self.queue.insert(0,val)

    def addrear(self,val):               #defining a method for entry of data at the end
        self.queue.append(val)

    def removerear(self):                  #defining a method for removal of data
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):                      #checking size of queue
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0

    def palindrome_checker(self, word):    #defining a method for checking palindrome
        word.split()
        rev = ""
        for i in reversed(word):
            self.addfront(i)

        while(len(self.queue) != 0):
            rev = rev + self.removerear()

        if word == rev :
            return True
        else:
            return False


que = Queue()

#taking user input
word = input("Enter a word : ")
check = que.palindrome_checker(word)

if check == False:
    print("The entered string is not palindrome ")
else:
    print("The entered string is palindrome ")