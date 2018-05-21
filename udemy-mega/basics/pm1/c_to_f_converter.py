def ctof(celcius):
    if celcius < -273.15:
        return "Sorry, Celcius value too low"
    else:
        fahrenheit = celcius * 9/5 + 32
        return fahrenheit

print(ctof(37))
