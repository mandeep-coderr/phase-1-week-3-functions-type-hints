def start_launch_sequence():

    print("Engine check complete.")
    print("Initiating countdown...")    # Function
    print("3... 2... 1...")             # def keyword, function name, colon, indented body
    print("LIFT OFF! ")

start_launch_sequence()


def check_balance():
    print("Checking balance....")
    print("Current balance: ₹5000")     # Calling a function — name followed by () executes it
check_balance()
check_balance()
check_balance()
check_balance()
check_balance()

def welcome():
    print("Welcome to Python ")         # Why functions — DRY principle (Don't Repeat Yourself)
    print("Have a nice day ")
welcome()
welcome()
welcome()
welcome()
welcome() 

# Void functions — functions that don't return anything (return None implicitly)
def the_janitor():
    print("Sweeping the floor...")

box_to_hold_item = the_janitor()       # A void function is a function that does not return a value.
print(box_to_hold_item)                # In Python, if we don't write return, Python automatically returns (None)

# 2nd example of void fucntion 
def lockdown_house():
    print("Doors are now locked. ")
    print("Lights are turned off. ")  # many functions exist only to perform an action, not to calculate and return data
security_status = lockdown_house()
print(security_status)

# Docstrings — """explains what function does""" right after def
def play_song():

    """This function loads the audio file and begins playback. """

    print("Playing music.... ")        # Docstrings

play_song()
