base = float(input("Inserisci la base del triangolo: "))
altezza = float(input("Inserisci l'altezza del triangolo: "))

area = 0.5 * base * altezza
perimetro = base + (2 * ((base ** 2 + altezza ** 2) ** 0.5))

print("Area del triangolo:", area)
print("Perimetro del triangolo:", perimetro)