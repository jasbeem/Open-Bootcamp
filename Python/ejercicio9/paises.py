

def main():
    # Pedimos los paises por teclado separados por comas
    paises = input("Introduce países separados por comas:\n")
    paises = paises.split(',')
    
    # Creamos un conjunto con los paises
    paises_unicos = set(paises)

    # Ordenamos los paises
    paises_ordenados = sorted(list(paises_unicos))

    # creamos la cadena a mostrar
    texto = ",".join(paises_ordenados)

    print(f'Los paises únicos y ordenados son: {texto}')


if (__name__=="__main__"):
    main()