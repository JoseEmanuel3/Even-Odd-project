i = 0
while i == 0:
    digit_user = input("Digite um numero inteiro: ")
    if digit_user.isdigit() and int:
        digit_user_int = int(digit_user)

        if (digit_user_int % 2) == 0:
            print(f"{digit_user_int} é um número inteiro e par!")
            i = 1
        else:
            print(f"{digit_user_int} é um número inteiro impar!")
            i = 1
    else:
        print("Você não digitou um número inteiro!")
        