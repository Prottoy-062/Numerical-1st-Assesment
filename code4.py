#problem 04: Check if a number is prime using loop.
n=int(input("Enter a number: "))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")
