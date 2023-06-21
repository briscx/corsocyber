base = float(input("Inserisci la base del rettangolo: "))
altezza = float(input("Inserisci l'altezza del rettangolo: "))

area = 0.5 * base * altezza
perimetro = base + (2 * ((base ** 2 + altezza ** 2) ** 0.5))

print("Area del rettangolo:", area)
print("Perimetro del rettangolo:", perimetro)