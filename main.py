"""
Essa aula possui 3 objetivos:
1.) Ensinar como se comenta em python e por quê.
2.) Utilizar o comando print.
3.) Utilizar o comando input.
4.) Se der, variaveis
"""

print("Essa aula possui 3 objetivos:")
print("1.) Ensinar como se comenta em python e por quê.")
print("2.) Utilizar o comando print.")
print("3.) Utilizar o comando input.")
print("4.) Se der, variaveis")

"""
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
        resultado = val1 ** 0.5
        print("O resultado é: ", resultado)
else:
    print("Digite uma operação válida")
"""