#patterns
n = 5
# pat 1
print("--------------")
# 1                 1
# 1 2             2 1
# 1 2 3         3 2 1
# 1 2 3 4     4 3 2 1
# 1 2 3 4 5 5 4 3 2 1
def pat1(n):
    for i in range(1, n+1):
        # number
        for j in range(0,i):
            print(i, end=" ")

        # space
        for j in range(0, 2*n-(2*i)):
            print(" ", end=" ")

        # number
        for j in range(0,i):
            print(i, end=" ")
        print()

pat1(n)
print("--------------")
'''
1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
'''

def pat2(n):
    count = 1
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(count, end=" ")
            count += 1
        print()
pat2(n)
print("--------------")
'''
ABCDE
ABCD
ABC
AB
A
'''
def pat3(n):
    for i in range(0, n):
        char = 65
        for j in range(0, n-i):
            print(chr(char), end="")
            char += 1
        # for j in range(char, char+n-i):
        #     print(chr(char), end="")
        #     char += 1

        print()
pat3(n)
print("--------------")
'''
A
BB
CCC
DDDD
EEEEE
'''
def pat4(n):
    for i in range(0, n):
        char = 65
        for j in range(0,i+1):
            print(chr(char), end="")
            char += 1
        print()
pat4(n)
print("--------------")

'''
**********
****  ****
***    ***
**      **
*        *
*        *
**      **
***    ***
****  ****
**********
'''
def pat5(n):
    # upper 
    for i in range(0,n):
        # star
        for j in range(0,n-i):
            print("*", end="")
        # space
        for j in range(0, 2*i):
            print(" ", end="")
        # star
        for j in range(0, n-i):
            print("*", end="")
        print()
    #lower
    for i in range(0,n):
        #star
        for j in range(0,i+1):
            print("*", end="")
        #space
        for j in range(1, 2*n-(2*i+1)):
            print(" ", end="")
        #star
        for j in range(0, i+1):
            print("*", end="")
        print()
pat5(n)
print("--------------")

'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''

def pat6(n):
    #upper
    for i in range(0,n):
        #star
        for j in range(0,i+1):
            print("*", end="")
        #space
        for j in range(1, 2*n-(2*i+1)):
            print(" ", end="")
        #star   
        for j in range(0, i+1):
            print("*", end="")
        print()

    #lower
    for i in range(1,n):
        #star
        for j in range(0, n-i):
            print("*", end="")
        #space
        for j in range(0, 2*i):
            print(" ", end="")
        #star
        for j in range(0,n-i):
            print("*", end="")
        print()
pat6(n)
print("--------------")

'''
****
*  *
*  *
****
'''

def pat7(n):
    for i in range(0,n):
        for j in range(0,n):
            if(i == 0 or j == 0 or i == (n-1) or j == (n-1)):
                print("*", end="")
            else:
                print(" ", end="")
        print()

pat7(n)