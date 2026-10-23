for i in range (1,26):
    print(i)

for i in range (20,41):
    print (i)

for i in range (100,79,-1):
    print(i)

for i in range (-10,11):
    print (i)

for i in range(-20,0):
    print(i)

for i in range (30,-1,-1):
    print(i)

for i in range (5,101,5):
    print(i)

for i in range(10,101,10):
    print(i)

for i in range (50,-1,-5):
    print(i)

for i in range (-30,30,3):
    print(i)

for i in range (7,101,7):
    print(i)

for i in range (9,101,9):
    print(i)

for i in range (10,201,10):
    print(i)

for i in range (-50,51,5):
    print(i)

for i in range(200,99,-10):
    print(i)

for i in range (1,101):
    if (i%4==0):
        print(i)

for i in range (1,101):
    if (i%3==0):
        print(i)

for i in range(1,100):
    if i%5==0 and i%7==0:
        print(i)

for i in range (1,51):
    if i%3==0:
        print(i)

for i in range (1,101):
    if i > 10 and i < 50:
        print(i)

for i in range (-20,21):
    if i < 0:
        print(i)

for i in range (-20,21):
    if i > 0:
        print(i)

for i in range (1,101):
    if i % 10==5:
        print(i)

for i in range (1,101):
    if i %10 ==0 and i % 20 !=0:
        print(i)

for i in range (1,101):
    if i ** 2 < 500:
        print(i)

for i in range (1,21):
        print(i **2)

for i in range (1,16):
    print(i ** 3)

sum=0
for i in range (1,21):
    if i%2==0:
        sum +=i
print (sum)
        
sum=0
for i in range (1,31):
    if i%2!=0:
        sum +=i
print (sum)
        
a=0
for i in range (1,11):
    a +=i ** 2
print(a)

a= int (input("Enter a number : "))
for i in range (1,11):
    print(a,"x",i,"=",a*i)


a=int(input("Enter a number : "))
fact=1
for i in range(1,a+1):
    fact*=i
    print(fact)

count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1
print(count)

total = 0
for i in range(1, 101):
    total += i ** 2
print(total)

n = int(input("Enter a number: "))
total = 1
for i in range(1, n + 1):
    total *= i
print(total)

name = "Python"
for i in name:
    print(i)

text = "Programming"
count = 0
for i in text:
    count += 1
print(count)

text = "Hello World"
count = 0
for i in text.lower():
    if i in "aeiou":
        count += 1
print(count)

text = "Python123"
for i in text:
    if i.isdigit():
        print(i)

text = "Hello123World"
for i in text:
    if i.isalpha():
        print(i)

text = "education"
for i in text:
    if i not in "aeiou":
        print(i)

text = "PYTHON"
for i in text:
    print(ord(i))

text = "computer"
for i in text:
    print(i.upper())

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

for i in range(1, 6):
    for j in range(1, 6):
        print(i, end=" ")
    print()

for i in range(1, 6):
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

text = "banana"
count = 0
for i in text:
    if i == "a":
        count += 1
print(count)

nums = [12, 45, 7, 89, 23]
largest = nums[0]

for i in nums:
    if i > largest:
        largest = i

print(largest)

nums = [10, 20, 30, 40, 50]

for i in range(len(nums) - 1, -1, -1):
    print(nums[i])