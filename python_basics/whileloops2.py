# This script repeatedly asks the user for numbers,
# and computes the largest odd number which divides it.
while True:
    value = input("Number: ")
    if (value.lower() == "exit"):
        # Stop asking for numbers.
        break
    value = int(value)
    # While value is even
    while value % 2 == 0:
        value = value / 2
    print("The largest odd factor is:", value)
print("Thank you for using this program. Bye!")