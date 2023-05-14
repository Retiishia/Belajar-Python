# Latihan Belajar untuk Episode 09 

# Mengkonversi Fahrenheit -> Kelvin
# Mengkonversi Kelvin -> Fahrenheit

print("\nPROGRAM KONVERSI TEMPERATURE FAHRENHEIT TO KELVIN\n")

fahrenheit = float(input('Masukan Suhu dalam Fahrenheit : '))
print("Suhu adalah",fahrenheit, "Fahrenheit")

# Fahrenheit -> Kelvin
kelvin = (fahrenheit - 32) * 5/9 + 273.15
print("Suhu dalam Kelvin adalah ",kelvin, "Kelvin")

print("=========================================")

print("\nPROGRAM KONVERSI TEMPERATURE KELVIN TO FAHRENHEIT\n")

kelvin = float(input('Masukan Suhu dalam Kelvin : '))
print("Suhu adalah",kelvin, "Kelvin")

# Kelvin -> Fahrenheit
fahrenheit = (kelvin - 273.15) * 9/5 + 32
print("Suhu dalam Kelvin adalah ",fahrenheit, "Kelvin")


