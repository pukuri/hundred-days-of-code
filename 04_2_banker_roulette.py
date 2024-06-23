import random

names_input = input("Give me everybody's names, separated by a comma. ")
names = names_input.split(",").strip()

num_names = len(names)

random_name = random.randint(0, num_names - 1)
person_who_pay = names[random_name]

print(person_who_pay + " is going to buy the meal today!")