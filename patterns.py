print("python patterns")

n=5

print("pat 1")
####
####
####
####

for i in range(1,6):
    for j in range(1,6):
        print('#', end=" ")
    print()

print("pat 2")

#
##
###
####

for i in range(1,n+1):
    for j in range(1, i+1):
        print("#", end=" ")
    print()


print("pat 3")

# 1
# 12
# 123
# 1234
# 12345
for i in range(1,n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

print("pat 4")

# 1
# 22
# 333
# 4444
# 55555

for i in range(1,n+1):
    for j in range(1, i+1):
        print(i, end=" ")
    print()

print("pat 5")
#####
####
###
##
#

for i in range(1,n+1):
    for j in range(0, n-i+1):
        print("#", end=" ")
    print()

print("pat 6")
# 12345
# 1234
# 123
# 12
# 1

for i in range(1,n+1):
    for j in range(1, n-i+1):
        print(j, end=" ")
    print()


print("pat 7")

        #
      # # #
    # # # # # 
  # # # # # # #
# # # # # # # # #   

for i in range(0,n):
    for j in range(0, n-i-1):
        print(" ", end="")

    #star
    for j in range(0, 2*i+1):   
        print("*", end="")

    #space
    # for j in range(1,n-i):
    #     print(" ", end="")
    print()


print("pat 8")
#########
 #######
  #####
   ###
    #

for i in range(0,n):
    # space
    for j in range(0,i):
        print(" ", end="")
    # star
    for j in range(0, 2*n-(2*i+1)):
        print("*", end="")
    print()



print("pat 9")
    #
   ###
  #####
 #######
#########
#########
 #######
  #####
   ###
    #


for i in range(0,n):
    #space 
    for j in range(0, n-i-1):
        print(" ", end="")
    #star
    for j in range(0, 2*i+1):
        print("*", end="")
    print()
for i in range(0,n):
    #space
    for j in range(0, i):
        print(" ", end="")
    #star
    for j in range(0, 2*n-(2*i+1)):
        print("*", end="")
    print()


print("pat 10")

#
##
###
####
#####
####
###
##
#

for i in range(1,n):
    for j in range(0, i):
        print("#", end=" ")
    print()
for j in range(0,n):
    for k in range(0, n-j):
        print("#", end=" ")
    print()


print("pat 11")
# 1 
# 0 1 
# 1 0 1
# 0 1 0 1 
# 1 0 1 0 1

def pat11(n):
    for i in range(0, n):
        value = 1
        if(i % 2 == 0):
            value = 1
        else: 
            value = 0
        for i in range(0, i+1):
            print(value, end=" ")
            value = 1- value
        print()
pat11(n)

print("pat 12")

#     *
#    **
#   ***
#  ****
# *****
# *****
#  ****
#   ***
#    **
#     *

for i in range(1,n+1):
    # upper triangle
    for j in range(0,n-i):
        print("", end=" ")
    for j in range(0,i):
        print("*", end="")
    print()
for i in range(1,n+1):
    #lower triangle
    for j in range(1,i):
        print("",end=" ")
    for j in range(0,n-i+1):
        print("*", end="")
    print()
    


print("pat 13")
# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 
# 11 12 13 14 15

def pat13(n):
    count = 0
    for i in range(0,n):
        for j in range(0,i+1):
            count += 1
            print(count, end=" ")
        print()

pat13(n)


print("pat 14")
def pat14(n):
    for i in range(65, n+65):
        for j in range(65, i+1):
            print(chr(j), end="")
        print()

pat14(n)

print("pat 15")
#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *
def pat15(n):
    for i in range(0,n):
        # space
        for j in range(0,n-i-1):
            print(" ", end="")
        # star
        for j in range(0,i+1):
            print("*", end="")
        print()
    for i in range(1,n):
        #space
        for j in range(0,i):
            print(" ", end="")
        #star
        for j in range(0, n-i):
            print("*", end="")
        print()

pat15(n)
