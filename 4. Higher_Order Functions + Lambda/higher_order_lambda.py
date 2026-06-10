# Simple Signal Light Controller
def blink(signal_name, timer_func):
    result = timer_func(signal_name)
    return result

slow_rule = lambda name: name + " blinks every 5 seconds"
fast_rule = lambda name: name + " blinks every 2 seconds"

print(blink("Red Light", slow_rule))
print(blink("Yellow Light", fast_rule))
print(blink("Green Light", lambda n: n + " blinks every 10 seconds"))

# Filter olders with differently way
orders = [450, 120, 700, 80, 350, 950]

def filter_orders(order_list, rule):
    result = []
    for amount in order_list:
        if rule(amount):
            result.append(amount)
    return result

def is_expensive(amount):
    return amount > 400

def is_cheap(amount):
    return amount < 200

# Passing named functions
print("Expensive:", filter_orders(orders, is_expensive))
print("Cheap:", filter_orders(orders, is_cheap))

# Passing a lambda (one-line anonymous function)
VIP_orders = filter_orders(orders, lambda x: x > 800)
print("VIP:", VIP_orders)

# Another lambda
mid_orders = filter_orders(orders, lambda x: 200 <= x <= 400)
print("Mid-range:", mid_orders)

# Another Lambda simple Function
# Step 1
def transform_data(data_string, func):
    return func(data_string)

print(transform_data("HELLO WORLD", str.lower))

# Step 2
ips = ["192.168.1.10", "10.0.0.5", "172.16.0.3"]
sorted_ips = sorted(ips, key=lambda x: x[-1])
print(sorted_ips)

# Step 3
apply_vat = lambda price: price * 1.2
print(apply_vat(100))

# TOPIC 1: Functions are First-Class Objects
print("=== 1. First-Class Functions ===")

# Functions can be assigned to variables
def greet(name):
    return f"Hello, {name}"

my_func = greet          # Assign function to variable
print(my_func("Alice"))  # Call via variable

# Functions can be passed as arguments to other functions
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def process_message(msg, func):
    return func(msg)

print(process_message("Hello World", shout))   
print(process_message("Hello World", whisper)) 


# TOPIC 2: Higher-Order Function (custom)
print("\n=== 2. Higher-Order Function ===")

# A function that takes another function as argument
def transform_data(data_string, func):
    """Calls func on data_string and returns result"""
    return func(data_string)

# Passing a built-in function without parentheses
print(transform_data("  PYTHON RULES  ", str.strip))   
print(transform_data("HELLO WORLD", str.lower))        
print(transform_data("hello world", str.upper))

# TOPIC 3: Lambda (Anonymous Function)
print("\n=== 3. Lambda Functions ===")

# Basic lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with multiple parameters
add = lambda a, b: a + b
print(add(3, 7))  # 10

# Lambda as inline expression (no variable)
print((lambda x: x * 3)(10))  # 30

# TOPIC 4: Passing Lambda as Argument
print("\n=== 4. Passing Lambda to Functions ===")

# Using lambda with map() – apply to every element
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # [2, 4, 6, 8]

# Using lambda with filter() – keep elements where condition true
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]

# Using lambda in custom higher-order function
print(transform_data("learning", lambda s: s.capitalize()))  # "Learning"

# TOPIC 5: sorted() with key=lambda
print("\n=== 5. sorted() with key=lambda ===")

# List of IP addresses
ips = ["192.168.1.10", "10.0.0.5", "172.16.0.3"]

# Sort by last character
sorted_by_last_char = sorted(ips, key=lambda x: x[-1])
print(sorted_by_last_char)  # ['192.168.1.10', '172.16.0.3', '10.0.0.5']
# Because last chars: '0', '3', '5' → alphabetical order '0','3','5'

# Sort by length of string
sorted_by_len = sorted(ips, key=lambda x: len(x))
print(sorted_by_len)  # Shortest to longest

# Sort list of dictionaries
users = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}]
sorted_by_age = sorted(users, key=lambda user: user["age"])
print(sorted_by_age)  # Bob first (25), then Alice (30)

# TOPIC 6: Practical Example – Data Pipeline with Lambdas
print("\n=== 6. Practical: Reusable Data Pipeline ===")

def pipeline(data, *functions):
    """Apply multiple functions sequentially to data"""
    result = data
    for func in functions:
        result = func(result)
    return result

# Clean user input using lambdas
clean = pipeline(
    "  User@Example.COM  ",
    lambda s: s.strip(),      # remove spaces
    lambda s: s.lower(),      # lowercase
    lambda s: s.replace("@", "[at]")  # obfuscate email
)
print(clean)  # "user[at]example.com"

# VAT calculator
apply_vat = lambda price: price * 1.2
print(apply_vat(100))  # 120.0

# TOPIC 7: Edge Case – Passing Non-Callable
print("\n=== 7. Edge Case: TypeError ===")

try:
    # Passing a string instead of a function
    transform_data("test", "not_a_function")
except TypeError as e:
    print(f"Caught error: {e}")
    # Output: Caught error: 'str' object is not callable

# 🧠 FORMULA / TEMPLATE FOR YOUR OWN PROJECTS
print("\n=== 🧠 Reusable Formula ===")

# Final demonstration – Your own project example
print("\n=== Your Own Project Example ===")

# Problem: You have a list of product prices. Apply discount (10% off) and then add tax (18%).
prices = [100, 200, 300]

# Using lambda with map
discounted = map(lambda p: p * 0.9, prices)   # 10% off
final_prices = map(lambda p: p * 1.18, discounted)  # add 18% tax
print(list(final_prices))  # [106.2, 212.4, 318.6]

# Same thing in one line (function composition)
final = list(map(lambda p: p * 0.9 * 1.18, prices))
print(final)  # [106.2, 212.4, 318.6]