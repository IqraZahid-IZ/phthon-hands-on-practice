
# # Task 1
import random
print("Task 1")
while True:
    car = input("what kind of rental car you would like. Enter 'exit' to quit  ")
    if car.lower() == 'exit':
        break
    else:
        print(f'Let me see if I can find you a {car}....\n')
print('-----------------------------------------------')

# # Task 2
while True:
    try:
        people = int(
            input("how many people are in their dinner group \n(Press 0 for Done) "))
        if people == 0:
            break
        elif people > 8:
            print('You’ll have to wait for a table')
            break
        elif 0 < people <= 8:
            print('Your table is ready')
            break
    except ValueError:
        print('Error: Enter a valid number')
        continue
print('-----------------------------------------------')

# Task 3
print("Task 3")
while True:
    ans = input(
        'Do you want to find multiple of 10 Enter "Stop" to quit  '.lower())
    if ans == 'stop':
        break
    else:
        number = int(input('Please Enter a number to find multiple of 10  '))
        remainder = number % 10
        if remainder == 0:
            print('Number is multiple of 10')
            continue
        else:
            print('Entered number is not a multiple of 10')
            continue
print('-----------------------------------------------')

# Task 4
print("Task 4")
while True:
    password = input("Create Password ")
    if len(password) < 8:
        print("Password must be atleast 8 characters long")
        continue
    elif password[0].isalpha():
        print("Password Created")
        break
    else:
        print("Password must not start with a number")
        continue
print('-----------------------------------------------')

# Task 5
print("Task 5")
numbers = int(input('Enter a number to make a triangle '))
i = 1
while i <= numbers:
    for n in range(1, i+1, 1):
        print(n, end=" ")
    i += 1
    print()
print('-----------------------------------------------')

# Task 6
print("Task 6")
random_no = random.randint(1, 10)
while True:
    number = int(input('Enter a number  between 0-10 '))
    if random_no == number:
        print("You guessed the right number")
        break
    elif number > random_no:
        print("Too high")
        continue
    elif number < random_no:
        print("Too low")
        continue
    elif 0 > number > 10:
        print("Entered number is not in range")
        continue
    else:
        print("invalid number")
        continue
print('-----------------------------------------------')

# Task 7
print("Task 7")
choice = input("Do you want to find factorial of a number Press Y to continue ")
while choice == 'y' or choice == "Y":
    number=int(input("Enter a number "))
    factorial=1
    for n in range(1,number+1):
        factorial=n*factorial
    print(f"The factorial of {number} is : {number}!= {factorial}")
    break
print('-----------------------------------------------')





