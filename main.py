import math
"""
Essa aula possui 3 objetivos:
1.) Ensinar como se comenta em python e por quê.
2.) Utilizar o comando print.
3.) Utilizar o comando input.
4.) Se der, variaveis
"""
"""
#print
print("Essa aula possui 3 objetivos:\n")
print("1.) Ensinar como se comenta em python e por quê.\n")
print("2.) Utilizar o comando print.\n")
print("3.) Utilizar o comando input.\n")
print("4.) Se der, variaveis")
"""
"""
#Concatenação
nome = input("Qual seu nome?\n")
idade = int(input("Qual sua idade?\n"))
print(f"\nMeu nome é {nome}, e minha idade é {idade} anos")
"""


#Adega
idade = int(input("Qual sua idade?\n"))
if idade < 18:
    print("\nNão pode consumir bebidas alcoólicas")
elif idade < 21:
    print("\nPode consumir cerveja")
else:
    print("\nPode consumir todas as bebidas alcoólicas")


"""
#Calculadora
val1 = float(input("Digite o primeiro valor"))
op = input("Digite a operação")
val2 = 1.0
resultado: float = 1.0
if op != "raiz":
    val2 = float(input("Digite o segundo valor"))
else:
    val2 = 1
if op == "+":
    # soma
    resultado = val1 + val2
    print("O resultado é: ", resultado)
elif op == "-":
    # subtração
    resultado = val1 - val2
    print("O resultado é: ", resultado)
elif op == "*" or op == "X" or op == "x":
    # multiplicação
    resultado = val1 * val2
    print("O resultado é: ", resultado)
elif op == "/":
    # divisão
    if val2 == 0:
        print("Impossível dividir por 0")
    else:
        resultado = val1 / val2
        print("O resultado é: ", resultado)
elif op == "**":
    # potenciação
    resultado = val1 ** val2
    print("O resultado é: ", resultado)
elif op == "raiz":
    # raiz
    if val1 < 0:
        print("Impossível realizar a raíz de números negativos")
    else:
        resultado = math.sqrt(val1)
        print("O resultado é: ", resultado)
else:
    print("Digite uma operação válida")
"""