while True:
    entrada = input("Digite um numero: ")
    
    try:
        numero = int(entrada)
        break
    except ValueError:
        print("ERRO! Digite apenas numeros.")

print("Numero:", numero)