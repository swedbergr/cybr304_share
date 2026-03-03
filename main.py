# Define the function below to factor a matrix into A=LU
def factorLU(matrix):
    '''
    Function takes a 2D square list and creates a L and U matrix such that
    A=LU.
    @param matrix: 2D list of numeric data
    @return: 2D list representing L
    @return: 2D list representing U
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
    # Get matrix values
    matrix = get_matrix()

    # Get product
    matrixL, matrixU = factorLU(matrix)

    print(f"{matrix} = {matrixL} * {matrixU}")


if __name__ == "__main__":
    main()
