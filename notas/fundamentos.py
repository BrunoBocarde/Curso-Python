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

