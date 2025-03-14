# #desafio 1
print("bem vindo a minha loja")
nome = input('digite seu nome')
login = input('coloque seu email')
senha = int(input('digite sua senha (apenas numeros)'))

print('ola', nome, ',seja bem vindo')
print('emai=l cadastrado é', login)
confirmação = input('sua senha é confidencial tem certeza que quer mostrar? (sim/não)')

if confirmação == "sim":
    print('sua senha é', senha)
else:
    print("sigilo")



print("Temos 3 coisas a venda no momento:"
"\nFones\ncelulares\ncarregadores\nescolha no seu tempo")

produtos = {'carregador': 50.00, 'celular':1200.00, 'fone':150.00}


#carrinho de compras
carrinho = []


# Entrada do usuário
produto1 = input("Escolha um produto (carregador, celular, fone): ")
produto2 = input("Escolha outro produto (carregador, celular, fone): ")

# Adicionando ao carrinho
carrinho.append(produtos[produto1])
carrinho.append(produtos[produto2])

# Calculando o total
total = sum(carrinho)

# Exibindo o valor da compra
print("Total da compra: R$", total)
print("como sera o modo de pagamento? aceitamos pix, debito e credito")

pagamentos = {'pix', 'debito', 'credito'}

pagar = input('escolha um dos metodos (pix, debito, credito)')

if pagar in pagamentos:
    print('certo, pagamento sera em', pagar,'.')
else:
    print('metodo de pagamento invalido')

#desafio 2
print("Bem vindo ao hotel: Panda Trips! Aproveite a estadia")
print("Temos tres tipos de quartos disponiveis no momento"
"\nSimples = diaria de R$100.00\nDuplo = diario de R$150.00\nLuxo = Diaria de R$250.00")

#cadrasto e reserva dos clientes (isso por 3 vezes)

nome1 = input('digite seu nome')
idade1 = int(input('digite sua idade'))

quarto1 = input('escolha entre um: quarto simples, quarto duplo ou quarto de luxo')
if quarto1 == "quarto simples" or quarto1 == "simples":
    preco1 = 100    
elif quarto1 == "duplo" or quarto1 == "quarto duplo":
    preco1 = 150
elif quarto1 == "quarto de luxo" or quarto1 == "luxo":
    preco1 = 250
else:
   print('ta moscndo paizao')
   preco1 = 0
print('voce escolheu o', quarto1, 'com o preço', preco1)

dias1 = int(input('quantos dias você ficara'))

valor1 = dias1 * preco1
print('o preço total sera', valor1)
#2
nome2 = input('digite seu nome')
idade2 = int(input('digite sua idade'))

quarto2 = input('escolha entre um: quarto simples, quarto duplo ou quarto de luxo')
if quarto2 == "quarto simples" or quarto2 == "simples":
    preco2 = 100    
elif quarto2 == "duplo" or quarto2 == "quarto duplo":
    preco2 = 150
elif quarto2 == "quarto de luxo" or quarto2 == "luxo":
    preco2 = 250
else:
   print('ta moscndo paizao')
   preco2 = 0
print('voce escolheu o', quarto2, 'com o preço', preco2)

dias2 = int(input('quantos dias você ficara'))

valor2 = dias2 * preco2
print('o preço total sera', valor2)
#3
nome3 = input('digite seu nome')
idade3 = int(input('digite sua idade'))

quarto3 = input('escolha entre um: quarto simples, quarto duplo ou quarto de luxo')
if quarto3 == "quarto simples" or quarto3 == "simples":
    preco3 = 100    
elif quarto1 == "duplo" or quarto3 == "quarto duplo":
    preco1 = 150
elif quarto3 == "quarto de luxo" or quarto3 == "luxo":
    preco3 = 250
else:
   print('ta moscndo paizao')
   preco3 = 0
print('voce escolheu o', quarto3, 'com o preço', preco3)

dias3 = int(input('quantos dias você ficara'))

valor3 = dias3 * preco3
print('o preço total sera', valor3)

#dados dos clientes
cliente1 = [nome1, idade1, quarto1, dias1, valor1]
cliente2 = [nome2, idade2, quarto2, dias2, valor2]
cliente3 = [nome3, idade3, quarto3, dias3, valor3]

print('dados do', nome1, '\n', cliente1)
print('dados do', nome2, '\n', cliente2)
print('dados do', nome3, '\n', cliente3)