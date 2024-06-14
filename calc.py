import streamlit as st

# Título da calculadora
st.title('Calculadora Simples')

# Função para realizar operações
def calculadora(num1, num2, operacao):
    if operacao == 'Soma':
        return num1 + num2
    elif operacao == 'Subtração':
        return num1 - num2
    elif operacao == 'Multiplicação':
        return num1 * num2
    elif operacao == 'Divisão':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Erro: Divisão por zero'

# Entrada dos números e da operação
num1 = st.number_input('Digite o primeiro número:')
num2 = st.number_input('Digite o segundo número:')
operacao = st.selectbox('Selecione a operação:', ['Soma', 'Subtração', 'Multiplicação', 'Divisão'])

# Botão para calcular
if st.button('Calcular'):
    resultado = calculadora(num1, num2, operacao)
    st.success(f'O resultado da {operacao.lower()} é: {resultado}')
