temperatures = []

while True:
    temperature = input("Inserisci una temperatura (q per terminare): ")
    if temperature.lower() == 'q':
        break
    try:
        temperature = float(temperature)
        temperatures.append(temperature)
    except ValueError:
        print("Inserisci un valore numerico valido.")

if len(temperatures) > 0:
    average_temperature = sum(temperatures) / len(temperatures)
    print("La media delle temperature inserite è:", average_temperature)
else:
    print("Nessuna temperatura inserita.")