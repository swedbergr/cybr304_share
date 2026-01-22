# Define the function below to verify that two matrices are compatible and multiply them together
def multiply(matrix1, matrix2):
    '''
    Matrix takes two 2D lists, verifies their compatibility, multiplies them together
    and then returns the product matrix as a 2D list.
    @param matrix1: 2D list of numeric data
    @param matrix2: 2D list of numeric data
    @return: 2D list of numeric data or alert if not compatible
    '''
    pass    

def get_matrix():
    # Get rows and columns from user
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))

    # Create empty list to store matrix values
    matrix = []

    # Iterate over rows and columns to fill matrix
    for r in range(rows):
        # Create empty list to store each row
        row_list = []
        for c in range(columns):
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
    print("Complete information for the first matrix.")
    matrix1 = get_matrix()

    # Get matrix2 values
    print("Complete information for the second matrix.")
    matrix2 = get_matrix()

    # Get product
    product = multiply(matrix1, matrix2)

    print(product)


if __name__ == "__main__":
    main()