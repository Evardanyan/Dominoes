menu = input()
pizza = ["Margarita, Four Seasons, Neapoletana, Vegetarian, Spicy"]
salad = ["Caesar salad, Green salad, Tuna salad, Fruit salad"]
soup = ["Chicken soup, Ramen, Tomato soup, Mushroom cream soup"]
if menu == "pizza":
    print(pizza[0])
elif menu == "salad":
    print(salad[0])
elif menu == "soup":
    print(soup[0])
else:
    print("Sorry, we don't have it in the menu")
