
# Python Programming Tasks

This repository contains a series of Python exercises that demonstrate basic control flow, loops, user input handling, and some fun functionality such as generating random numbers and calculating factorials.

## Table of Contents
1. [Task 1: Rental Car](#task-1-rental-car)
2. [Task 2: Dinner Group](#task-2-dinner-group)
3. [Task 3: Multiples of 10](#task-3-multiples-of-10)
4. [Task 4: Password Creation](#task-4-password-creation)
5. [Task 5: Number Triangle](#task-5-number-triangle)
6. [Task 6: Guess the Number](#task-6-guess-the-number)
7. [Task 7: Factorial Calculator](#task-7-factorial-calculator)

## Task 1: Rental Car

This task simulates a rental car service. The user is asked what kind of rental car they would like. The loop continues until the user types 'exit' to quit.

### Example Usage:
```python
Enter the kind of rental car you'd like, or type 'exit' to quit: SUV
Let me see if I can find you a SUV...
```

---

## Task 2: Dinner Group

This task prompts the user to enter the number of people in their dinner group. It checks whether the group is larger than 8 and notifies the user whether they can be seated or need to wait for a table. If the user enters `0`, the program stops.

### Example Usage:
```python
How many people are in the dinner group? (Press 0 for Done): 5
Your table is ready.
```

---

## Task 3: Multiples of 10

This task asks the user to input a number and checks if it's a multiple of 10. The loop continues until the user types "Stop".

### Example Usage:
```python
Do you want to find multiple of 10? Enter "Stop" to quit: no
Please enter a number to find multiples of 10: 20
Number is multiple of 10
```

---

## Task 4: Password Creation

This task asks the user to create a password. The password must be at least 8 characters long and cannot start with a number. If the user does not meet these criteria, they will be asked to try again.

### Example Usage:
```python
Create Password: 12345abc
Password must not start with a number
Create Password: abc12345
Password Created
```

---

## Task 5: Number Triangle

This task prints a number triangle. The user is asked to input a number, and a triangle of numbers is printed, with each row containing one more number than the last.

### Example Usage:
```python
Enter a number to make a triangle: 5
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
```

---

## Task 6: Guess the Number

This task generates a random number between 1 and 10. The user is asked to guess the number, and the program informs them whether their guess is too high, too low, or correct. The user is prompted until they guess the correct number.

### Example Usage:
```python
Enter a number between 0-10: 3
Too low
Enter a number between 0-10: 7
Too high
Enter a number between 0-10: 5
You guessed the right number
```

---

## Task 7: Factorial Calculator

This task allows the user to calculate the factorial of a number. The user inputs a number, and the program computes the factorial (e.g., 5! = 120).

### Example Usage:
```python
Do you want to find the factorial of a number? Press Y to continue: Y
Enter a number: 5
The factorial of 5 is: 5! = 120
```

---

## Requirements

To run this program, you will need Python 3.x installed on your machine. The `random` module is used in Task 6 for random number generation.
