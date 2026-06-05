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

# another example of print and return value
def with_print(name):
    print("Hello " + name)

def with_return(name):
    return "Hello " + name

a = with_print("Raj")    # a gets NOTHING (None)
b = with_return("Raj")   # b gets "Hello Raj"

def triple(number):
    return 3 * number

calculate = triple(4)
print(calculate)

# All three concepts together — Positional, Keyword, and Default
def pizza_order(size, topping="Cheese", crust="Thin"):
    message = f"{size} pizza with {topping} on {crust} crust"
    return message


# POSITIONAL: order matters!
order1 = pizza_order("Large", "Pepperoni", "Thick")
print("Order 1:", order1)

# KEYWORD: order does NOT matter!
order2 = pizza_order(topping="Olives", size="Medium", crust="Classic")
print("Order 2:", order2)

# DEFAULT: skip things with a default value!
order3 = pizza_order("Small")           # uses default topping & crust
print("Order 3:", order3)

order4 = pizza_order("Medium", "Mushroom")  # override topping only
print("Order 4:", order4)

# another example of Positional, keyword & defalt
def book_ticket(passenger, seat, meal= "Veg"):
    message = f" Ticket booked for {passenger} , seat {seat} , meal {meal} "
    return message

passenger_1 = book_ticket("Sharan", "28A", "Non Veg")    # Positional
print("Passenger one:" , passenger_1)
passenger_2 = book_ticket(seat = "14H" , passenger = "Harman")     #keyword
print("Passenger two:" , passenger_2)

# Positional Arguments	Order is everything. 1st → 1st box.
# Keyword Arguments	Labels decide. Order doesn't matter.
# Default Parameters	A fallback value if nothing is given.