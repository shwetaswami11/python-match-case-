# 1 Check a number

n = int(input("Enter a number : "))
match n:
    case 1:
        print("one")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other Number")

# 2 Day of the week

day = int(input("Enter day number : "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day")

# 3 Arithmetic operations

a = 10
b = 8
op = input("Enter operator (+, -, *, /): ")

match op:
    case "+":
        print("Result =", a + b)
    case "-":
        print("Result =", a - b)
    case "*":
        print("Result =", a * b)
    case"/":
        print("Result=",a / b)
    case _:
        print("Invalid operator")

# 4 Traffic light
  
light = input("Enter traffic light color: ").lower()

match light:
    case "red":
        print("Stop")
    case "yellow":
        print("Wait")
    case "green":
        print("Go")
    case _:
        print("Invalid color")

#  5 Vowel or consonant

ch = input("Enter a letter: ").lower()

match ch:
    case "a" | "e" | "i" | "o" | "u":
        print("Vowel")
    case _:
        print("Consonant or invalid input")

# 6 Check even or odd

n= int(input("Enter a number: "))

match n % 2:
    case 0:
        print("Even number")
    case 1:
        print("Odd number")

# 6 Grade

marks = int(input("Enter your marks : "))

match marks:
    case m if 90 <= m <= 100:
        print("Grade A")
    case m if 75 <= m < 90:
        print("Grade B")
    case m if 60 <= m < 75:
        print("Grade C")
    case m if 35 <= m < 60:
        print("Grade D")
    case m if 0 <= m < 35:
        print("Fail")
    case _:
        print("Invalid marks")

# 7 Login role selection

role = input("Enter your role: ").lower()

match role:
    case "admin":
        print("Full access")
    case "teacher":
        print("Teacher access")
    case "student":
        print("Student access")
    case _:
        print("Unknown role")

# 8 Calculator for squares and cubes

n = int(input("Enter a number: "))
choice = input("Enter square or cube: ").lower()

match choice:
    case "square":
        print("Square =", n ** 2)
    case "cube":
        print("Cube =", n ** 3)
    case _:
        print("Invalid choice")

# 9 Month name

month = int(input("Enter month number : "))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month")

# 10 Check a fruit

fruit = input("Enter a fruit: ").lower()

match fruit:
    case "apple":
        print("Apple is a fruit.")
    case "mango":
        print("Mango is a fruit.")
    case "banana":
        print("Banana is a fruit.")
    case _:
        print("Fruit not listed")