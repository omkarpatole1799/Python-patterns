'''
1. Print the patterns
2. Fibonacci sequence 
	- upto n numbers
	- addition upto n number 
	- the n th number
	
3. prime number
 	- upto n numbers
	- addition upto n numbers
4. odd even 
	- addition of odd numbers upto n numbers
	- addition of even numbers upto n numbers
'''
	
'''
2. Fibonacci sequence 
	- upto n numbers
	- addition upto n number 

'''
# addition upto n number 
def fibAdd(n):
    if (n>=1):
        addition = 0
        a = 0
        b = 1
        if( n==1 or n==0):
            addition += a + b
            print("addition is", addition)
        else:
            addition += a + b
            for i in range(2,n):
                c = a+b
                a = b
                b = c
                addition += c
            print("addition is: ", addition)
fibAdd(3)

# upto n numbers
def fibonacciSeq(n):
    if (n >= 1):
        a = 0
        b = 1
        if(n == 1):
            print(a)
            print(b)
        else: 
            print(a)
            print(b)
            for i in range(2,n):
                c = a+b
                a = b
                b = c
                print(c)
fibonacciSeq(5)