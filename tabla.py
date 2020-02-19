
def imprimir_tabla(numero):
    # Se supone que las tablas llegan hasta el 10
    LIMITE = 10
    # Comenzar en 1
    contador = 1
    while contador <= LIMITE:
        resultado = contador * numero
        print("{} x {} = {}".format(numero, contador, resultado))
        # Incrementar contador para no caer en ciclo infinito
        contador = contador + 1

# Probar función
imprimir_tabla(1)
imprimir_tabla(2)
imprimir_tabla(3)
imprimir_tabla(4)
imprimir_tabla(5)
imprimir_tabla(6)
imprimir_tabla(7)
imprimir_tabla(8)
imprimir_tabla(9)
imprimir_tabla(10)
