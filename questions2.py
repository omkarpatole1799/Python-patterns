'''
1. Print the patterns  //  done
2. Fibonacci sequence 
	- upto n numbers
	- addition upto n number 
	- seq in array
3. prime number
 	- upto n numbers
    - addition upto n numbers

4. odd even 
	- addition of odd numbers upto n numbers
	- addition of even numbers upto n numbers
'''

def fib_seq(n):

    if(n >= 0):
        # base numbers
        a = 0
        b = 1
        if(n == 0):
            print(a, end=" ")
        elif(n == 1):
            print(a, end=" ")
            print(b, end=" ")
        else:
            print(a, end=" ")
            print(b, end=" ")
            for i in range(1, n):
                c = a + b
                a = b
                b = c
                print(c, end=" ")

# fib_seq(3)

# fibonacci add upto n number

def fib_add(n):
    sum = 0
    if(n > 0):
        # base value
        a = 0 
        b = 1
        if(n == 0):
           print(a) 
           sum += a
           return sum
        elif(n == 1):
            print(a)
            print(b)
            sum += a + b
            return sum
        else:
            print(a)
            print(b)
            sum += a + b
            for i in range(1,n):
                c = a + b
                a = b
                b = c
                print(c)
                sum += c
            return sum
# print("total sum upto n number is: ", fib_add(5))

# - fib_seq in array

fibArr=[]
def fib_seq(n):
    if (n >= 0):
        a = 0
        b = 1
        if (n == 0):
            fibArr.append(a)
        elif (n == 1):
            fibArr.append(a)
            fibArr.append(b)
        else:
            fibArr.append(a)
            fibArr.append(b)
            for i in range(1, n):
                c = a + b
                a = b
                b = c
                fibArr.append(c)

fib_seq(4300)
print(fibArr)
