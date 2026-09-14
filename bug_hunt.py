count = 1
total = 0

# The while condition was missing a colon (:).
while count <= 5:
    total = total + count

    # The loop must increase count so that it eventually reaches 6 and stops.
    count = count + 1

# total is an integer, so it must be converted to a string before joining it with text.
print("Sum of 1 to 5 is: " + str(total))