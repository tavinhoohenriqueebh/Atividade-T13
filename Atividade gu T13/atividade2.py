while True:
    try:
        numero = int(input("Digite um numero positivo: "))
        
        if numero < 0:
            print("ERRO! O numero nao pode ser negativo.")
        else:
            break
    
    except ValueError:
        print("ERRO! Digite apenas numeros inteiros.")

print("Numero:", numero)