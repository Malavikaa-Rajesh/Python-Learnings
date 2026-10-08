# for i in range(1,11):
#     print(i)

# for i in range(10,0,-1):
#     print(i)
    
# for i in range(1,21):
#     print(i)

# for i in range(1,21):
#     if i % 2==0:
#         print(i)

# for i in range(1,21):
#     if i % 2!=0:
#         print(i)

# total=0
# for i in range(1,11):
#     print(i)
#     total=total+i
# print("sum=",total)

# n=int(input("enter n:"))
# for i in range(1,n+1):
#     print(i)

# n=int(input("enter n:"))
# total=0
# for i in range(1,n+1):
#     total=total+i
# print("sum=",total)

# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     print(n, "*", i, "=", n * i)


# # n=int(input("enter a number:"))
# for i in range(1,n+1):
#     print(i,"=",i*i)

# a=int(input("enter a first number:"))
# b=int(input("enter a last number:"))
# for i in range(a,b+1):
#     print(i)


# limit=int(input("enter a number:"))
# i=0
# while i<=limit:
#     if i%2!=0:
#         print(i)
#     i+=1

# limit=int(input("enter a number:"))
# i=0
# total=0
# while i<=limit:
#     total+=i
#     print("total=",total)
    


# total=0
# while True:
#     a=int(input("enter a number:"))
#     if a==0:
#         break 
#     else:
#         total+=a
# print(f'total={total}')

# password = ""
# attempts = 0

# while password != "1234" and attempts < 3:
#     password = input("Enter password: ")
#     attempts = attempts +1
#     if password=="1234":
#         print("Your pin is correct")
#         break
#     else:
#         print("Your pin is incorrect")
# else:
#     print("card is blocked")        

# n=int(input("enter a number:"))
# fact=1
# i=1
# while i<=n:
#    fact=fact*i
#    i+=1
# print("factorial=",fact)


# number = int(input("Enter a number: "))

# total = 0

# while number > 0:
#     digit = number % 10
#     total += digit
#     number //= 10

# print(f"total = {total}")

# number = int(input("Enter a number: "))

# reverse = 0

# while number > 0:
#     digit = number % 10
#     reverse = reverse * 10 + digit
#     number //= 10

# print("Reverse =", reverse)
 

number = int(input("Enter a number: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")