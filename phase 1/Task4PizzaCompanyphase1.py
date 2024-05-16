print("Welcome to the Calder Pizzeria!")
total_cost = 0
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
    print(str(total_cost))
else:
    print("you can't buy that")

toppinglist = ["Pepperoni", "Mushroom", "Extra cheese", "sausage", "Onion", "Black olives", "Green pepper", "Fresh garlic", "Tomato", "Fresh basil"]
print(toppinglist)


for topping in range(0,len(toppinglist)):
    #print(str(topping))
    print(str(topping)+": "+toppinglist[topping])

amount_topping = input("How many toppings would you like?")


chosen_topping = input("please choose a topping: ")

print(toppinglist[int(chosen_topping)])
