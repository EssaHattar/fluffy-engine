# Plan on making 3 variations
# 1st bound by a grid, only able to move 1 position
# 2nd bound by grid, being able to move a variety of spaces in 1 direction
# 3rd off grid, moving a variety of lengths at any angle (most likely can mislead to seem that way by just creating
# random plot points)
import random
x = 0
y = 0
cord = (x, y)
cordfolder = []


for i in range(10):
    # append folder to add cord
    cordfolder.append((x, y))

    # Generate a random number sequence to determine direction of change
    direction = random.randint(1, 4)

    # then change cord
    while True:
        # 1 == north, 2== east, 3 == south, 4== west
        if direction == 1:
            x += 1
            break
        elif direction == 2:
            y += 1
            break
        elif direction == 3:
            x -= 1
            break
        elif direction == 4:
            y -= 1
            break
        else:
            print('wtf is this error')

print(cordfolder)

import pygraph
g = pygraph.build_chvatal_graph()
pygraph.is_planar(g)