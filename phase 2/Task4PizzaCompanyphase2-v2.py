##### Start
##### Variables
size_cost = 0
toppinglist = ["None", "Pepperoni", "Mushroom", "Extra cheese", "sausage", "Onion", "Black olives", "Green pepper", "Fresh garlic", "Tomato", "Fresh basil"]
toppings_price = 0.75
pizzas = {"large":12.00,"medium":7.90,"small":5.50}

chosen_toppings = {"None":0,"Pepperoni":1, "Mushroom":2, "Extra cheese":3, "sausage":4, "Onion":5, "Black olives":6, "Green pepper":7, "Fresh garlic":8, "Tomato":9, "Fresh basil":10}
'''
dictonary for the topppings in topping lists

0:none
1:pepperoni etc.


ask the user for their choices

store the number in a list.... chosen_toppings[]

'''

#### Functions

def get_pizza_size():
    cost=0.0
    size=""
    size = input("\nSmall- £5.50\nMedium- £7.90\nLarge- £12.00\nWhat size pizza would you like:")
    print(size)

    if size == "small":# if pizza is small store cost in total_cost 
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
    chosen_toppings = input("Which of the toppings would you like?")
    return chosen_toppings 

def display_order(size,cost):
    output="Your size is"+size+". This costs £"+str(cost)

    return output



def calculate_final_ammount(ammount_toppings,size_cost, toppings_price ):

    output = "Pizza cost = £{pizza:.2f}.\n Thank you for your order!"

    return output.format(pizza = size_cost+(ammount_toppings*toppings_price))
    #return str(size_cost)+" That will be " + str(size_cost+(ammount_toppings*toppings_price)) + ", Thankyou for your order"
   
    


#### Code

while True:
    number_of_toppings_asked_for = 0
    print("\n\nWelcome to the Calder Pizzeria!")

    pizzas = get_pizza_size()  # get pizza size order

    #print(pizzas[ pizza_size])

    #size_cost = pizzas[pizza_size]
    


#    print(get_topping_list(toppinglist))

    print(display_topping_list(get_topping_list(toppinglist)))
    

    number_of_toppings_asked_for = get_toppings()

    print(calculate_final_ammount(number_of_toppings_asked_for,size_cost,toppings_price))

    user_toppinglist = get_topping_order()
    
    #print(get_pizza_size + user_toppinglist)

    print(display_order(pizza_size,size_cost))

