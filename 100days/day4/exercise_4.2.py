import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#Get the total number of item in list.
number_item = len(names)

#Generate random numbers between 0 and the last index.
random_choice = random.randint(0, number_item - 1)

#Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + ' is going to buy the meal today.')
