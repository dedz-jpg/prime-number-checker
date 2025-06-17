# Prime Number Checker 

Projeto simples desenvolvido para verificar se um número informado pelo usuário é um número primo ou não, usando Python.

---

## O que é um número primo?

Um número primo é aquele que possui exatamente dois divisores positivos:  
**1 e ele mesmo.**

**Exemplos de números primos:**
- 2
- 3
- 5
- 7
- 11
- 13

**Exemplos de números NÃO primos (compostos):**
- 4 (divisível por 1, 2, 4)
- 6 (divisível por 1, 2, 3, 6)
- 9 (divisível por 1, 3, 9)
- 10 (divisível por 1, 2, 5, 10)

Curiosidade:  
O número **1 não é considerado primo** e nem composto.

---

## Lógica utilizada:

O programa segue os seguintes passos:

1. Lê o valor de **N** informado pelo usuário.
2. Se **N < 2**, já sabemos que não é primo.
3. Caso contrário, verifica se **existe algum divisor de N entre 2 e N-1**.
4. Se encontrar um divisor, exibe "**Not Prime**".
5. Se não encontrar nenhum divisor, exibe "**Prime**".

---

## Exemplo de entrada e saída:

### Exemplo 1:  
**Input:** 

11

**Output:**

Prime

**Input:**

9

**Output:**

Not prime

**Input:**

1

**Output:**

Not prime

---

## Por que fiz esse projeto?

Esse projeto faz parte da minha fase de aprendizado de **lógica de programação**, como parte do curso **Coding Essentials – Logic Building for Beginners (Udemy)**.  
Meu objetivo foi treinar:

- Estruturas de repetição (loops)
- Condicionais
- Validação matemática básica

---

## Tecnologias usadas:

- Python 3.x

---

## Sobre mim:

Sou André Ricardo, estudante em transição de carreira para a área de TI.  
Atualmente focado em aprender **Python**, **Lógica de Programação** e também explorando áreas como **Inteligência Artificial** e **Montagem de Hardware**.
 
