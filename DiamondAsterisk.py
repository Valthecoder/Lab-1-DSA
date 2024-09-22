# Define Function
def create_diamond():
    # Try and Except block for passing an even number and if the input is not number
    try:
        n = int(input("Type an odd number: "))
        # If else for not an odd number
        if n % 2 == 0:
            print("Please input a positive odd number.")
            return 

        # For Upper part of the Diamond Asterisk
        for i in range(n // 2 + 1):
            print(' ' * (n // 2 - i) + '*' * (2 * i + 1))
        
        # For Lower part of the Diamond Asterisk
        for i in range(n // 2 - 1, -1, -1):
            print(' ' * (n // 2 - i) + '*' * (2 * i + 1))
    # Except block
    except ValueError:
        print("Please input a valid number.") 

# Call the function
create_diamond()
