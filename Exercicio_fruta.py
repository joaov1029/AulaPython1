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
if fruta == "1" or fruta == "banana":
    print(f"\nO cliente {nome}, com a idade {idade} anos, deseja comprar banana")
elif fruta == "2" or fruta == "maçã":
    print(f"\nO cliente {nome}, com a idade {idade} anos, deseja comprar maçã")
elif fruta == "3" or fruta == "pêra":
    print(f"\nO cliente {nome}, com a idade {idade} anos, deseja comprar pêra")
elif fruta == "4" or fruta == "melância":
    print(f"\nO cliente {nome}, com a idade {idade} anos, deseja comprar melância")
elif fruta == "5" or fruta == "morango":
    print(f"\nO cliente {nome}, com a idade {idade} anos, deseja comprar morango")
elif fruta == "6" or fruta == "Abacaxi":
    print(f"\nO cliente {nome}, com a idade {idade} anos, deseja comprar Abacaxi")
else:
    print("Fruta não disponível")