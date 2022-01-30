box_length = int(input())
box_width = int(input())
box_height = int(input())
door_width = int(input())
door_height = int(input())

if box_height > door_height and box_width > door_width and (box_length > door_width or box_length > door_height):
    print("The box cannot be carried")
else:
    print("The box can be carried")
