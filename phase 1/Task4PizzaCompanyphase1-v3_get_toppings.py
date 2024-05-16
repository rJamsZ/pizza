##### Start
##### Variables
size_cost = 0
toppinglist = ["Pepperoni", "Mushroom", "Extra cheese", "sausage", "Onion", "Black olives", "Green pepper", "Fresh garlic", "Tomato", "Fresh basil"]
toppings_price = 0.75

#### Functons

def get_pizza_size():
    cost=0.0
    size=""
    size = input("\nSmall- £5.50\nMedium- £7.90\nLarge- £12.00\nWhat size pizza would you like:")
    print(size)

    if size == "small":# if pizza is small store cost in total_cost
        print("chose small") 
        cost = 5.50
        #print(str(cost))
    elif size == "medium":
        print("chose medium")
        cost = 7.90
        #print(str(cost)
    elif size == "large":
        print("chose large")
        cost = 12.00
    else:
        print("Invalid input")
        get_pizza_size()

#    if cost != 0:
#        print("inside function: "+str(cost))
#    else:
#        print("you can't buy that")    

    return cost

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
        
    amount_toppings = input("How many toppings would you like?\nYou can choose up to 3 from our list")
    if amount_toppings == "0":
        return 0
    elif amount_toppings == "1":
        return 1
    elif amount_toppings == "2":
        return 2
    elif amount_toppings == "3":
        return 3
    else:
        print("Invalid input")
        return get_toppings()



def calculate_final_ammount(ammount_toppings,size_cost, toppings_price ):

    output = "Pizza cost = £{pizza:.2f}.\n Thank you for your order!"

    return output.format(pizza = size_cost+(ammount_toppings*toppings_price))
    #return str(size_cost)+" That will be " + str(size_cost+(ammount_toppings*toppings_price)) + ", Thankyou for your order"
   
    


#### Code

while True:
    number_of_toppings_asked_for = 0
    print("\n\nWelcome to the Calder Pizzeria!")

    size_cost = get_pizza_size()

    print(get_topping_list(toppinglist))

    print(display_topping_list(get_topping_list(toppinglist)))

    number_of_toppings_asked_for = get_toppings()

    
    print(calculate_final_ammount(number_of_toppings_asked_for,size_cost,toppings_price))

