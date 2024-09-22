# Define Function
def temperature_converter():
    ask_conv = str(input("What conversion type do you need? (C or F): ")).upper()
    
# Try and Except for Value Error
    try:
        ask_temp = float(input("What is the temperature?: "))

        if ask_conv == 'C':
            converted_tempC = (ask_temp * 9/5) + 32
            print(f"The {ask_temp}°C you've given is converted to {converted_tempC:.2f}°F")
        elif ask_conv == 'F':
            converted_tempF = (ask_temp - 32) * 5/9
            print(f"The {ask_temp}°F you've given is converted to {converted_tempF:.2f}°C")
        else:
            print("Please only type F (for Fahrenheit) or C (for Celsius).")
    
    except ValueError:
        print("Please input a valid number for temperature.")


# Call the function
temperature_converter()
