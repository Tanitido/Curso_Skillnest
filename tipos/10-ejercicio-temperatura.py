t = input("ingresa temperatura en °C")
t = float(t)
far = ((t*9/5)+32)
kel = (t+273.15)
mensaje = f"""la temperatura en grados Celcius es {t}°C
la temperatura en grados Fahrenheit es {far}°F
la temperatura en grados Kelvin es {kel}°K"""
print(mensaje)
