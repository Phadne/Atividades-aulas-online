# Financiamento
valor = float(input("Digite o valor do financiamento: "))
salário = float(input("Digite o seu salário: "))
prestacao = valor / salário
if prestacao > salário * 0.3:
    print("Infelizmente você não pode obter o empréstimo")
else:
    print(f"Valor da prestação: R$ {prestacao:7.2f} Empréstimo OK")
