#universo
#heroi - 5 herois
#qtd de vezes

Marvel = ["Iron Man", "Spider-Man", "Hulk", "Wolverine", "Ciclope"]
DC = ["Super Man", "Batman", "Aquaman", "Wonder Woman", "Cyborg"]

universo = input("Digite o universo: ")
if universo == "Marvel": 
    print("Você escolheu o universo marvel!")

    heroi = input("Digite seu herói: ")
    print("Você escolheu o "+heroi+"!")
    numero = int(input("Quantas vezes deseja repetir este herói? "))

    contador = 0
    while(contador < numero):
        print(heroi)
        contador = contador + 1


elif universo == "DC": 
   print("Você escolheu o universo DC!")

   heroi = input("Digite seu herói: ")
   print("Você escolheu o "+heroi+"!")
   numero = int(input("Quantas vezes deseja repetir este herói? "))

   contador = 0
   while(contador < numero):
        print(heroi)
        contador = contador + 1
   
else:
    print("Universo não encontrado!")