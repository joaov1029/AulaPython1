frutas = {
    "1": "banana",
    "2": "maçã",
    "3": "pêra",
    "4": "melância",
    "5": "morango",
    "6": "Abacaxi"
}

nome = input("Digite seu nome:\n")
idade = int(input("Digite sua idade\n"))
fruta = input("\nQual das frutas abaixo deseja comprar?"
              "\n1.) banana"
              "\n2.) maçã"
              "\n3.) pêra"
              "\n4.) melância"
              "\n5.) morango"
              "\n6.) Abacaxi"
              "\n")
if fruta in frutas.keys():
    print(f"\nO cliente {nome}, com a idade {idade} anos, deseja comprar {frutas[fruta]}")
else:
    print("Fruta não encontrada")