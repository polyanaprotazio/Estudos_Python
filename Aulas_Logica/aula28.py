"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""

nome = input('Digite o seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade: 
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é {nome[::-1]}')

    if ' ' in nome:
        print(f'Seu nome contém espaços')
    else:
        print(f'Seu nome não contem espaços')
        
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print('Desculpe, você deixou campos vazios')

# nome = input('Digite seu nome:')
# idade = input('Digite sua idade:')
# nome_invertido = nome[::-1]
# qtd_letras = len(nome)

# if nome and idade:
#     print('Seu nome é {}'.format(nome))
#     print('Seu nome invertido é {}'.format(nome_invertido))
#     if ' ' in nome:
#         print('Seu nome contém espaços')
#     else:
#         print('Seu nome não contém espaços')
#     print('Seu nome tem {} letras'.format(qtd_letras))
#     print('A primeira letra do seu nome é {[0]}'.format(nome))
#     print('A última letra do seu nome é {[0]}'.format(nome_invertido))
# else:
#     print('Desculpe, você deixou campos vazios.')


    