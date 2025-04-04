#this is a program to check whether the given number is primenumber or not.
number=int(input("enter the values of number="))
i=1
while i<=number:
    if number%i==0:
        print("number is prime number")
    else:
        print("number is not a prime number")
i=i+1
