#conversão de dados
idade = int(input("Digite sua idade: "))
if idade >= 12 and idade <21: 
    print("Você é adolescente")
elif idade >= 21 and idade < 30:
    print("Você é jovem")
elif idade >=30 and idade <=100:
    print("Você é adulto")
else:
    print("Valor não encontrado")
