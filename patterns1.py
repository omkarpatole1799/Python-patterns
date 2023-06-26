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
print("--------------")


'''
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
'''
def pat8(n):
    n = 7
    for i in range(0,7):
        for j in range(0,7):
            if(i == 0 or j == 0 or i == (n-1) or j == (n-1)):
                print("4", end=" ")
            elif( i == 1 or j == 1 or i == (n-2) or j == (n-2)):
                print("3", end=" ")
            elif( i == 2 or j == 2 or i == (n-3) or j == (n-3)):
                print("2", end=" ")
            else: 
                print("1", end=" ")
        print()

pat8(n)
print("--------------")


'''
    *
   * *
  * * *
 * * * *
* * * * *
'''
def pat9(n):
    for i in range(1,n+1):
        # space
        for j in range(0, n-i):
            print(" ", end="")
        #star
        for j in range(0, i):
            print("*", end=" ")
        #space
        # for j in range(0, n-i):
        #     print(" ", end=" ")
        print()
    
pat9(n)
print("--------------")


'''         1
          2 1 2
        3 2 1 2 3
      4 3 2 1 2 3 4
    5 4 3 2 1 2 3 4 5
'''
def pat10(n):
    for row in range(1, n+1):
    # space
        for j in range(0, n-row, +1):
            print(" ", end=" ")
        # number
        for j in range(row, 0, -1):
            print(j , end=" ")
        for j in range(2, row+1, +1):
            print(j , end=" ")
        print()

pat10(n)
print("--------------")

'''
*
**
***
****
*****
****
***
**
*
'''

def pat11(n):
    for i in range(1, 2*n):
        totalCols = (2 * n - i) if (n < i) else (i)
        for j in range(0, totalCols):
          print("*", end="")
        print()
pat11(n) 
print("--------------")
    
'''
         *
        **
       ***
      ****
     *****
'''
def pat12(n):
    for row in range(1, n+1):
        #space
        for j in range(0, n - row, 1):
            print(" ", end="")
        #star
        for j in range(0, row):
            print("*", end="")
        print()
pat12(n)

print("--------------")

'''
     *****
      ****
       ***
        **
         *
'''
def pat13(n):
    for row in range(1, n+1):
        # space
        for j in range(1, row):
            print(" ", end="")
        # star
        for j in range(0, n - row + 1):
            print("*", end="")
        print()
pat13(n)
print("--------------")

'''
        *
       ***
      *****
     *******
    *********
'''

def pat14(n):
    for row in range( 1, n+1):
        # space
        for j in range(0, n-row):
            print(" ", end="")
        #star
        for j in range(0, 2*row - 1):
            print("*", end="")
        print()
pat14(n)

print("--------------")

'''
    *********
     *******
      *****
       ***
        *
'''
def pat15(n):

    for row in range(1, n+1):
        #space
        for space in range(1, row):
            print(" ", end="")
        # star
        for star in range(0, 2*n-(2*row - 1)):
            print("*", end="")
        print()

pat15(n)
print("--------------")

'''
   1
  212
 32123
4321234
 32123
  212
   1   
'''
def pat16(n):
    n = 4
    for row in range(1, 2*n):
        totalCols = (2 * n - row) if(row > n) else(row)
        # space
        for space in range(0, n-totalCols):
            print(" ", end="")
        # cols
        for col in range(totalCols, 0, -1):
            print(col, end="")
        for col in range(2, totalCols+1, +1):
            print(col, end="")
        print()


pat16(n)
print("--------------")

'''
         *
        * *
       * * *
      * * * *
     * * * * *
      * * * *
       * * *
        * *
         *
'''
def pat17(n):
    for row in range(1, 2*n):
        totalCols = (2 * n - row) if (row > n) else (row)
        # space
        for space in range(0, n - totalCols):
            print(' ', end="")
        # cols
        for col in range(0, totalCols):
            print("*", end=" ")
        print()
pat17(n)

print("--------------")

'''
4 4 4 4 4 4 4  
4 3 3 3 3 3 4   
4 3 2 2 2 3 4   
4 3 2 1 2 3 4   
4 3 2 2 2 3 4   
4 3 3 3 3 3 4   
4 4 4 4 4 4 4  
'''

def pat18(n):
    n = 4
    for row in range(1, 2*n):
        for col in range(1, 2*n):
            row, col = row, col
            if(col > n):
                col = 2 * n - col
            if(row > n):
                row = 2 * n - row
            print(n - min (row, col) +1, end="")
        print()
pat18(n)

print("--------------")
