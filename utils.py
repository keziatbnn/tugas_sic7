def celcius_to_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def celcius_to_kelvin(celcius):
    kelvin = celcius + 273.15
    return kelvin

def fahrenheit_to_celcius(fahrenheit):
    celcius = (fahrenheit - 32) * 5/9
    return celcius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = ((fahrenheit - 32) * 5/9) + 273.15
    return kelvin
  
def kelvin_to_celcius(kelvin):
    celcius = kelvin - 273.15
    return celcius

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = ((kelvin - 273.15) * 9/5) + 32
    return fahrenheit