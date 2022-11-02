# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1.lower() + name2.lower()
comp1 = "true"
comp2 = "love"

count1 = 0
count2 = 0

for i in comp1:
    count1 += name.count(i)
    str(count1)
for i in comp2:
    count2 += name.count(i)
    str(count2)
score = int(str(count1) + str(count2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

