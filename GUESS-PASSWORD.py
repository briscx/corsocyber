def guess_password(dictionary, password):
    for word in dictionary:
        if word == password:
            print(f"Password trovata: {word}")
        else:
            print(f"Password non trovata: {word}")


# Creazione del dizionario di parole
dictionary = [
    "ciao",
    "mela",
    "gatto",
    "sole",
    "mare",
    "rosso123",
    "verde",
    "blu",
    "casa",
    "amore",
    # Aggiungi altre parole al dizionario
]

# Password da indovinare
password = "rosso123"

# Tentativo di indovinare la password
guess_password(dictionary, password)