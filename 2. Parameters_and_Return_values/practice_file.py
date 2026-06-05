# first step
def calculate_tax (amount, tax_rate= 0.18):
    total = amount + (amount * tax_rate)
    return total

calculate_1 = calculate_tax(2500)
print(calculate_1)
calculate_2 = calculate_tax(2500, tax_rate= 0.05)
print(calculate_2)

# second step
def is_valid_email(email):
    if "@" in email:
        return(True)
    else:
        return(False)

user_email1 = is_valid_email("pritampur@gmail.com")
print(user_email1)
user_email2 = is_valid_email("pritampurgmail.com")
print(user_email2)

# third step


# forth step
def add(a, b):
    return(a + b)

result = add(5, 5) * 2
print(result)

# forth step
def format_log(level, message, timestamp="12:00"):
    return f"Result is {level}, and {message}, timestamp is {timestamp}"

# Positional
print(format_log("ERROR", "Server Down"))

# Keyword
print(format_log("WARNING", "DB Connection Lost", timestamp="14:00"))

