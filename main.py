# main.py - Personal Data Manager

# TODO: Step 1 - Prompt the user to enter their name and age
# Hint: Use input() and store the values in variables

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Your name is ",name," and your age is ",age,".")


# TODO: Step 2 - Ask the user to enter 3 hobbies
# Hint: Use a loop to collect hobbies and store them in a list

hobbies = []
print("Enter 3 of your hobbies:")

for i in range(3):
    hobby = input(f"Hobby {i+1}: ")
    hobbies.append(hobby)


# TODO: Step 3 - Create a dictionary to store the user's name, age, and hobbies
# Hint: Use key-value pairs to organize the data

user_data = {
    "name": name,
    "age": age,
    "hobbies": hobbies
}

# TODO: Step 4 - Display the user's information using formatted strings
# Hint: Use f-strings to format the output

print(f"\nHello, {user_data['name']}! You are {user_data['age']} years old and your hobbies are: {', '.join(user_data['hobbies'])}.")

# TODO: Step 5 - Convert the hobbies list into a set to remove duplicates
# Hint: Use the set() function

unique_hobbies = set(user_data['hobbies'])
print(f"Your unique hobbies are: {unique_hobbies}")

# TODO: Step 6 - Calculate the user's birth year and store it in a tuple with the current year
# Hint: Use subtraction and a tuple to store both years

current_year = 2025
birth_year = current_year - int(age)
years = (birth_year, current_year)
print(f"You were likely born in {years[0]}. Current year is {years[1]}.")

# TODO: Step 7 - Create a function that takes the dictionary and returns a summary string
# Hint: Use string concatenation or f-strings inside the function

def generate_summary(data):
    name = data["name"]
    age = data["age"]
    hobbies = ", ".join(set(data["hobbies"])) 
    return f"{name} is {age} years old and enjoys: {hobbies}."

# TODO: Step 8 - Call the function and print the summary
# Hint: Pass the dictionary to the function and print the result

summary = generate_summary(user_data)
print("\nSummary:")
print(summary)
