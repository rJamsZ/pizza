##### Start
##### Variables
size_cost = 0
toppinglist = ["Pepperoni", "Mushroom", "Extra cheese", "sausage", "Onion", "Black olives", "Green pepper", "Fresh garlic", "Tomato", "Fresh basil"]
toppings_price = 0.75
pizzas = {"large":12.00,"medium":7.90,"small":5.50}



#### Functions

def get_pizza_size():
    cost=0.0
    size=""
    size = input("\nSmall- £5.50\nMedium- £7.90\nLarge- £12.00\nWhat size pizza would you like:")
    print(size)

    if size == "small":# if pizza is small store cost in total_cost
        print("chose small") 
        return "small"  
    elif size == "medium":
        return "medium"
    elif size == "large":
        return "large"
    else:
        print("Invalid input")
        get_pizza_size()

def get_topping_list(topping_list_to_display):
    return topping_list_to_display

def display_topping_list(topping_list_to_display):
    '''Function to take a toppings list and display it on the screen'''
    output = ""
    for topping in range(0,len(topping_list_to_display)):
    #print(str(topping))
        output += str(topping)+": "+toppinglist[topping]+"\n"

    return output

def get_toppings():
        
    amount_toppings = int(input("How many toppings would you like? Each topping is 75p"))
    return amount_toppings
    print(amount_toppings*toppings_price)

def get_topping_order():
    user_toppinglist = input("Which of the toppings would you like?")
    return user_toppinglist

def calculate_final_ammount(ammount_toppings,size_cost, toppings_price ):

    return (size_cost+(ammount_toppings*toppings_price))
   
def display_order(size,cost):
    output = "Your {size} Pizza will cost = £{cost:.2f}.\n Thank you for your order!"

    return output.format(size = size, cost = cost)
    


#### Code

while True:
    number_of_toppings_asked_for = 0
    print("\n\nWelcome to the Calder Pizzeria!")

    pizza_size = get_pizza_size()  # get pizza size order

    #print(pizzas[ pizza_size])

    #size_cost = pizzas[pizza_size]
    


    print(get_topping_list(toppinglist))

    print(display_topping_list(get_topping_list(toppinglist)))
    

    number_of_toppings_asked_for = get_toppings()

#    print(calculate_final_ammount(number_of_toppings_asked_for,size_cost,toppings_price))

#    size_cost = calculate_final_ammount(number_of_toppings_asked_for,size_cost,toppings_price)

    user_toppinglist = get_topping_order()
    
    #print(get_pizza_size + user_toppinglist)

    size_cost = calculate_final_ammount(number_of_toppings_asked_for,pizzas[pizza_size],toppings_price)

    print(display_order(pizza_size,size_cost))

