# ADVENT OF CODE DAY 1 SOLUTION

def main():
    # Set the path to the input for the challenge
    path = './inputs/1.txt'

    # Open the file in read-only mode
    file = open(path, 'r')

    # Grab every line in the file and put it into an array
    input_array = file.readlines()

    # Initialize an incrementor for use when performing each operation
    incrementor = 0

    # Loop through each line, first getting the operator
    # then removing it and performing the operation on the incrementor variable
    for line in input_array:
        if line[0] == "+":
            incrementor += int(line[1:])
        else:
            incrementor -= int(line[1:])

    print("Final result: " + str(incrementor))

main()