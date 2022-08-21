from operacao import *

def valor_digitado(valor):
    return str(valor)

def Operação_str(str_operacao):
    if ("-" in str_operacao):
        valor = str_operacao.split("-")
        print(str_operacao)
        return subtrair(float(valor[0]), float(valor[1]))
    elif ("+" in str_operacao):
        valor = str_operacao.split("+")
        print(str_operacao)
        return somar(float(valor[0]), float(valor[1]))
    elif ("/" in str_operacao):
        valor = str_operacao.split("/")
        print(str_operacao)
        return divisao(float(valor[0]), float(valor[1]))
    elif ("*" in str_operacao):
        valor = str_operacao.split("*")
        print(str_operacao)
        return multiplicar(float(valor[0]), float(valor[1]))

def apagar(str_operacao):
    str_operacao=str(int(float(str_operacao)))
    valor = list(str_operacao)
    valor.pop()
    valor1="".join(valor)
    valor2 = (lambda valor: True if (valor == 0 or valor =="" or valor =="0") else False)
    if (valor2(valor1) == True):
        return 0
    return valor1







