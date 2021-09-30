# Free Code Generator
import time

choice = 0

print("------Menu-----")
print(" ")
print("1. Print 'Python code'.")
print("2. Print 'no code'.")
print(" ")
print("------------")

while True:
    try:
        while(choice < 1) or (choice > 2):
            choice = int(input("What is your option? : "))
        break
    except ValueError:
        print("Please choose either '1' or '2'")

if choice == 1:
    print("Python code")
elif choice == 2:
    print("no code")