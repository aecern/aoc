import re

x = 0
y = 0
cardinal = "north"

# Get the entire string of directions from the user
directions = input('Enter in direction string: ')
# Remove "," and spaces from string and create list
dlist = directions.strip().split(","" ")

# Changes the direction facing based on right or left turn
def facing(l):
    global cardinal
    if cardinal == "north":
        if l == "R":
            cardinal = "east"
        else:
            cardinal = "west"
    elif cardinal == "south":
        if l == "R":
            cardinal = "west"
        else:
            cardinal = "east"
    elif cardinal == "west":
        if l == "R":
            cardinal = "north"
        else:
            cardinal = "south"
    elif cardinal == "east":
        if l == "R":
            cardinal = "south"
        else:
            cardinal = "north"
    else:
        print("Boom!")
        # Changes x and y cooordinates based on direction facing
        def block_move(n):
            global cardinal
            global x
            global y
            n = int(n)
            if cardinal == "north":
                y = y + n
            elif cardinal == "south":
                y = y - n
            elif cardinal == "west":
                x = x + n
            elif cardinal == "east":
                x = x - n
            else:
                print("Boom!")

        # Apply facing() and block_move() to each item in the list
        for dir in dlist:
            rightleft = re.sub(r'\d+', '', dir)
            facing(rightleft)
            number = re.sub('[^0-9]','', dir)
            block_move(number)

        answer = abs(x) + abs(y)
        print(answer)
