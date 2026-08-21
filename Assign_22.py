# ==================================================
# Assignment: Break and Continue
# ==================================================

# Print odd numbers from 1 to 20.
# Use continue to skip even numbers.
# Use break to stop the loop when the number reaches 15.

i = 1

while i <= 20:

    # Skip even numbers
    if i % 2 == 0:
        i += 1
        continue

    # Stop the loop when i reaches 15
    if i == 15:
        break

    print(i)
    i += 1