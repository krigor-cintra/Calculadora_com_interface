from operacao import *

def valor_digitado(valor):
    return str(valor)

def Str_somar(str_operacao):
    valor = str_operacao.split("+")
    return somar(float(valor[0]),float(valor[1]))
def apagar(str_operacao):
    str_operacao=str(int(float(str_operacao)))
    valor = list(str_operacao)
    valor.pop()
    valor1="".join(valor)
    return valor1






