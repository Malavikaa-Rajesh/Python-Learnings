# 1
word = "Python"
print(word[0])


# 2
word = "Python"
print(word[5])


# 3
word = "Python"
print(word[-1])


# 4
word = "Programming"
print(word[1])
print(word[3])


# 5
name = "Sreeraj"
print(name[0])
print(name[2])
print(name[-1])


# 6
word = input("Enter a word: ")
print(word[0])


# 7
word = input("Enter a word: ")
print(word[-1])


# 8
text = input("Enter a string: ")
print(text[2])


# 9
text = input("Enter a string: ")
index = int(input("Enter index: "))
print(text[index])


# 10
word = "Python"
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])


# 11
word = "Python"
print(word[:3])


# 12
word = "Python"
print(word[-3:])


# 13
word = "Programming"
print(word[1:4])


# 14
word = "Computer"
print(word[:4])


# 15
word = "Python"
print(word[2:])


# 16
word = "Programming"
print(word[3:7])


# 17
text = input("Enter a string: ")
print(text[:4])


# 18
text = input("Enter a string: ")
print(text[-4:])


# 19
text = input("Enter a string: ")
print(text[1:])


# 20
text = input("Enter a string: ")
print(text[:-1])


# 21
word = "Computer"
print(word[-1])
print(word[-2])
print(word[-3])


# 22
word = "Developer"
print(word[-4:])


# 23
word = "Python"
print(word[-4:])


# 24
text = input("Enter a string: ")
print(text[0])
print(text[-1])


# 25
text = input("Enter a string: ")
print(text[-2])


# 26
text = "ABCDEFGHIJ"
print(text[::2])


# 27
text = "ABCDEFGHIJ"
print(text[1::2])


# 28
text = "Programming"
print(text[::3])


# 29
text = "ABCDEFGHIJKL"
print(text[2::2])


# 30
text = input("Enter a string: ")
print(text[::2])


# 31
text = input("Enter a string: ")
print(text[1::2])


# 32
text = "Python"
print(text[::-1])


# 33
text = "Programming"
print(text[::-1])


# 34
text = input("Enter a string: ")
print(text[::-1])


# 35
text = "ABCDEFGHIJ"
print(text[::-2])


# 36
text = "Programming"
print(text[::-3])


# 37
text = "0123456789"
print(text[9:0:-2])


# 38
text = "ABCDEFGHIJ"
print(text[9::-2])


# 39
text = "Python"
print(text[0:3])


# 40
text = "Python"
print(text[2:])


# 41
text = "Python"
print(text[:4])


# 42
text = "Python"
print(text[-4:-1])


# 43
text = "Python"
print(text[::2])


# 44
text = "Python"
print(text[::-1])


# 45
text = "ABCDEFGHIJ"
print(text[1:8:2])


# 46
text = "ABCDEFGHIJ"
print(text[-2:-9:-2])


# 47
text = "Programming"
print(text[3:10:2])


# 48
text = "Programming"
print(text[::-2])


# 49
word = "Python"
print(word[len(word) - 1])


# 50
text = "Python"
print(text[1:6])


# 51
text = "Python"
print(text[-1:-5:-1])


# 52
text = "Python"
print(text[::1])


# 53
text = "Python"
print(text[::-1])
print(text[::-2])


# 54
text = input("Enter a string: ")
middle = len(text) // 2
print(text[:middle])
print(text[middle:])


# 55
text = input("Enter a string: ")
print(text[0])
print(text[-1])
print(text[:3])
print(text[-3:])


# 56
text = input("Enter a string: ")
result = text[-1] + text[1:-1] + text[0]
print(result)


# 57
text = input("Enter a string: ")
print(text[1:-1])


# 58
text = input("Enter a string: ")
print(text[2:-2])


# 59
text = input("Enter a string: ")
result = text[:3][::-1] + text[3:]
print(result)


# 60
text = input("Enter a string: ")
result = text[:-3] + text[-3:][::-1]
print(result)


# 61
text = input("Enter a string: ")
result = text[::2] + text[1::2]
print(result)


# 62
text = input("Enter a string: ")
middle = len(text) // 2
print(text[middle:])


# 63
text = input("Enter a string: ")
middle = (len(text) - 1) // 2
print(text[middle::-1])


# 64
email = "student@gmail.com"
print(email[:3] + "***" + email[7:])


# 65
username = "sreeraj123"
print(username[:4] + "..." + username[-2:])


# 66
phone = input("Enter 10-digit phone number: ")
print("*" * 6 + phone[-4:])


# 67
filename = "project_report.pdf"
print(filename[-3:])


# 68
path = "documents/python/project.py"
print(path[19:])


# 69
url = input("Enter URL: ")

if len(url) > 20:
    print(url[:20] + "...")
else:
    print(url)


# 70
card = input("Enter 16-digit card number: ")
print("*" * 12 + card[-4:])


# 71
student_id = "STU2026CS045"
print(student_id[3:7])
print(student_id[-3:])


# 73
text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 74
original = input("Enter a string: ")
print(original + original[::-1])


# 75
text = "abcdefghij"
print(text[::2] + text[1::2])


# 76
text = "Python Django Flask"

word1 = text[:6]
word2 = text[7:13]
word3 = text[14:]

print(word3 + " " + word2 + " " + word1)


# 77
text = input("Enter a string: ")
middle = len(text) // 2

if len(text) % 2 == 1:
    print(text[middle])
else:
    print(text[middle - 1:middle + 1])


# 78
text = "Python"
print(text[1:] + text[:1])


# 79
text = "Python"
print(text[-1:] + text[:-1])


# 80
text = input("Enter a string: ")
n = int(input("Enter n: "))

n = n % len(text)

print(text[n:] + text[:n])


# 81
text = input("Enter a string: ")
print(text[::2])


# 82
text = input("Enter a string: ")
print(text[::-2])


# 83
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

if text1[:3] == text2[:3]:
    print("Identical")
else:
    print("Not identical")