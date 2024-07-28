name = input("Digite seu nome: ")
counter_name = len(name)

if counter_name <= 4:
    print("Seu nome é curto!")
elif 4 <= counter_name <= 6:
    print("Seu nome é normal!")
elif counter_name >= 6:
    print("Seu nome é grande!")
