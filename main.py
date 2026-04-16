def main():
    """
    Main function
    """
    pass


def readData():
    """
    Function reads data from a text file and returns the values as floats in a
    2D list.
    :return: 2D list of floats
    """
    # Set placeholder for data matrix
    data = []
    with open("data.txt", "r") as infile:
        # Get raw string for first line
        raw_line = infile.readline()
        # Iterate as long as a string line exists
        while raw_line != "":
            # Convert string to list by removing \n and splitting at the comma
            raw_list = raw_line.rstrip().split(",")
            data_line = []

            # Iterate over list of strings
            for element in raw_list:
                # Cast data value to a float
                data_line.append(float(element))

            # Append list of float data values to data matrix
            data.append(data_line)

            # Read the next string line
            raw_line = infile.readline()

    # Return completed 2D list for data matrix
    return data



if __name__ == "__main__":
    main()
