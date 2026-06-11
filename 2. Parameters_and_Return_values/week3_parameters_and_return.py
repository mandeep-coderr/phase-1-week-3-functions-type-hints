# ============================================================
# Week 3 Tuesday – Parameters and Return Values
# All code written by me during Neural Lock Protocol session
# Date: 2026-06-11
# ============================================================

# 1. While loop recall (from Step 1 – Active Recall correction)
print("=== 1. While loop (1 to 3) ===")
count = 1
while count <= 3:
    print(count)
    count = count + 1
print()

# 2. Function with print (Sub‑part 1 – Parameters)
print("=== 2. double() using print ===")
def double(num):
    print(num * 2)

double(5)
print()

# 3. Function with return (Sub‑part 2 – Return values)
print("=== 3. add() with return ===")
def add(a, b):
    return a + b

total = add(3, 7)
print(total)
print()

# 4. Discount price (Sub‑part 3 – Real backend example)
print("=== 4. discount_price() ===")
def discount_price(original, discount_percent):
    discount_amount = original * discount_percent / 100
    remaining = original - discount_amount
    return remaining

final_price = discount_price(200, 25)
print(final_price)
print()

# 5. Email validator (Step 3 – Line‑by‑line guided coding)
print("=== 5. is_valid_email() ===")
def is_valid_email(email):
    return "@" in email

result = is_valid_email("ms04436@gmail.com")
print(result)
print()

# 6. Fixed calculate_discount (Step 4 – Debugging)
print("=== 6. calculate_discount() fixed ===")
def calculate_discount(price, discount):
    final = price - discount
    return final

print(calculate_discount(100, 25))
print()

# 7. Apply tax (Step 5 – Independent variation)
print("=== 7. apply_tax() ===")
def apply_tax(price, tax_rate):
    tax = price * tax_rate
    total_price = price + tax
    return total_price

total = apply_tax(250, 0.10)
print(total)
print()

# 8. Default parameter – calculate_tax (Task 1)
print("=== 8. calculate_tax() with default parameter ===")
def calculate_tax(amount, tax_rate=0.18):
    tax_amount = amount * tax_rate
    return tax_amount

total_amount = calculate_tax(200)
print(total_amount)
total_amount1 = calculate_tax(200, tax_rate=0.05)
print(total_amount1)
print()

# 9. Positional, keyword, mixed arguments – create_user (Task 2)
print("=== 9. create_user() – positional, keyword, mixed ===")
def create_user(name, role, is_active=True):
    detail = f"user [{name}] is a [{role}] Active status: [{is_active}]"
    return detail

print(create_user("Mandeep", "Python developer", True))
print(create_user(role="Film actor", name="Agent Vinod"))
print(create_user("Harsh", role="cinematographer", is_active=False))
print()

# 10. format_log with default timestamp (Task 3)
print("=== 10. format_log() – default timestamp ===")
def format_log(level, message, timestamp="12:00"):
    return f"[{timestamp}] {level}: {message}"

print(format_log(level="ERROR", message="Disk full"))
print(format_log(level="INFO", message="Backup done", timestamp="14:30"))
print()

# 11. Fixed add() – return instead of print (Task 4 – debugging fix)
print("=== 11. add() fixed with return ===")
def add(a, b):
    return a + b

result = add(5, 5) * 2
print(result)