# ===============================
# CONDITIONAL EXECUTION
# ===============================

marks = int(input("Enter marks: "))

if marks >= 80:
    print("Grade A")
elif marks >= 50:
    print("Pass")
else:
    print("Fail")


# ===============================
# BREAK, CONTINUE, PASS
# ===============================

print("\nBreak / Continue / Pass demo:")

for i in range(5):
    if i == 2:
        continue   # skip 2
    if i == 5:
        break      # stop loop
    print(i)

# pass example
for i in range(3):
    if i == 1:
        pass
    print("Value:", i)


# ===============================
# SIMPLE AI / ML / DL DEMO
# ===============================

print("\nSimple AI decision:")

temperature = int(input("Enter temperature: "))

if temperature > 30:
    print("Hot day")
else:
    print("Normal day")


# ===============================
# NESTED CONDITIONALS
# ===============================

print("\nNested condition:")

age = int(input("Enter age: "))
citizen = True

if age >= 18:
    if citizen:
        print("Eligible to vote")
    else:
        print("Not citizen")
else:
    print("Under age")


# ===============================
# TERNARY CONDITIONAL
# ===============================

print("\nTernary result:")

status = "Adult" if age >= 18 else "Minor"
print(status)


# ===============================
# WHILE LOOP
# ===============================

print("\nWhile loop:")

i = 1
while i <= 5:
    print(i)
    i += 1


# ===============================
# FOR LOOP
# ===============================

print("\nFor loop:")

for i in range(5):
    print(i)


# ===============================
# ENUMERATE
# ===============================

print("\nEnumerate:")

names = ["Ali", "Sara", "John"]

for index, name in enumerate(names):
    print(index, name)


# ===============================
# NESTED LOOPS
# ===============================

print("\nNested loops:")

for i in range(3):
    for j in range(2):
        print(i, j)


# ===============================
# LIST COMPREHENSION
# ===============================

print("\nList comprehension:")

nums = [1, 2, 3, 4, 5]
squares = [x*x for x in nums]
print("Squares:", squares)

evens = [x for x in nums if x % 2 == 0]
print("Evens:", evens)


# ===============================
# ITERABLE
# ===============================

print("\nIterable demo:")

text = "Python"

for ch in text:
    print(ch)


# ===============================
# ITERATOR
# ===============================

print("\nIterator demo:")

numbers = [10, 20, 30]
it = iter(numbers)

print(next(it))
print(next(it))
print(next(it))