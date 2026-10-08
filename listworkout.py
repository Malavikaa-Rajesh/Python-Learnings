# # 1. Create and Display a List

# students = ["Anu", "Ammu", "Arun", "Rahul", "Meera",
#             "Neha", "Riya", "Akhil", "Vishnu", "Diya"]

# print(students)
# print("Length:", len(students))
# print("First:", students[0])
# print("Last:", students[-1])


# # 2. Mixed-Type List

# my_list = [10, 5.5, "Python", [1, 2, 3]]

# for item in my_list:
#     print(item, type(item))


# 3. List Index Explorer

# numbers = [10, 20, 30, 40, 50, 60, 70, 80]

# print(numbers[0])
# print(numbers[3])
# print(numbers[-1])
# print(numbers[-3])

# print("First index:", 0)
# print("Last index:", len(numbers) - 1)


# 4. Safe Index Check

# numbers = [10, 20, 30, 40, 50]

# index = int(input("Enter index: "))

# if -len(numbers) <= index < len(numbers):
#     print("Element:", numbers[index])
# else:
#     print("Invalid index")


# 5. List Slicing Practice

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# print("First 5:", numbers[:5])
# print("Last 3:", numbers[-3:])
# print("Index 2 to 6:", numbers[2:7])
# print("Reverse:", numbers[::-1])


# 6. Even Numbers from a List

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = []

for n in numbers:
    if n % 2 == 0:
        even.append(n)

print(even)


# # 7. Membership Checker

# numbers = [10, 20, 30, 40, 50]

# value = int(input("Enter a value: "))

# if value in numbers:
#     print("Value found")
# else:
#     print("Value not found")


# # 8. Join Two Lists

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# list3 = list1 + list2

# print("List 1:", list1)
# print("List 2:", list2)
# print("Combined:", list3)


# # 9. Repeat a List

# colors = ["Red", "Blue", "Green"]

# print(colors * 3)


# # 10. Shopping List Update

# shopping = ["Milk", "Bread", "Eggs"]

# shopping.append("Rice")
# print(shopping)

# shopping.insert(1, "Sugar")
# print(shopping)

# shopping.remove("Bread")
# print(shopping)

# item = shopping.pop()
# print("Removed:", item)
# print(shopping)


# # 11. Extend Instead of Repeated Append

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# list1.extend(list2)

# print("Using extend:", list1)

# a = [1, 2]
# b = [3, 4]

# a.append(b)

# print("Using append:", a)


# # 12. Basic List Statistics

# numbers = [10, 5, 20, 15, 30]

# print("Number of elements:", len(numbers))
# print("Minimum:", min(numbers))
# print("Maximum:", max(numbers))
# print("Total:", sum(numbers))
# print("Sorted:", sorted(numbers))


# # 13. Count a Target Value

# numbers = [10, 20, 10, 30, 10, 40]

# target = int(input("Enter target: "))

# print("Count:", numbers.count(target))


# # 14. Find the First Position

# names = ["Anu", "Rahul", "Meera", "Anu"]

# name = input("Enter name: ")

# if name in names:
#     print("First position:", names.index(name))
# else:
#     print("Name not found")


# # 15. Remove All Occurrences

# numbers = [1, 2, 3, 2, 4, 2, 5]

# target = int(input("Enter value to remove: "))

# new_list = []

# for n in numbers:
#     if n != target:
#         new_list.append(n)

# print(new_list)


# # 16. Remove Duplicates While Preserving Order

# numbers = [4, 2, 4, 1, 2, 7, 1]

# new_list = []

# for n in numbers:
#     if n not in new_list:
#         new_list.append(n)

# print(new_list)


# # 17. Second Largest Number

# numbers = [10, 20, 30, 20, 40]

# unique = []

# for n in numbers:
#     if n not in unique:
#         unique.append(n)

# unique.sort()

# if len(unique) >= 2:
#     print("Second largest:", unique[-2])
# else:
#     print("Not enough distinct values")


# # 18. Second Smallest Number

# numbers = [10, 20, 10, 30, 40]

# unique = []

# for n in numbers:
#     if n not in unique:
#         unique.append(n)

# unique.sort()

# if len(unique) >= 2:
#     print("Second smallest:", unique[1])
# else:
#     print("Not enough distinct values")


# # 19. Separate Positive and Negative

# numbers = [10, -5, 20, -8, 0, 15, -2]

# positive = []
# negative = []

# for n in numbers:
#     if n > 0:
#         positive.append(n)
#     elif n < 0:
#         negative.append(n)

# print("Positive:", positive)
# print("Negative:", negative)


# # 20. Move Zeros to the End

# numbers = [0, 1, 0, 3, 12, 0, 5]

# new_list = []

# for n in numbers:
#     if n != 0:
#         new_list.append(n)

# for n in numbers:
#     if n == 0:
#         new_list.append(n)

# print(new_list)


# # 21. Find Common Elements

# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]

# common = []

# for n in list1:
#     if n in list2 and n not in common:
#         common.append(n)

# print(common)


# # 22. Merge Two Sorted Lists

# list1 = [1, 3, 5]
# list2 = [2, 4, 6]

# merged = list1 + list2
# merged.sort()

# print(merged)


# # 23. Reverse Without reverse()

# numbers = [1, 2, 3, 4, 5]

# new_list = numbers[::-1]

# print(new_list)


# # 24. Manual Maximum and Minimum

# numbers = [10, 5, 30, 20, 15]

# largest = numbers[0]
# smallest = numbers[0]

# for n in numbers:
#     if n > largest:
#         largest = n

#     if n < smallest:
#         smallest = n

# print("Largest:", largest)
# print("Smallest:", smallest)


# # 25. Frequency Table

# numbers = [1, 2, 2, 3, 3, 3, 4]

# checked = []

# for n in numbers:
#     if n not in checked:
#         print(n, ":", numbers.count(n))
#         checked.append(n)