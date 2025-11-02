def isPrime(n):
   for i in range(2, int(n**0.5)+1):#
       if n%i==0:
           return False
       else:
           return True


checkedNumber = int(input("Enter a number: "))
print(isPrime(checkedNumber))