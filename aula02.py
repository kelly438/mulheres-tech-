"""print('Qual a sua idade?')
idade = int(input())

if idade >= 18:
    print(' ACESSO LIBERADO! BOA FESTA!')
else :
    print(' ACESSO NEGADO! VOCÊ É MENOR DE IDADE!')"""

#CÓDIGO PARA LIBERAR O ACESSO SOMENTE PARA MAIORES DE 19 ANOS

"""print(' Qual a sua idade?')
idade = int(input())

if idade < 18:
    print(' ACESSO NEGADO! VOCÊ É MENOR DE IDADE!')
elif idade == 18:
    print(' VOCÊ ESTÁ QUASE LÁ! MAIS UM ANO E VOCÊ TERÁACESSO !')
else:
    print(' AECSSO LIBERADO! BOA FESTA ')"""
    
     
"""print('Digite a nota do primeiro bimestre:')   
B1 = float(input())  
print('Digite a nota do segundo bimestre:')   
B2 = float(input()) 
print('Digite a nota do terceiro bimestre:')   
B3 = float(input()) 
print('Digite a nota do quarto bimestre:')   
B4 = float(input()) 
media = (B1 + B2 + B3 + B4) / 4 
print('A média do aluno é ', media)

if media >=7:
    print('APROVADO')
elif media >= 5:
    print('RECUPERAÇÃO')
else:
    print("REPROVADO")"""


#CÓDIGO PARA VERIFICAR SE PODE PARTICIPAR DO MULHERES TECH

"""print('Qual seu gênero ? ( F ou M)')
genero = input()
print('Qual é o municipio que você mora?')
municipio = input()

if genero.upper == 'F' and municipio.lower == 'rio de janeiro':
    print('Você pode participar !')
else:
    print(' você não pode participar!')"""


#CÓDIGO PARA LIBERAR  ACESSO AO FILME PARA MAIORES DE 18 ANOS

print("*"*30 , 'BEM VINDO AO CINEMA SEVERIANO RIBEIRO ','* * 30')
print('')
print('Qual é a sua idade?')
idade = int(input())

if idade >=18:
    print ('Acesso liberdado!\n Bom filme!')
elif idade >=16:
    print('O filme selecionado é para maiores de 18 ano\n para acessar precisa estar acompanhado de um responsável. \n Você está com seu responsável?')
    responsavel = input().lower()
    if responsavel == 'sim':
     print('Acesso liberado ! \n Bom filme!')
    else:
        print('você só pode ver o filme acompanhado de um responsável')
else:
    print('Acesso negado! \n Você é menor de idade ')






















    
