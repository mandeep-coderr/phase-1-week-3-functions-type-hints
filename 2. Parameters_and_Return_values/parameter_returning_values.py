def make_juice(fruit_name):             # Parameters
    return fruit_name + " juice"

result = make_juice("Orange")           # Arguments
print(result) 

# parameters and argument
def greet_user(user_name):
    print(f"Hello there, {user_name}!")

greet_user("Mandeep")

# Positional Arguments
def create_profile(name, age):
    print(f"Profile created for {name}, who is {age} years old.")

create_profile("Mandeep", 23)
print(create_profile)

# Keyword arguments
def create_profile(name, age):
    print(f"Profile created for {name}, who is {age} years old.")

create_profile(age=25, name="Mandeep")

# Default parameters
def greet(name="stranger"):
    print(f"Welcome, {name}!")

greet("Mandeep") 
greet()