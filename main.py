# Get elements of matrix A
A = []
for row in range(1,3):
    single_row = []
    for column in range(1,3):
        # Create elements in a single row in matrix A
        single_row.append(int(input(f"A{row}{column}: ")))

    # Add entire row to matrix A
    A.append(single_row)

# Create 2D lists for X, Lambda, and X inverse
x_regular = [[0,0],[0,0]]
Lambda = [[0,0],[0,0]]
x_inverse = [[0,0],[0,0]]




# YOUR CODE HERE







print(f"{A}={x_regular}{Lambda}{x_inverse}")
