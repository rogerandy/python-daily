# Print the menu and get the user's choice
user = input("What do you like: 'espresso', 'latte', or 'cappuccino'? ").lower()

# Define the menu dictionary
menu = {
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
            "coffee": 26,
        },
        "cost": 2.6,
    }
}

# Define a function to get the details of the selected item
def get_item_details(choice):
    if choice in menu:
        return menu[choice]["ingredients"]
    else:
        return None

# Call the function and print the result
item_details = get_item_details(user)
if item_details:
    print(f"Ingredients for {user}: {item_details}")
else:
    print("Something is wrong. Please choose from the menu.")
