#RECURSION

#iterate through a list and print:
def helper(index, list1):
    print(list1[index])
    if index == len(list1) - 1:
        return
    helper(index + 1, list1)

def iterate(list1):
    helper(0, list1)

#Calculating factorial
def factorial(num):
    #identify base case
    if num == 1:
        return 1
    #identify recursive case
    return num * factorial(num - 1)

def fibonacci(n):
    #identify base case
    if n == 1:
        return 1
    if n == 2:
        return 2
    #identify recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)



