# Get elements of matrix A
A = []
for row in range(1,3):
    single_row = []
    for column in range(1,3):
        # Create elements in a single row in matrix A
        single_row.append(int(input(f"A{row}{column}: ")))

    # Add entire row to matrix A
    A.append(single_row)

# Get elements of vector b
b = []
b.append(int(input("b11: ")))
b.append(int(input("b21: ")))

# TODO
solution = []


# Output solution
print(solution)