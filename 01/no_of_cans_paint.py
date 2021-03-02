# In this challenge we need to check how many cas of paint we need to buy for paiting a wall
def paint_calc(height, width, cover_sq_m):
    cans= round(height*width/cover_sq_m)
    return print(f' required c.a {cans} cans to paint the {height}x{width} wall')
# Write your code above this line

test_h = int(input('Enter the height of wall: '))
test_w = int(input('Enter the width of wall: '))
coverage = 5

paint_calc(height=test_h, width= test_w, cover_sq_m = coverage)