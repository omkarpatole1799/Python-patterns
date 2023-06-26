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

'''
3. prime number
 	- upto n numbers
    - addition upto n numbers
    
'''

#list of prime numbers upto n number
primeArr = []
def listPrime(n):
    for num in range(2,n):
        prime = True
        for j in range(2,num):
            if (num % j == 0):
                prime = False
        if prime:
            primeArr.append(num)

# listPrime(101)
# print(primeArr)

#addition of prime numbers upto n number

def addPrime(n):
    sum = 0
    for num in range(2, n):
        prime = True
        for j in range(2, num):
            if (num % j == 0):
                prime = False
        if prime:
            sum += num
    return sum

sum = addPrime(10)
print(sum)

# check if the number is prime or not
def primeNumber(n):
    if(n>1):
        for i in range(2,n):
            if(n % i == 0):
                return False
            return True
        return False

# print(primeNumber(5))



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
# fibAdd(3)

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
            for i in range(1,n):
                c = a+b
                a = b
                b = c
                print(c)
fibonacciSeq(6)
