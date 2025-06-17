# Verificador de Número Primo

# Entrada de dados
n = int(input("Digite um número para verificar se é primo: "))

# Variável de controle
is_prime = True

# Condição: números menores que 2 não são primos
if n < 2:
    is_prime = False
else:
    # Checando divisores de 2 até n-1
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

# Saída
if is_prime:
    print("Prime")
else:
    print("Not Prime")
