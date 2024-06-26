##### Start
##### Variables
total_cost = 0
toppinglist = ["None","Pepperoni", "Mushroom", "Extra cheese", "sausage", "Onion", "Black olives", "Green pepper", "Fresh garlic", "Tomato", "Fresh basil"]
toppings_price = 0.75
pizzas = {"large":12.00,"medium":7.90,"small":5.50}
delivery_charge = 3.75


#### Functions
def get_pizzas():
    amount_pizzas = int(input("How many pizzas would you like?"))
    return amount_pizzas

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
        
    amount_toppings = float(input("How many toppings would you like? Each topping is 75p"))
    return amount_toppings
    print(amount_toppings*toppings_price)

def get_topping_order():
    user_toppinglist = input("Which of the toppings would you like?")
    return user_toppinglist

def get_delivery():
    
   
    get_delivery = input("Would you like your order to be delivered?")
    print(get_delivery)
    if get_delivery == "yes":
        return True  #return true indicating we would like delivery.
    else:
        return False #return false indicating that we do not need delivery
        
    
def calculate_final_ammount(ammount_toppings,size_cost, toppings_price,add_delivery ):

    final_cost = (size_cost+(ammount_toppings*toppings_price))

    if add_delivery == True:
        final_cost += delivery_charge
        return final_cost
    elif add_delivery == False:
        return final_cost


def calculate_final_toppings_cost(ammount_toppings,toppings_price):
    return (ammount_toppings*toppings_price)

def generate_receipt_file(data_to_save, type_of_file):
    '''generates receipt txt'''
#    if type_of_file == refund
#    write a refund
#    elif  type_of_file == receipt
#    write a receipt
    
    #generate timestamped filename
    #open file (use f = open..."
    #write string
    #close file

    pass
   
def display_order(size,cost):
    final_toppings_ammount = calculate_final_toppings_cost(number_of_toppings_asked_for,toppings_price)
    output = ("*"*49+"\n")

    if delivery_required == False:
        output += "{size} Pizza - £{size_cost:.2f}" +"\n"+user_toppinglist+ "\n{amount_toppings:.0f} toppings - "  +  "£{toppings_price:.2f}" +"\n"+"*"*49+"\n"+ "\ntotal cost = £{cost:.2f}.\n" 

    elif delivery_required == True:
        output += "{size} Pizza - £{size_cost:.2f}" +"\n"+user_toppinglist+ "\n{amount_toppings:.0f} toppings - "  +  "£{toppings_price:.2f}" + "\nDelivery - £{delivery:.2f}" +"\n"+"*"*49+"\n"+ "\ntotal cost = £{cost:.2f}.\n" 
    #+ cost#  + "{amount_toppings} toppings - " # + (float({amount_toppings})*float({toppings_price}))  +"\n"+ user_toppinglist+ " will cost = £{cost:.2f}.\n"
    output += "\n"+"*"*49+"\n Thank you for your order!\n"+ "\n"+"-"*49 + "\n"

    f = open("receipt0001.txt", "a")
    f.write(output.format(size = size, cost = cost, size_cost = pizzas[pizza_size], amount_toppings = number_of_toppings_asked_for, toppings_price =final_toppings_ammount, delivery = delivery_charge ))
    f.close()

    return output.format(size = size, cost = cost , size_cost =  pizzas[pizza_size], amount_toppings = number_of_toppings_asked_for, toppings_price = final_toppings_ammount, delivery = delivery_charge )

    

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

    delivery_required = get_delivery()
    #delivery = delivery_required 
    #print(get_pizza_size + user_toppinglist)
    total_cost = calculate_final_ammount(number_of_toppings_asked_for,pizzas[pizza_size],toppings_price,delivery_required)

    
    print(display_order(pizza_size,total_cost))
