import math
import sys # com esse import voce consegue ler o argumento passado

def help():
    print("É necessario informar o raio do circulo")



def circulo(raio):
   return math.pi * float(raio) ** 2 # criação de uma função


if __name__ == '__main__':
    if len(sys.argv) <2:
        help()
        # sys.exit(1) # faz com que a aplicação pare
    elif not sys.argv[1].isnumeric(): # pega o valor do parametro e verifica se é numerico
        help()
        print("Informar apenas valores numericos")
    else:
        raio = sys.argv[1] # o argumento de numero 0 é  o proprio nome do arquivo, o 1 é o parametro passado
        area = circulo(raio) # chamando a função
        print('Area do circulo é: ', area)
