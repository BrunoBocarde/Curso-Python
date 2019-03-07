import math
import sys # com esse import voce consegue ler o argumento passado


def circulo(raio):
   return math.pi * float(raio) ** 2 # criação de uma função 


if __name__ == '__main__':
    raio = sys.argv[1]
    area = circulo(raio) # chamando a função
    print('Area do circulo é: ',area)
