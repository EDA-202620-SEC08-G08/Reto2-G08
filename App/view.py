import sys
import App.logic as logic
from DataStructures.List import array_list as lt

default_limit = 1000
sys.setrecursionlimit(default_limit * 10)

def new_logic():
    
    
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    print("\nArchivos disponibles:")
    print("1- chocolate_sale_100_elementos.csv")
    print("2- chocolate_sale_20_ptc.csv")
    print("3- chocolate_sale_40_ptc.csv")
    print("4- chocolate_sale_60_ptc.csv")
    print("5- chocolate_sale_80_ptc.csv")
    print("6- chocolate_sale_100_ptc.csv")
    opcion = input("Seleccione el archivo que desea cargar: ")

    if opcion == "1":
        archivo = "chocolate_sale_100_elementos.csv"
    elif opcion == "2":
        archivo = "chocolate_sale_20_ptc.csv"
    elif opcion == "3":
        archivo = "chocolate_sale_40_ptc.csv"
    elif opcion == "4":
        archivo = "chocolate_sale_60_ptc.csv"
    elif opcion == "5":
        archivo = "chocolate_sale_80_ptc.csv"
    else:
        archivo = "chocolate_sale_100_ptc.csv"

    control, tiempo = logic.load_data(control, archivo)

    print(f"\nArchivo cargado: {archivo}")
    print(f"Carga de datos ejecutada en {tiempo:.2f} milisegundos")
    print(f"Total de pedidos cargados: {lt.size(control['orders'])}")

    return control



def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
pass    

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    anio = int(input("Ingrese el año del pedido (YYYY): "))
    mes = int(input("Ingrese el mes del pedido (1-12): "))
    descuento_min = float(input("Ingrese el descuento mínimo (%): "))
    descuento_max = float(input("Ingrese el descuento máximo (%): "))

    tiempo, total_pedidos, total_amount, promedio_precio, promedio_cajas, pedidos = logic.req_1(control, anio, mes, descuento_min, descuento_max)

    print(f"\nRequerimiento 1 ejecutado en {tiempo:.2f} milisegundos")
    print(f"Cantidad de pedidos que cumplen el filtro: {total_pedidos}")
    print(f"Monto total recaudado: ${total_amount:.2f}")
    print(f"Promedio del precio por caja: ${promedio_precio:.2f}")
    print(f"Promedio de Cajas Despachadas: {promedio_cajas:.2f}")

    if total_pedidos == 0:
        print("\nNo se encontraron pedidos con los parámetros ingresados")
        return

    if total_pedidos > 20:
        print(f"\nSe muestran los primeros 10 y los últimos 10 pedidos de {total_pedidos}")

    for pos in range(0, total_pedidos):
        if total_pedidos > 20 and pos >= 10 and pos < total_pedidos - 10:
            continue
        pedido = lt.get_element(pedidos, pos)
        print(f"\nOrder_ID: {pedido['Order_ID']}")
        print(f"Product: {pedido['Product']}")
        print(f"Country: {pedido['Country']}")
        print(f"Channel: {pedido['Channel']}")
        print(f"Order_Date: {pedido['Order_Date']}")
        print(f"Discount_Pct: {pedido['Discount_Pct']:.2f}%")
        print(f"Price_per_Box: ${pedido['Price_per_Box']:.2f}")
        print(f"Boxes_Shipped: {pedido['Boxes_Shipped']}")
        print(f"Amount: ${pedido['Amount']:.2f}")



def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    pass


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    n = int(input("Ingrese el número N de países a listar: "))
    producto = input("Ingrese el producto (Product): ")
    fecha_inicial = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fecha_final = input("Ingrese la fecha final (YYYY-MM-DD): ")

    tiempo, total_pedidos, total_paises, amount_total, marketing_total, top_paises = logic.req_6(control, n, producto, fecha_inicial, fecha_final)

    print(f"\nRequerimiento 6 ejecutado en {tiempo:.2f} milisegundos")
    print(f"Cantidad de pedidos que cumplen el filtro: {total_pedidos}")
    print(f"Cantidad de países diferentes encontrados: {total_paises}")
    print(f"Amount total de los pedidos filtrados: ${amount_total:.2f}")
    print(f"Gasto Marketing total de los pedidos filtrados: ${marketing_total:.2f}")

    if total_pedidos == 0:
        print("\nNo se encontraron pedidos con los parámetros ingresados")
        return

    print(f"\nTop {lt.size(top_paises)} países con mayor eficiencia de mercadeo:")
    for pos in range(0, lt.size(top_paises)):
        pais = lt.get_element(top_paises, pos)
        print(f"\nPais: {pais['Country']}")
        print(f"Cantidad de pedidos: {pais['num_pedidos']}")
        print(f"Amount total: ${pais['amount_total']:.2f}")
        print(f"Gasto Marketing total: ${pais['marketing_total']:.2f}")
        print(f"Cajas Despachadas totales: {pais['boxes_total']}")
        print(f"Precio por caja promedio: ${pais['precio_promedio']:.2f}")
        print(f"Eficiencia de mercadeo: {pais['eficiencia']:.4f}")


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
