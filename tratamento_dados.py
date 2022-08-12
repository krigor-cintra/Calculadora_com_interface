from operacao import *

def valor_digitado(valor):
    return str(valor)
def fazer_operacao(str_operacao):
    valor = str_operacao.split("+")
    return somar(float(valor[0]),float(valor[1]))




