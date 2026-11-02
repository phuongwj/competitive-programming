current = input()
next = input()

compass = {
    "N": 0,
    "NE": 1,
    "E": 2,
    "SE": 3,
    "S": 4,
    "SW": 5,
    "W": 6,
    "NW": 7
}

value = compass[next] - compass[current]

degree = 45 * value
if degree < 0:
    degree = abs(degree)
    if degree == 180:
        print("U-turn")
    elif degree == 0:
        print("Keep going straight")
    elif degree > 179:
        degree = 360 - degree
        print("Turn", degree, "degrees starboard")
    elif degree <= 179:
        print("Turn", degree, "degrees port")
else:
    if degree == 180:
        print("U-turn")
    elif degree == 0:
        print("Keep going straight")
    elif degree > 179:
        degree = 360 - degree
        print("Turn", degree, "degrees port")
    elif degree <= 179:
        print("Turn", degree, "degrees starboard")