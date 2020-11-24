import random
dibujo= [
    '''
        +---+
        |   |
            |
            |
            |
            |
            ============''', 
            '''
        +---+
        |   |
        O   |
            |
            |
            |
            ============''', 
            '''
        +---+
        |   |
        O   |
        |   |
            |
            |
            ============''', 
            '''
        +---+
        |   |
        O   |
        |\  |
            |
            |
            ============''',
            '''
        +---+
        |   |
        O   |
       /|\  |
            |
            |
            ============''',
            '''
        +---+
        |   |
        O   |
       /|\  |
         \  |
            |
            ============''',
            '''
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |FAILED
            ============'''
]

oracion='''
sobrina bisabuela criatura especie naturaleza campo bosque selva jungla desierto costa playa
rio laguna lago mar océano cerro monte montaña animales animal perro gato vaca cerdo caballo 
yegua oveja'''

def sacandoPalabra():
    palabra=oracion.split()
    n= random.randint(0,len(palabra)-1)
    return palabra[n]

def main():
    palabra=sacandoPalabra()
    lpalabra=[]
    l2palabra=[]
    for i in palabra:
        lpalabra.append(i)
        l2palabra.append('__')
    #print(palabra)
    #print(','.join(l2palabra))
    
    contaDibujo=0
    print(dibujo[contaDibujo])
    print(','.join(l2palabra))
    while True:
        llave=False       
        entrada=input('\nIngrese Letra= ')
        conta=-1
        for i in palabra:
            conta+=1
            if entrada==i:
                l2palabra[conta]=entrada
                llave=True
        if lpalabra==l2palabra:
            print('Ganaste!!')
            break
        
        if contaDibujo>=5 and llave != True:
            print(dibujo[6])
            print('Perdiste la palabra es: ', ''.join(lpalabra))
            break
        elif llave==False:
            contaDibujo+=1
        print(dibujo[contaDibujo])
        print(','.join(l2palabra))


main()