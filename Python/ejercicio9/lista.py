from functools import reduce

def reduceLista(lista): 
    impares = list(filter((lambda x: x % 2), lista)) 
    reduccion = reduce( (lambda x, y: x + y), impares) 
    print(f'El resultado de filtar impares de la lista {lista} es {list(impares)} y reduciendo queda {reduccion}')

def main():
    lista = [1,2,3,4,5,6,7,9,10]
    reduceLista(lista)



if (__name__=="__main__"):
    main()
