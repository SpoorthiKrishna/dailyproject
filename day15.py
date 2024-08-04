MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# coins={'qua':0.25,
#     'dime':0.10,
#     'nickel':0.5,
#     'penny':0.01,}
profit=0
def is_resource_sufficient(order_ingredient):
    '''Return True when order can be made,False if ingredients are insufficient '''
    for item in order_ingredient:
        if order_ingredient[item]>=resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coin():
    print("Please insert a coin ")
    total =int(input("how many quarters?: "))*0.25
    total+=int(input("how many dimes?: "))*0.1
    total+=int(input("how many nickels ?: "))*0.05
    total+=int(input("how many pennies?: "))*0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost)
        print(f"here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry,the money is not enough, Money Refunded.")
        return False

def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name}")

# total=[]
# def calculate():
#     print("please insert a coin..")
#     for i in coins:
#         coin = input(print(f"how many {i}"))
#         total_cal=coin*coins[i]
#         total.append(total_cal)

           
    
# def resource():
#     actual_cost=MENU([user_input]["cost"])
#     remain=total-actual_cost
#     if total>actual_cost:
#         return remain
is_on = True
while True:
    user_input=str(input("what would you like (Espresso/latte/cappuccino) : "))
    if user_input=="off":
        is_on=False
    elif user_input=='report':
       print(f'water:{resources["water"]}')
       print(f'milk:{resources["milk"]}')
       print(f'coffee:{resources["coffee"]}')
       print(f'money:{profit}')
    else:
        drink=MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coin()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_input,drink["ingredients"])


