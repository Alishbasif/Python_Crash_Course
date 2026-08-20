# Star Pattern using While Loop

# Initialize the row counter
i = 1

# Outer while loop for rows
while i <= 5:

    # Initialize the star counter
    j = 1

    # Inner while loop for printing stars
    while j <= i:
        print("*", end="")
        j += 1

    # Move to the next line
    print()

    # Move to the next row
    i += 1