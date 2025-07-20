# ---2D Grid--- (list inside list)
num_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(num_grid[0][0])
        #     ^   ^ 
        #  row  colume
# ---Nested Loops--- (loop inside loop)

for row in num_grid:# this loop passes through every loop in num grid. 
    for col in row:# this loop passes through evrry column in a row from first loop giving a number.
        print(col)

