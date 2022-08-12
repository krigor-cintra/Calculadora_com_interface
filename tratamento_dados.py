from operacao import *

def valor_digitado(valor):
    return str(valor)

def Str_somar(str_operacao):
    valor = str_operacao.split("+")
    return somar(float(valor[0]),float(valor[1]))




