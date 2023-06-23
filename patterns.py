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


for i in range(0, n):
    start = 1
    if(i % 2 == 0):
        start = 1
    else: 
        start = 0
    for i in range(0, i+1):
        print(start, end=" ")
        start = 1- start
    print()



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


#     *
#    **
#   ***
#  ****
# *****
#  ****
#   ***
#    **
#     *
