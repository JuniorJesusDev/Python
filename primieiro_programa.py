tabela = int (input("Informe a tabela que deseja visualizar: "))
valor_maximo = tabela*10+1

for numero in range(0,valor_maximo,tabela):
    print(numero, end=" ")
