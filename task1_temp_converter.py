def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, from_scale, to_scale):
    if from_scale == "Celsius":
        if to_scale == "Fahrenheit":
            return celsius_to_fahrenheit(value)
        elif to_scale == "Kelvin":
            return celsius_to_kelvin(value)
    elif from_scale == "Fahrenheit":
        if to_scale == "Celsius":
            return fahrenheit_to_celsius(value)
        elif to_scale == "Kelvin":
            return fahrenheit_to_kelvin(value)
    elif from_scale == "Kelvin":
        if to_scale == "Celsius":
            return kelvin_to_celsius(value)
        elif to_scale == "Fahrenheit":
            return kelvin_to_fahrenheit(value)

def main():
    print("Temperature Converter")
    value = float(input("Enter the temperature value: "))
    from_scale = input("Enter the scale of the temperature (Celsius, Fahrenheit, Kelvin): ")
    to_scale = input("Enter the scale to convert to (Celsius, Fahrenheit, Kelvin): ")

    converted_value = convert_temperature(value, from_scale.capitalize(), to_scale.capitalize())
    print(f"{value} {from_scale.capitalize()} is equal to {converted_value} {to_scale.capitalize()}.")

if __name__ == "__main__":
    main()
