money = int(input())
chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769
if money >= sheep:
    sheep_count = money // sheep
    print(sheep_count, "sheep")
elif sheep > money >= cow:
    cow_count = money // cow
    if cow_count == 1:
        print(cow_count, "cow")
    else:
        print(cow_count, "cows")
elif cow > money >= pig:
    pig_count = money // pig
    if pig_count == 1:
        print(pig_count, "pig")
    else:
        print(pig_count, "pigs")
elif pig > money >= goat:
    goat_count = money // goat
    if goat_count == 1:
        print(goat_count, "goat")
    else:
        print(goat_count, "goats")
elif goat > money >= chicken:
    chicken_count = money // chicken
    if chicken_count == 1:
        print(chicken_count, "chicken")
    else:
        print(chicken_count, "chickens")
else:
    print("None")
