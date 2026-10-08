# i=1
# while i<=10:
#     print(i)

a=int(input('enter a limit: '))

i = 1
while i>=a:
    print(i)
    i += 1
    
n = int(input("Enter a number: "))

fact = 1
i = 1

while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial =", fact)

number = int(input("Enter a number: "))

reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

print("Reverse =", reverse)