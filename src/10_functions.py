# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(2))
print(is_even(3))


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def print_even_or_odd(n):
    if n % 2 == 0:
        print('EVEN')
    elif n % 2 != 0:
        print('ODD')

print_even_or_odd(num)

