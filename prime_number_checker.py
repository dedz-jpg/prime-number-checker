# Verificador de Número Primo - Projeto de Lógica de Programação

# Entrada de dados
n = int(input("Digite um número para verificar se ele é primo: "))

# Inicializa a variável de controle
is_prime = True

# Trata casos menores que 2
if n < 2:
    is_prime = False
else:
    # Verifica possíveis divisores de 2 até n-1
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break  # Não precisa continuar verificando

# Saída
if is_prime:
    print(f"{n} é um número primo.")
else:
    print(f"{n} não é um número primo.")
