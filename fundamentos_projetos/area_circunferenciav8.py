import math


def circulo(raio):
    print('A area do circulo é: ', math.pi *
          float(raio) ** 2)  # criação de uma função


if __name__ == '__main__':
    raio = input('Informe o raio :')
    circulo(raio)  # chamando a função
