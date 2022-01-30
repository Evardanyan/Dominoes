col = int(input())
row = int(input())

if col == 1 and  row == 1 or col == 8 and  row == 1 or col == 1 and  row == 8 or col == 8 and row == 8:
    print("3")
elif col == 1 and row > 1 or col == 8 and row > 1 or row == 1 and col > 1 or row == 8 and col > 1:
    print("5")
else:
    print("8")
