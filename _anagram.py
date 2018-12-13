"""
This is  a program to print prime numbers in interval of 200 and print those number in 2d array
also find numbers which are anagram in those primne numbers and print those values


To-Do
    * find prime numbers in range
    * append those prime numbers  in 2d array
    *find anagram within those prime numbers
    * print data


Author :
        Vijendra pratap singh

Email :
        pratap.vijendrasingh96@gmail.com

Date :
        13/12/2018
"""

def prime_number():      #defining a function to find prime numbers

    list1 = []         #taking empty list to hold values
    flag = 0
    arr = [[],[[]]]
    list0 = []
    anglst = []

    for iteration_value in range(0, 10):
        min = iteration_value * 100
        max = 100*(iteration_value + 1)
        for number in range(min,max+1):
            if number > 1:
                for i in range(2, number):
                    if number % i == 0:
                        flag = 0
                        break
                    else:
                        flag = 1
                if flag == 1:
                    if number not in list1:
                        list1.append(number)
        # print("Prime number in range ", min, "-", max, "=", list1)
        list0.append(min)
        list0.append(max)

        for i in list1:
           for j in range(list1.index(i)+1, len(list1)):
                new = str(i)
                new1 = str(list1[j])
                if sorted(new) == sorted(new1):
                    anglst.append(new1)
                    anglst.append(new)


#printing out put
        arr[0] = list0
        arr[1][0] = list1
        print(arr)
        list0.clear()
        list1.clear()
        arr[1][0] = anglst
        print(arr)
        anglst.clear()


prime_number()
