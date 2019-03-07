import math
import sys # com esse import voce consegue ler o argumento passado

def help():
    print("É necessario informar o raio do circulo")



def circulo(raio):
   return math.pi * float(raio) ** 2 # criação de uma função 


if __name__ == '__main__':
    if len(sys.argv) <2 :
        help()
    else:
        raio = sys.argv[1] # o argumento de numero 0 é  o proprio nome do arquivo, o 1 é o parametro passado
        area = circulo(raio) # chamando a função
        print('Area do circulo é: ', area)
