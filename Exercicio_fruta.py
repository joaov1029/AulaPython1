"""
Um programa que vende frutas:
nome do comprador
idade do comprador
perguntar a fruta desejada
menu
1.) banana
2.) maçã
3.) pêra
4.) melância
5.) morango
6.) Abacaxi

Escolher fruta
apresentar o nome da pessoa, a idade e a  fruta escolhida
"""

nome = input("Digite seu nome:\n")
idade = int(input("Digite sua idade\n"))
fruta = input("Qual das frutas abaixo deseja comprar?"
              "\nbanana"
              "\nmaçã"
              "\npêra"
              "\nmelância"
              "\nmorango"
              "\nAbacaxi"
              "\n")
print(f"\nO cliente {nome}, com a idade {idade}, deseja comprar a fruta {fruta}")