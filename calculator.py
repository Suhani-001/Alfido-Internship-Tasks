def fah_to_cel(f):
    return (f-32)*5/9

def fah_to_kel(f):
    return (f-32)*5/9 + 273.15

def kel_to_cel(k):
    return k-273.15

def kel_to_fah(k):
    return (k-273.15)*9/5+32

def cel_to_kel(c):
    return c + 273.15

def cel_to_fah(c):
    return (c*9/5)+32

def temperature_converter():
    print("Temperature converter!")
    print("Available units: Celsius,Fahrenheit,Kelvin")

    from_unit=input("Enter the unit you want to convert from (C,F,K) :").lower()
    to_unit=input("Enter the unit you want to convert into (C,F,K) :").lower()
    value=float(input(f"Enter the temperature in {from_unit}: "))

    if from_unit=="c":
        if to_unit=="f":
            return f"The temperature in Fahrenheit is : {value:.2f}"
        elif to_unit=="k":
            return f"The temperature in Kelvin is : {value:.2f} K"
        elif to_unit=="c":
            return f"The temperature in Celsius is : {value:.2f} C"
        else:
            return "Invalid target unit!"
    elif from_unit=="f":
        if to_unit=="c":
            return f"The temperature in Celsius is : {value:.2f} C"
        elif to_unit=="k":
            return f"The temperature in Kelvin is : {value:.2f} K"
        elif to_unit=="f":
            return f"The temperature in Fahrenheit is : {value:.2f} F"
        else:
            return "Invalid target unit!"
    elif from_unit=="k":
        if to_unit=="c":
            return f"The temperature in Celsius is : {value:.2f} C"
        elif to_unit=="f":
            return f"The temperature in Fahrenheit is : {value:.2f} F"
        elif to_unit=="k":
            return f"The temperature in Kelvin is : {value:.2f} K"
        else:
            return ("Invalid target unit!")
    else:
        return "Invalid input unit!!"

print(temperature_converter())
