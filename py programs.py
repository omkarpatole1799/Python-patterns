myArr = [1,2,3,4,5,6,7,8,9]


# odd even number in array
# for i in myArr:
#     if (i%2==0):
#         print("even", i)
#     elif (i%2!=0):
#         print("odd", i)

#prime numbers
# a number is prime when it has no other factor other than itself and 1
# prime number is greater then 1 always
# (2, num) -- native implementation (check all the number upto the given number)
# (2,num // 2+1) -- floor division 
# (2, int(num ** 0.5) + 1) -- square root
number = 5

def checkPrime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0: 
                return False
        return True
    return False

# print(checkPrime(number))

#fibonachi squence
# start with 0, 1
# and other number is addition of previous two numbers

#method 1 with recursion
def fibonacci(num):
    if num in {0,1}:    
        return num
    else:
        return fibonacci(num-1)+fibonacci(num-2)

# print([fibonacci(num) for num in range(50)])


def fib_seq(num):
    a = 0
    b = 1
    if(num == 1 or num == 0):
        print(a)
    else: 
        print(a)
        print(b)
        for i in range(2,num):
            c = a+b
            a = b
            b = c
            print(c)
# fib_seq(101)

fib_arr = []

def fibonacci_arr(n):
    if( n > 0):
        a = 0
        b = 1
        if(n == 0 or n == 1):
            fib_arr.append(a)
        else: 
            fib_arr.append(a)
            fib_arr.append(b)
            for i in range(2, n):
                c = a+b
                a = b
                b = c
                fib_arr.append(c)
    else: 
        return fib_arr.append('number should be greater than 0')
fibonacci_arr(10)
print(fib_arr)


# 12321
# def myFun(n):
#     start = 1
#     end = n
#     while start <= end:
#         print(start, end="")
#         start += 1
#         if(start == end):
#             while end-1 >= 0:
#                 print(end, end="")
#                 end -= 1
# myFun(3)