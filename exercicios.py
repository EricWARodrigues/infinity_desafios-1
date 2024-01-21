def calcular(num1, num2, operador):
    if operador == '+':
        return num1 + num2
    elif operador == '-':
        return num1 - num2
    elif operador == '*':
        return num1 * num2
    elif operador == '/':
        if num2 == 0:
            return 'Impossível dividir por 0'
        else:
            return num1 / num2
    else:
        return 'Operação inválida'

print('-' * 30)
print('Bem vindo a calculadora simples')
print('-' * 30)

num1 = int(input('informe um numero: '))
operador= input('informe o operador(+,-,*,/): ')
num2 = int(input('informe um numero: '))
print(f'o resultado é {calcular(num1, num2, operador)}')
