# age=int(input("enter ur age:"))

# if age>=18:
#     print("You are eligible")
# else:
#     print("You are not eligible")

# number = int(input("enter a number:"))
# if number % 2 == 0:
#     print("The number is even")
# else:
#     print("The number is odd")

# number = int(input("enter a number:"))
# if number > 0:
#     print("The number is positive")
# else:
#     print("The number is negative")

# balance = 5000
# amount = int(input("enter the amount to withdraw:"))
# if amount <= balance:
#     balance -= amount
#     print("Withdrawal successful.Remaining balance:", balance)
# else:
#     print("Insufficient balance.")

# name = input("enter your name: ")
# print("my name is", name)
# age = int(input("enter your age:"))

# test_result =input("are you completed driving test? (yes/no):")

# if age >=18 and test_result == "yes":
#     print("You are eligible for a driving license")
# else:
#     print("You are not eligible for a driving license")

# number = int(input("enter a number:"))


# if number > 0 :
#     print("the number is positive")
# elif number == 0:
#     print("the number is neutral")
# else:
#     print("it is negative")

# name = input('enter your name: ')
# print("my name is: ",name)
# mark=int(input("enter your mark:"))
# if mark >100:
#     print("invalid mark")
# elif mark >=90 : 
#     print("congratulations! you got A grade")
# elif mark >= 80:
#     print("congratulation! you got B grade")
# elif mark >= 70 :
#     print("good try! you got C+ grade")
# elif mark >= 50 :
#     print("you want to try your best! you got C grade")
# else:
#     print("sorry! bloody bitch. you fail")

# registered = input("are you registered(yes/no):")
# username = "arshad"
# password = "arshadachu"

# if registered == "yes":
#     u_name = input("enter your username: ") 
#     u_pass = input("enter your password: ")

#     if u_name == username and u_pass == password:
#         print("login sucessfull...")
#     elif u_name != username and u_pass != password:
#         print("invalid credential")
#     elif u_name != username :
#         print("invalid username")
#     else: 
#         print('your password is unavailable')
# else:
#     print("you need to register")
    
# result = input("Are you completed 10th (yes / no): ")

# if result == "yes":
#     print("You are eligible for higher studies!!")
    
#     plustwo = input("Are you completed you higher stuies(yes / no ): ")
    
#     if plustwo == "yes":
#         print("you are eligible of UG studies")
#         ug = input("Are you completed UG (yes / no)")
        
#         if ug == "yes":
#             print("you are eligible for PG studies")
#         else:
#             print("you are not eligible of PG studies")
#     else:
#         print("not eligible for UG studies")
         
# else: 
#     print("first complete your 10th idiot!!")


day=int(input("enter a number between 1-7:"))

match day:
    case 1:
        print("its mon")
    case 2:
        print("its Tue")
    case 3:
        print("its wed")
    case 4:
        print("its thu")
    case 5:
        print("its fri")
    case 6:
        print("its sat")
    case 7:
        print("its sun")
    case __:
        print("invalid input")
    