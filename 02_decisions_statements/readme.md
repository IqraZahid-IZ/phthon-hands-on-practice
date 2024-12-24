

# Python Projects: Various Small Programs 🚀

This repository contains several small Python programs that handle common tasks such as login verification, temperature advice, tax calculation, and more. These programs are simple and beginner-friendly, designed to showcase Python's basic concepts like conditionals, user input, and calculations.

---

## Contents 📁

1. **Login System Verification** 🔒
2. **Temperature Advisor** 🌡️
3. **Simple Tax Calculator** 💰
4. **Day of the Week Checker** 📅
5. **Driving Eligibility Checker** 🚗

---

## 1. Login System Verification 🔒

### Objective:
Create a simple login system that checks if the entered username and password match predefined values.

### Steps:
- Prompt the user to input a username.
- Prompt the user to input a password.
- If the entered username and password match the predefined values, print a "Login successful!" message.
- If either the username or password is incorrect, print an "Invalid credentials" message.
### Example

u_name = 'Iqra Zahid'
pas = 'iqra123'
user_name = input("Enter your Full name ")
password = input("Enter your Password ")
if u_name == user_name:
    if pas == password:
        print("Login Successfull ✅")
    else:
        print('Invalid Password ❌')
else:
    print("Invalid credentials ❌")

### Example Output:
```python
Enter your Full name: Iqra Zahid
Enter your Password: iqra123
Login Successfull ✅
```

---

## 2. Temperature Advisor 🌡️

### Objective:
Write a program that suggests actions based on the current temperature.

### Steps:
- Ask the user to input the current temperature.
- If the temperature is above 30°C, suggest staying hydrated.
- If the temperature is between 20°C and 30°C, suggest it's a nice day for a walk.
- If the temperature is below 20°C, suggest wearing a jacket.

### Example
c_temp = int(input("Enter current temperature 🌡️"))
if c_temp >= 30:
    print('stay hydrated 🥵')
elif 20 < c_temp < 30:
    print("it's a nice day for a walk 🌞")
elif c_temp < 20:
    print('❄️wear a jacket 🥶')

### Example Output:
```python
Enter current temperature 🌡️: 35
stay hydrated 🥵
```

---

## 3. Simple Tax Calculator 💰

### Objective:
Calculate the tax rate based on the user's income.

### Steps:
- Ask the user to input their annual income.
- If the income is less than 50,000, the tax rate is 10%.
- If the income is between 50,000 and 100,000, the tax rate is 20%.
- If the income is above 100,000, the tax rate is 30%.
- Display the calculated tax amount.

### Example

annual_income = int(input("Enter your annual income.  💰"))
tax = annual_income*10/100
if annual_income <= 50000:
    print(f"You have to pay tax of 10% on your annual income which is {tax} 🪙")
elif 50000 < annual_income <= 100000:
    print(f"You have to pay tax of 20% on your annual income which is {tax} 💵")
elif annual_income < 100000:
    print(f"You have to pay tax of 30% on your annual income which is {tax} 📈")

### Example Output:
```python
Enter your annual income. 💰: 60000
You have to pay tax of 10% on your annual income which is 6000 🪙
```

---

## 4. Day of the Week Checker 📅

### Objective:
Determine if the day entered by the user is a weekday or a weekend.

### Steps:
- Ask the user to input a day of the week (e.g., "Monday").
- If the day is "Saturday" or "Sunday," print "It's a weekend!"
- If the day is any other day, print "It's a weekday."

### Example

day = input('Input day of a week')
if day == 'saturday':
    print("It's a weekend! 😊")
elif day == 'sunday':
    print("It's a weekend! 😊")
else:
    print("It's a weekday")

### Example Output:
```python
Input day of a week: Saturday
It's a weekend! 😊
```

---

## 5. Driving Eligibility Checker 🚗

### Objective:
Check if a person is eligible to get a driving license based on their age.

### Steps:
- Ask the user to input their age.
- If the age is below 16, print "You are too young to get a driving license."
- If the age is between 16 and 18, print "You need parental consent to get a driving license."
- If the age is 18 or older, print "You are eligible to get a driving license."
### Example

print("Task 5")
age = int(input("Enter your age"))
if age <= 16:
    print('You are too young to get a driving license.')
elif 16 < age > 18:
    print('You need parental consent to get a driving license.')
else:
    print('You are eligible to get a driving license.🚗')

### Example Output:
```python
Enter your age: 17
You need parental consent to get a driving license.
```

---

## How to Run the Programs 🖥️

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/IqraZahid-IZ/python-hands-on-practice.git
   ```

2. Navigate to the directory where you cloned the repository.

3. Run each Python file separately, for example:
   ```bash
   python login_system.py
   python temperature_advisor.py
   ```

---

## Requirements ⚙️

- Python 3.x installed on your machine.

---

## Contributing 🤝

If you would like to contribute to this project, feel free to fork the repository, make changes, and create a pull request.

---

## License 📝

This project is licensed under the MIT License - [.\Licence](LICENSE) 

