primeiro = input('Digite um valor: ')
segundo = input('Digite outro valor: ')


"""
Operadores de comparação (relacionais)
OP      Significado         Exemplo (True)
>       maior               2 > 1
>=      maior ou igual      2 >= 2
<       menor               1 < 2
<=      menor ou igual      2 <= 2
==      igual               'a' == 'a'
!=      diferente           'a' != 'b'
"""

if primeiro > segundo:
    print(f'{primeiro=} é maior que o {segundo=}')
elif primeiro < segundo:
    print(f'{segundo=} é maior que o {primeiro=}')
elif primeiro == segundo:
    print(f'{primeiro=} é igual ao {segundo=}')
else:
    print('Digite um número válido.')