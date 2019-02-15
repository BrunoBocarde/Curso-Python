import math


def circulo(raio):
   return math.pi * float(raio) ** 2 # criação de uma função 


if __name__ == '__main__':
    raio = input('Informe o raio :')
    area =  circulo(raio) # chamando a função 
    print('Area do circulo é: ',area)
