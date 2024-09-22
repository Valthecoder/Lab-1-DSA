# Define function
def ohms_law_calculator():
    calc_type = input("What do you want to calculate? (Voltage/Current/Resistance): ").title()

# if, elif and else statements
    if calc_type == "Voltage":
        # try and except block for Value Error
        try:
            current = float(input("Enter the current (in A or amperes): "))
            resistance = float(input("Enter the resistance (in Ω or ohms): "))
            return f"Voltage = {current * resistance:.2f} V"
        except ValueError:
            return "Please enter numbers for current and resistance"

    elif calc_type == "Current":
        try:
            voltage = float(input("Enter the voltage (in V or volts): "))
            resistance = float(input("Enter the resistance (in Ω or ohms): "))
            return f"Current = {voltage / resistance:.2f} A" if resistance != 0 else "Resistance cannot be zero"
        except ValueError:
            return "Please enter numbers for voltage and resistance"

    elif calc_type == "Resistance":
        try:
            voltage = float(input("Enter the voltage (in V or volts): "))
            current = float(input("Enter the current (in A or amperes): "))
            return f"Resistance = {voltage / current:.2f} Ω" if current != 0 else "Current cannot be zero"
        except ValueError:
            return "Please enter numbers for voltage and current"

    else:
        return "Please only type Current, Voltage, or Resistance"

# Call the function
result = ohms_law_calculator()
print(result)
