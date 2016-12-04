
total = 0
remainder = 0
def triangulator(one, two, three):
    global total
    global remainder
    one = int(one)
    two = int(two)
    three = int(three)
    sides1 = one + two
    sides2 = one + three
    sides3 = two + three
    if sides1 > three and sides2 > two and sides3 > one:
        total = total + 1
    else:
        remainder = remainder + 1
# All the triangle numbers have been put in a file. This strips and splits
# them then feeds them in to the traingulator() function.
with open('triangles2.txt') as numberset:
    for line in numberset:
        tlist = [item.strip() for item in line.split(' ')]
# This removes empty list items that were showing up
        tlist = list(filter(None, tlist))
# This sets a variable for each item in the list
        t1, t2, t3 = tlist
        triangulator(t1, t2, t3)
print(total)
print(remainder)
