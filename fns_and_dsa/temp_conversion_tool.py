FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

def convert_to_fahrenheit(celsius):
    result = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return result

user_input = float(input("Enter the temperature to convert: "))

temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if temp == "C":
    converted = convert_to_fahrenheit(user_input)
    print(f"{user_input}°F is {converted}°C")
elif temp == "F":
    converted = convert_to_celsius(user_input)
    print(f"{user_input}°C is {converted}°F")
else:
        print(f"Invalid temperature. Please enter a numeric value.")