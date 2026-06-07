# ARGS
def book_tickets(*names):
    print("🎬 Tickets booked for:")
    for name in names:
        print(f"  - {name}")
    print(f"Total tickets: {len(names)}\n")

book_tickets("Raj", "Simran")
book_tickets("Amit")
book_tickets("Priya", "Kabir", "Zoya", "Farhan")

# Kwargs
def print_profile(**details):
    print("--- Profile ---")
    for every_detail, value in details.items():
        print(f" {every_detail} = {value} ")
    print()

print_profile(Name = "Ravi" , Age = 25 , City = "Delhi")
print_profile(Name = "Pritam" , Age = 21 , City = "Mumbai")
print_profile(Name = "Gurbachan" , Age = 23 , City = "Gujarat")

# Global scope / Local scope
# 🌍 GLOBAL — the bank's public name. Everyone can see this.
bank_name = "State Bank of India"

def manager_room():
    # 🔒 LOCAL — the manager's private vault code.
    vault_code = 9991
    print(f"Manager sees bank name: {bank_name}")
    print(f"Manager knows vault code: {vault_code}")

def customer_area():
    print(f"Customer sees bank name: {bank_name}")
    # print(f"Customer tries vault code: {vault_code}")  # ❌ Would CRASH!

manager_room()
customer_area()

# Global Scope
app_name = "MyApp"

# Local Scope
def login():
    password = "abc123"
    print("Logging in...")
    print(f" App : {app_name}")
    print(f" Password : {password}")
    print()

def dashboard():
    print("Dashboard open...")
    print(f" App : {app_name}")

login()
dashboard()

# Global Keyword - To change the variable of global value
system_mode = "Normal"

def toggle_mode():
    global system_mode
    if system_mode == "Normal":
        system_mode = "Safe"
    else:
        system_mode = "Normal"
    print(f" Current mode : {system_mode}")

def check_mode():
    print(f"  Current mode : {system_mode} ")

check_mode()
toggle_mode()
check_mode()
toggle_mode()
check_mode()
