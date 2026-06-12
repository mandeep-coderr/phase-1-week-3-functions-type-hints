# Write one program of code that uses a while loop with a break statement
add = 0
while add < 10:
    print(add)
    if add == 5:
        break
    add = add + 1

count = 5 
while count > 1: 
    print(count) 
    if count == 3: 
        break 
    count = count - 1    

# Part 1
def print_args(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"keyword: {kwargs}")

print_args(4, 5, 8, 9, name="Mandeep", state="Punjab")

print_args(4, 5, 8, 9, 10, 54, 65, 78, Name="Mandeep", State="Punjab", Country="India", Status="Active")

# Part 2


# Part 2
system = "online"   # global

def check():
    print(system)   # can read global
    local_var = 10  # local to this function

check()

# Part 3
lobby_phone = "📞 +1-555-GLOBAL"   # global variable (everyone can see)

def my_room():
    room_key = "🔑 SECRET KEY"      # local variable (only inside this function)
    print(lobby_phone)              # ✅ I can see the lobby phone from my room
    print(room_key)                 # ✅ I can see my room key

my_room()

# Part 4
hotel_name = "Grand Central"

def check_in():
    print(hotel_name)

check_in()

# Part 5

status = "active"
def deactivate():
    global status
    if status == "active":
        status = "inactive"

deactivate()
print(status)

# Part 6
log_level = "INFO"
def log_event(*args, **kwargs):
    global log_level
    if kwargs.get("debug"):
        log_level = "DEBUG"
    print(log_level)
    print(*args)
    print(kwargs)

log_event("Server Started", "Port 8080", debug=True)

# Part 7
global_log = "WARNING"

def set_debug():
    global global_log
    global_log = "DEBUG"

set_debug()
print(global_log)

# Part 8
def sum_all(*args, **kwargs):
    multiplier = kwargs.get("multiplier", 1)
    total = sum(args)
    return total * multiplier

# Call the function
result = sum_all(15, 23, 36, 47, multiplier=2)
print(result)

# Without multiplier (default any value)
result2 = sum_all(11, 65, 87)
print(result2)