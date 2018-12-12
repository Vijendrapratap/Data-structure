"""
This is  a program of hash table data structure. hash table are very efficient for data handling as it store data in key
and value pair and the keys are shorten by hash function.

To-Do
    * insert data in Hash table
    * delete data from Hash table
    * print data


Author :
        Vijendra pratap singh

Email :
        pratap.vijendrasingh96@gmail.com

Date :
        12/12/2018
"""

#creating a Node class for entry of data initializing with key, value, and a pointer
class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


#creating a hashtable class for operations
class HashTable:

    def __init__(self):
        self.capacity = 20                         #setting capacity of array to 20
        self.size = 0
        self.block = [None] * self.capacity        #blocks are the separate index of array holding data

    def hash(self, key):                         #defining a hash method for unique key generation
        hashsum = 0
        hashsum += key%11
        return hashsum


    def insert(self, key, value):               #defining a method for entry of data
        self.size += 1
        index = self.hash(key)
        node = self.block[index]

        if node is None :                              #if node is empty enter our data in that node
            self.block[index] = Node(key, value)
            return

        while node is not None:
            prev = node
            node = node.next
        prev.next = Node(key, value)


    def find(self, key):                            #defining a method to find entered data in our table
        index = self.hash(key)
        node = self.block[index]

        while node is not None and node.key is key:

            if node is None :
                return None
            else :
                return node.value
            node = node.next


    def remove(self, key):                        #defining method for removing data from table
        index = hash(key)
        node = self.block[index]
        while node is not None and node.key is key:
            prev = node
            node = node.next
        if node is None:
            return None
        else:
            self.size -= 1
            result = node.value
            if prev is None :
                node = None
            else :
                prev.next = prev.next.next
            return result

if __name__ == '__main__':

    H = HashTable()

    H.insert(101, 1234567890)
    H.insert(102, 9876543210)
    H.insert(103, 5647389201)
    H.insert(104, 1092837465)
    H.insert(105, 1056928374)

    check = H.find(104)
if check == None:
    print("Data is not present in table")
else:
    print(check)





