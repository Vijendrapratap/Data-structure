"""
This is  a program of stack in which we have to check if the given expression have balanced parenthesis
if a parenthesis is opening it needs to be closed in oder to be balanced


To-Do
    * insert data in stack
    * delete data from a stack
    * check size of stack
    * check the topmost element of stack
    * print data


Author :
        Vijendra pratap singh

Email :
        pratap.vijendrasingh96@gmail.com

Date :
        10/12/2018
"""

#creating a class for stack
class Stack:
    def __init__(self):
        self.stack = []     # initializing an empty list

    def pop(self):           #popping elements from the list
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self,val):                 #adding elements at the end of list
        return self.stack.append(val)

    def peak(self):                       #checking topmost element of the stack
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

    def size(self):                      #checking size of stack
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0


    def check_balance(self, equation) :    #defining a method for checking balance of parenthesis
        equation.split()                     #spliting or string into a list
        for i in equation:

            #if we find the open parenthesis we add it to stack
            if i =="(" or i == "{" or i == "[":
                self.push(i)
                continue

            #if we find close parenthesis  we pop from the stack
            elif i == ")" or i == "}" or i == "]":
                if self.is_empty():
                    return False
                else:
                    self.pop()
        if self.size() != 0:
            return False
        else:
            return True


""" Testing """
strings =  "(5+6)*(7+8)/(4+3)*(5+6)*(7+8)/(4+3)"
stack = Stack()
check = stack.check_balance(strings)
if check == False:
    print("The given expression is not balanced ")
else:
    print("The given expresssion is balanced ")