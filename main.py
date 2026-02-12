# Define the function below to verify that the equation has a solution and solves the equation (if possible)
# You may copy and paste functions from previous assignments to make calls in this function.
def solve(matrix1, matrix2):
    '''
    Function takes two 2D square lists, verifies a solution is possible, and computes the solution
    to the matrix equation that is in the form matrix1 * X = matrix2
    @param matrix1: 2D list of numeric data
    @param matrix2: 2D list of numeric data
    @return: 2D list of numeric data or alert if solution not possible
    '''
    pass    

def get_matrix():
    # Get rows and columns from user
    rows = int(input("Enter the number of rows and columns: "))

    # Create empty list to store matrix values
    matrix = []

    # Iterate over rows and columns to fill matrix
    for r in range(rows):
        # Create empty list to store each row
        row_list = []
        for c in range(rows):
            # Get the value for the matrix position and append it to the row
            value = int(input(f"Enter the value for element {r+1}, {c+1}: "))
            row_list.append(value)
        
        # Append entire row to matrix
        matrix.append(row_list)
    
    # Return matrix
    return matrix

def main():
    '''
    Main function for the program.
    '''
    # Get matrix1 values
    print("Complete information for the coefficient matrix.")
    matrix1 = get_matrix()

    # Get matrix2 values
    print("Complete information for the solution matrix.")
    matrix2 = get_matrix()

    # Display equation
    print(f"{matrix1} * X = {matrix2}")

    # Get product
    solution = solve(matrix1, matrix2)

    print(f"X = {solution}")


if __name__ == "__main__":
    main()
