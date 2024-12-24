# Task 1
print("Task 1")
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
print('-----------------------------------------------')

# Task 2
print("Task 2")
c_temp = int(input("Enter current temperature 🌡️"))
if c_temp >= 30:
    print('stay hydrated 🥵')
elif 20 < c_temp < 30:
    print("it's a nice day for a walk 🌞")
elif c_temp < 20:
    print('❄️wear a jacket 🥶')
print('-----------------------------------------------')

# Task 3
print("Task 3")
annual_income = int(input("Enter your annual income.  💰"))
tax = annual_income*10/100
if annual_income <= 50000:
    print(f"You have to pay tax of 10% on your annual income which is {tax} 🪙")
elif 50000 < annual_income <= 100000:
    print(f"You have to pay tax of 20% on your annual income which is {tax} 💵")
elif annual_income < 100000:
    print(f"You have to pay tax of 30% on your annual income which is {tax} 📈")
print('-----------------------------------------------')

# Task 4
print("Task 4")
day = input('Input day of a week')
if day == 'saturday':
    print("It's a weekend!")
elif day == 'sunday':
    print("It's a weekend!")
else:
    print("It's a weekday")
print('-----------------------------------------------')

# Task 5
print("Task 5")
age = int(input("Enter your age"))
if age <= 16:
    print('You are too young to get a driving license.')
elif 16 < age > 18:
    print('You need parental consent to get a driving license.')
else:
    print('You are eligible to get a driving license.')
