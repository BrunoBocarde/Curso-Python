print('Hello word')
print(1 + 2)
# help(print)  usando o help voce consegue consegue ver a "documentação" da função 

        # TIPOS BASICOS 
print(True)
print(False)
print(1.2 + 3)
print('test')
print("test 2 ")
print('voce é '+ 3 * 'muito ' + 'legal')
#print(3 + " 3") Ambiguidade 
lista = [1, 2, 3] # lista 
dicionario =  {'nome': 'pedro','idade': 22}
print(None) # valor nulo 

        # VARIAVEIS
a = 10
b = 5.2 
print(a+b)
a = 'agora sou uma string '
print(a)
print(type(a))

        # COMENTARIOS
salario = 3450.25 
dispesas = 2456.2
'''
isso é comentario de multiplas linhas
!!!!
'''
print(salario - dispesas)

        # OPERADORES ARITIMETICOAS
print(2 +3)
print(4  -7)
print(2 * 5.3)
print(9.4 / 3)
print(9.4 // 3 )    # o // sesrve para dar o resultado da divisao um numero interio 
print(2 **8) # exponenciação 
print(10 % 3) # modulo a sobra da visivão 


        # OPERADORES RELAIONAIS
print(3>4)
print(4>=3)
print(1<2)
print(3<=2)
print(3!=2)
print(3==3)
print(3 =='3')

        # OPERADORES DE ATRIBUIÇÃO
a = 3
a = a + 7 
print(a)
a+=5 # acresentando o valor 5 na variavel 
print(a)
a-=5 #tirando da variavel 
print(a)
a*= 2 #multiplicativa 
print(a)
a/= 4 #divisiva 
print(a)
a%= 3 #modular
print(a)
a**= 8 #exponenciativa 
print(a)
a//=256 #divisivel mas o resultado sempre inteiro 
print(a) 

        # OPERADRES LOGICOS 
print(7 !=3 and 2 > 3) # and tem que obeder todas as  condições 
print(3>=2 or 7!= 7) # or só precisa obdecer umas das condições 

        #OPERADORES UNARIOS
c = 3 
# a++ em python nao se uso ++ para encrementar as variaveis se usa :
c += 1
print(c)
# a-- em python nao se uso -- para decencrementar as variaveis se usa :
c-= 1 
print(c)

        #OPERADPRES TERNARIOS
esta_chovendo = True
print('Hoje estou com as roupas ' + ('secas.', 'molhadas')[esta_chovendo])
print('Hoje estou com as roupas ' + ('molhadas' if esta_chovendo else 'secas'))

        #MAIS OPERADORES
    #OPERADOR DE MEMBRO 
lista = [1, 2, 3, 'ana','carla']
print(2 in lista)
print('ana' not in lista)
    #OPERADOR DE IDENTIDADE 
x = 3
y = x
z = 3
print( x is z)
print(y is not z)
lista_a = [1,2,3]
lista_b = lista_a
lista_c = [1,2,3]
print(lista_a is lista_b)
print(lista_a is lista_c)

        #BUILTINS
print(dir()) # ver todas as variaveis globais 

        # CONVERSÃO DE TIPOS 
a= 2
b ='3'
print(type(a))
print(type(b))
print(a + int(b))
print(str(a) +b )

                #TIPOS NUMERICOS 
print(dir(float))
print(dir(int))
print(1.1 + 2.2) 
from decimal import Decimal, getcontext # aqui importamos a pacote decimal e getcontext para aumentar a precisão 
print(Decimal(1) / Decimal(7))  
getcontext().prec = 4    # mudamos a precisao p/ 4 casa decimais   
print(Decimal(1) / Decimal(7))  
print(Decimal.max(Decimal(1), Decimal(7))) # retorna o maior valor 


                #TIPO STRING
print(dir(str))
nome = 'Saulo Pedro'
print(nome[0]) # cada letra tem seu indice 
print(" Texto para testar o escape d\'agua  ") #\ para texto que tenho que usar aspas 
print("Texto com multiplas \n ..... linhas")
nome = "ana paula"
print(nome[0])
print(nome[1])
print(nome[-2]) # com o menos ele pega da direita p/ esquerda 
print(nome[4:]) # acessa do range 4 até o ultimo
print(nome[-5 :])
print(nome[:3]) # do indice o até  o 2 
numero = '1234567890'
print(numero[::2]) # vai pulando de 2 em 2 
print(numero[1::3]) # começa no indice 1 incluindo ele e vai pulando de 3 em 3 
print(numero[::-1]) # mostrando a string ao contrario
print(numero[::-2]) # mostrando ao contrario e pulando em 2 em 2
print(nome[::-1])
frase = 'Python é uma linguagem execelente'
print('py'in frase) # é case sensitive 
print('ing' in frase)
print(len(frase))
print(frase.lower()) # a frase foi inteira minuscula 
print(frase.upper()) # a frase foi inteira maiuscula 
print(frase.split('e')) # retira toda letra e 

                #LISTA
lista = []
lista.append(1)
lista.append(5)
print(lista)
nova_lista = [1,5,'ana','bia']
nova_lista.remove(5) # o elemento 5 foi excluido nao de indice 5 
print(nova_lista)
nova_lista.reverse()
print(nova_lista)
lista = [1,5,"guilherme",'joao',3.14]
print(lista.index('guilherme'))
print(lista[3])
lista = ['rui','jao','pedro','bruno']
print(lista[1:3])
print(lista[0:-1])
del lista[1]
print(lista)

                #TUPLA
tupla = ()
tupla = tuple() # as duas maneiras estao certas 
print(help(tuple))
tupla = ('um')
print(type(tupla)) 
tupla = ('um',) # para criar um tupla de um unico elemento precisa colocar a virgula no final, pois se não vira uma str
print(type(tupla))
cores = ('azul','amarelo','branco','preto')
print(cores[0])
print(cores[-1])
print(cores[1:])

                #DICIONARIO
pessoa = {'nome' : 'prof ana', 'idade' : 30 , 'cursos ' : ['ingles','portugues']} # mesmo comando da lista 

                #CONJUNTO
a= {1,2,3}
print(a)
a = set('cor3er')
print(a) # conjunto não é indexado e nao aceita repetição 
print({1,2,3} == {1,2,3,2,1}) # pois como sao conjuntos nao tem index e nao aceita repetição 
#operações 
c1 = {1,2}
c2 = {3,2}
print(c1.union(c2))
print(c1.intersection(c2)) # somente ira mostara o que os 2 conjuntos tem de igual 
c1.update(c2) # adicionou todos so elementos do c2 para c1 
print(c1)
c2 <= c1 # se o conjunto c2 é subconjunto de c1 
c1 <= c2 
print({1,2,3} - {2}) # diferença entre dois conjuntos

                #INTERPOLAÇÃO 
nome, idade = 'ana', 30.858
print('Nome: %s Idade %.2f' %(nome,idade))