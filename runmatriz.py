import matriz

def main():
    
    lista = ['MENU\n''1.Determinante', '2.Transpuesta', '3.Inversa', '4.Escalar', '5.Matriz_Elevada', '6.Simetrica', '7.Identica',
             '8.Multiplicacion', '9.Suma', '10.Resta', '11.Salir']

    for i in lista:
        print i
    Z = int(input("Selecione La operacion que Desea Realizar "))
    if Z == 1:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a=matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.matriz_det(Z)

    if Z == 2:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.transpuesta()

    if Z == 3:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a=matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.matriz_inversa(Z)

    if Z == 4:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.matriz_numero()

    if Z == 5:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         matrizA.matriz_elevada()

    if Z == 6:
         matrizA = matriz.Matriz()
         matrizA.matrizSimetrica()

    if Z == 7:
         matrizA = matriz.Matriz()
         matrizA.matrizidentica()

    if Z == 8:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a=matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprime_matrizC()

         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.multiplicacionmatriz(filasA,columnasB,filasB,columnasA,a,b)

    if Z == 9:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a = matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprime_matrizC()

         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.sumamatriz(filasA, columnasB, filasB, columnasA, a, b)

    if Z == 10:
         matrizA = matriz.Matriz()
         matrizA.crearMatrizA()
         a = matrizA.llenarmatrizA()
         matrizA.imprime_matriz()
         columnasA = matrizA.getColumnas()
         filasA = matrizA.getFilas()

         matrizB = matriz.Matriz()
         matrizB.crearMatrizA()
         b = matrizB.llenarmatrizA()
         matrizB.imprime_matrizC()

         columnasB = matrizB.getColumnas()
         filasB = matrizB.getFilas()
         matrizA.restamatriz(filasA, columnasB, filasB, columnasA, a, b)

    if Z == 11:
        print "Vuelva Pronto Y Usa Esta Calculadora "
        M = True
    else:
        b = raw_input("Presione la tecla entrar para volver al menu")
        M = False



if __name__ == '__main__':
    main()