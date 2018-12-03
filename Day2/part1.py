# ADVENT OF CODE DAY 2 PART 1

from collections import Counter

def main():
    # Set the path to the input for the challenge
    path = 'Day2\\input.txt'

    # Open the file in read-only mode
    file = open(path, 'r')

    # Grab every line in the file and put it into an array
    input_array = file.readlines()

    # Count IDs containing 2 of the same or 3 of the same letter
    # Multiply the count of these together to get the checksum

    # If a string contains 2 of the same and 3 of the same, count it for both
    # If a string contains 2 occurences of 2 of the same, it only counts once
    # Same for strings which contain 2 occurences of 3 of the same.

    two_of_the_same = 0
    three_of_the_same = 0

    for line in input_array:

        letter_count = Counter(line)

        # Store local counts for each "two of a kind" and "three of a kind"
        has_two = 0
        has_three = 0

        for value in letter_count.values():
            if value == 2 and has_two < 1:
                has_two += 1
            elif value == 3 and has_three < 1:
                has_three += 1

        # Add them onto our counts
        two_of_the_same += has_two
        three_of_the_same += has_three


    print(str("Checksum: " + str(two_of_the_same * three_of_the_same)))

main()