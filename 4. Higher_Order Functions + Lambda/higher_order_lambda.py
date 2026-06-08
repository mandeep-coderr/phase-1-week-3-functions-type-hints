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