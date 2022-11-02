# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days_left = 90 - int(age)
days = days_left * 365
weeks = days_left * 52
months = days_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left")

