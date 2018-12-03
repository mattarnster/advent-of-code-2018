# ADVENT OF CODE DAY 1 SOLUTION

import sys

def main():
    # Set the path to the input for the challenge
    path = 'Day1\\input.txt'

    # Open the file in read-only mode
    file = open(path, 'r')

    # Grab every line in the file and put it into an array
    input_array = file.readlines()

    # Initialize an incrementor for use when performing each operation
    incrementor = 0

    # Use a set to hold the historial operation values
    operation_values = set()

    duplicate_found = False

    # Loop through each line, first getting the operator
    # then removing it and performing the operation on the incrementor variable.
    while duplicate_found == False:
        for line in input_array:
            if line[0] == "+":
                incrementor += int(line[1:])
            else:
                incrementor -= int(line[1:])

            # Add the results into the operation_values set if it's not already in there
            # If it is, break and let the user know we found the first duplicate.
            if incrementor in operation_values:
                print("First occurance of duplicate value: " + str(incrementor))
                duplicate_found = True
                break
            else:
                operation_values.add(incrementor)
main()