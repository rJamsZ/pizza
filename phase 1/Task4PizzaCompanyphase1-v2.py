##### Start

##### Variables
overall_cost = 0
toppinglist = ["Pepperoni", "Mushroom", "Extra cheese", "sausage", "Onion", "Black olives", "Green pepper", "Fresh garlic", "Tomato", "Fresh basil"]


#### Functons

def get_pizza_size():
    size = input("\nSmall- £5.50\nMedium- £7.90\nLarge- £12.00\nWhat size pizza would you like:")
    print(size)

    if size == "small":# if pizza is small store cost in total_cost
        print("chose small") 
        total_cost = 5.50
        #print(str(total_cost))
    elif size == "medium":
        print("chose medium")
        total_cost = 7.90
        #print(str(total_cost)
    elif size == "large":
        print("chose large")
        total_cost = 12.00
    else:
        print("Invalid input")

    if total_cost != 0:
        print("inside function: "+str(total_cost))
    else:
        print("you can't buy that")    

    return total_cost

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
    pass


#### Code


print("Welcome to the Calder Pizzeria!")

overall_cost = get_pizza_size()

#print("outside function: "+str(overall_cost))



print(get_topping_list(toppinglist))

print(display_topping_list(get_topping_list(toppinglist)))


'''
amount_topping = input("How many toppings would you like?")


chosen_topping = input("please choose a topping: ")

print(toppinglist[int(chosen_topping)])
'''
