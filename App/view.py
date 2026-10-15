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
    print("8- Consultar un pedido por Order_ID")
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
    elif opcion == "6":
        archivo = "chocolate_sale_100_ptc.csv"


    else:
        print("Opción incorrecta")
        return control

    nuevo_control = logic.new_logic()
    catalog, tiempo, resumen = logic.load_data(nuevo_control, archivo)

    control.clear()
    control.update(catalog)

    print(f"\nArchivo cargado: {archivo}")
    print(f"Tiempo de carga: {tiempo:.2f} milisegundos")
    print(f"Total de pedidos cargados: {resumen['total_pedidos']}")

    print("\nPEDIDOS POR CANAL")

    for canal in resumen["canales"]:
        print(f"{canal}: {resumen['canales'][canal]}")

    if resumen["total_pedidos"] == 0:
        print("\nNo se encontraron pedidos en el archivo")
        return control

    print(f"\nFecha más antigua: {resumen['fecha_min']}")
    print(f"Fecha más reciente: {resumen['fecha_max']}")

    campos = [
        "Order_ID",
        "Product",
        "Country",
        "Channel",
        "Order_Date",
        "Boxes_Shipped",
        "Price_per_Box",
        "Amount"
    ]

    print("\nPEDIDO CON MENOR AMOUNT")

    pedido_min = resumen["pedido_min"]

    for campo in campos:
        print(f"{campo}: {pedido_min[campo]}")

    print("\nPEDIDO CON MAYOR AMOUNT")

    pedido_max = resumen["pedido_max"]

    for campo in campos:
        print(f"{campo}: {pedido_max[campo]}")

    print("\nPRIMEROS CINCO PEDIDOS")

    primeros = resumen["primeros"]

    for i in range(lt.size(primeros)):
        pedido = lt.get_element(primeros, i)

        print(f"\nPedido {i + 1}")

        for campo in campos:
            print(f"{campo}: {pedido[campo]}")

    print("\nÚLTIMOS CINCO PEDIDOS")

    ultimos = resumen["ultimos"]

    for i in range(lt.size(ultimos)):
        pedido = lt.get_element(ultimos, i)

        print(f"\nPedido {i + 1}")

        for campo in campos:
            print(f"{campo}: {pedido[campo]}")

    return control


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    id = input("Ingrese el Order_ID del pedido: ")
    pedido = logic.buscar_pedido(control, id)

    if pedido is None:
        print(f"\nNo existe un pedido con el Order_ID {id}")
        return

    print(f"\nOrder_ID: {pedido['Order_ID']}")
    print(f"Product: {pedido['Product']}")
    print(f"Country: {pedido['Country']}")
    print(f"Channel: {pedido['Channel']}")
    print(f"Order_Date: {pedido['Order_Date']}")
    print(f"Discount_Pct: {pedido['Discount_Pct']:.2f}%")
    print(f"Price_per_Box: ${pedido['Price_per_Box']:.2f}")
    print(f"Marketing_Spend: ${pedido['Marketing_Spend']:.2f}")
    print(f"Boxes_Shipped: {pedido['Boxes_Shipped']}")
    print(f"Amount: ${pedido['Amount']:.2f}") 

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
    pais = input("Ingrese el país: ")
    min_cajas = int(input("Ingrese el mínimo de cajas: "))
    max_cajas = int(input("Ingrese el máximo de cajas: "))

    if min_cajas > max_cajas:
        print("El mínimo no puede ser mayor que el máximo")
        return

    resultado = logic.req_2(control, pais, min_cajas, max_cajas)

    tiempo = resultado["tiempo"]
    total_pedidos = resultado["total_pedidos"]
    productos_diferentes = resultado["productos_diferentes"]
    promedio_marketing = resultado["promedio_marketing"]
    promedio_amount = resultado["promedio_amount"]
    producto_frecuente = resultado["producto_frecuente"]
    frecuencia_maxima = resultado["frecuencia_maxima"]
    pedidos = resultado["pedidos"]

    print(f"\nRequerimiento 2 ejecutado en {tiempo:.2f} milisegundos")
    print(f"Cantidad de pedidos que cumplen el filtro: {total_pedidos}")
    print(f"Cantidad de productos diferentes: {productos_diferentes}")
    print(f"Promedio de Marketing Spend: ${promedio_marketing:.2f}")
    print(f"Promedio de Amount: ${promedio_amount:.2f}")
    print(f"Producto más frecuente: {producto_frecuente}")
    print(f"Cantidad de pedidos de ese producto: {frecuencia_maxima}")

    if total_pedidos == 0:
        print("\nNo se encontraron pedidos con los parámetros ingresados")
        return

    if total_pedidos > 20:
        print(f"\nSe muestran los primeros 10 y últimos 10 pedidos de {total_pedidos}")

    for pos in range(lt.size(pedidos)):
        pedido = lt.get_element(pedidos, pos)

        print(f"\nOrder_ID: {pedido['Order_ID']}")
        print(f"Product: {pedido['Product']}")
        print(f"Channel: {pedido['Channel']}")
        print(f"Order_Date: {pedido['Order_Date']}")
        print(f"Boxes_Shipped: {pedido['Boxes_Shipped']}")
        print(f"Price_per_Box: ${pedido['Price_per_Box']:.2f}")
        print(f"Marketing_Spend: ${pedido['Marketing_Spend']:.2f}")
        print(f"Amount: ${pedido['Amount']:.2f}")



def print_req_3(control):
    """
    Función que imprime la solución del Requerimiento 3 en consola
    """
    fechaPedido = input("Ingrese la fecha del pedido (YYYY-MM-DD): ")
    valor_min = float(input("Ingrese el valor mínimo de costo total: "))
    valor_max = float(input("Ingrese el valor máximo de costo total: "))

    tiempo, count, amount_total, marketing_total, aporte_total, pedidos = logic.req_3(control, fechaPedido, valor_min, valor_max)

    print(f"\nRequerimiento 3 ejecutado en {tiempo:.2f} milisegundos")
    print(f"Cantidad de pedidos que cumplen el filtro: {count}")
    print(f"Monto total recaudado: ${amount_total:.2f}")
    print(f"Total inversión en mercadeo: ${marketing_total:.2f}")
    print(f"Aporte comercial total: ${aporte_total:.2f}")

    if count == 0:
        print("\nNo se encontraron pedidos con los parámetros ingresados")
        return

    if count > 20:
        print(f"\nSe muestran los primeros 10 y los últimos 10 pedidos de {count}")

    for pos in range(0, lt.size(pedidos)):
        if count > 20 and pos >= 10 and pos < count - 10:
            continue
        pedido = lt.get_element(pedidos, pos)
        print(f"\nOrder_ID: {pedido['Order_ID']}")
        print(f"Product: {pedido['Product']}")
        print(f"Country: {pedido['Country']}")
        print(f"Order_Date: {pedido['Order_Date']}")
        print(f"Marketing_Spend: ${pedido['Marketing_Spend']:.2f}")
        print(f"Boxes_Shipped: {pedido['Boxes_Shipped']}")
        print(f"Amount: ${pedido['Amount']:.2f}")
        print(f"Aporte comercial: ${pedido['Aporte_Comercial']:.2f}")


def print_req_4(control):
    """
    Función que imprime la solución del Requerimiento 4 en consola
    """
    producto = input("Ingrese el producto (Product): ")
    pais = input("Ingrese el país (Country): ")

    resultado = logic.req_4(control, pais, producto)

    if resultado is None:
        print("\nNo se encontraron pedidos con los parámetros ingresados")
        return

    tiempo, count, prom_box, prom_disc, prom_mark, prom_box_ship, amount1, amount2 = resultado

    print(f"\nRequerimiento 4 ejecutado en {tiempo:.2f} milisegundos")
    print(f"Cantidad de pedidos que cumplen el filtro: {count}")
    print(f"Precio promedio por caja (Price_per_Box): ${prom_box:.2f}")
    print(f"Promedio de descuento (Discount_Pct): {prom_disc * 100:.2f}%")
    print(f"Promedio de Marketing Spend: ${prom_mark:.2f}")
    print(f"Promedio de Cajas Despachadas (Boxes_Shipped): {prom_box_ship:.2f}")

    if amount1 is not None:
        print("\nPedido con mayor Amount:")
        print(f"Order_ID: {amount1['ID']}")
        print(f"Canal: {amount1['channel']}")
        print(f"Fecha: {amount1['date']}")
        print(f"Cajas enviadas: {amount1['box_ship']}")
        print(f"Monto (Amount): ${amount1['amount']:.2f}")

    if amount2 is not None:
        print("\nSegundo pedido con mayor Amount:")
        print(f"Order_ID: {amount2['ID']}")
        print(f"Canal: {amount2['channel']}")
        print(f"Fecha: {amount2['date']}")
        print(f"Cajas enviadas: {amount2['box_ship']}")
        print(f"Monto (Amount): ${amount2['amount']:.2f}")


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    n = int(input("Ingrese el número N de productos a listar: "))
    pais = input("Ingrese el país: ")
    fecha_inicio = input("Ingrese la fecha inicial (YYYY-MM-DD): ")
    fecha_fin = input("Ingrese la fecha final (YYYY-MM-DD): ")

    if n <= 0:
        print("El número de productos debe ser mayor que cero")
        return

    if fecha_inicio > fecha_fin:
        print("La fecha inicial no puede ser mayor que la final")
        return

    resultado = logic.req_5(
        control, n, pais, fecha_inicio, fecha_fin
    )

    tiempo = resultado["tiempo"]
    total_pedidos = resultado["total_pedidos"]
    total_productos = resultado["total_productos"]
    recaudo_total = resultado["recaudo_total"]
    top_productos = resultado["top_productos"]

    print(f"\nRequerimiento 5 ejecutado en {tiempo:.2f} milisegundos")
    print(f"Cantidad de pedidos que cumplen el filtro: {total_pedidos}")
    print(f"Cantidad de productos diferentes: {total_productos}")
    print(f"Amount total de los pedidos filtrados: ${recaudo_total:.2f}")

    if total_pedidos == 0:
        print("\nNo se encontraron pedidos con los parámetros ingresados")
        return

    print(f"\nTop {lt.size(top_productos)} productos con mayor recaudo:")

    for pos in range(lt.size(top_productos)):
        producto = lt.get_element(top_productos, pos)

        print(f"\nPosición: {pos + 1}")
        print(f"Product: {producto['Product']}")
        print(f"Cantidad de pedidos: {producto['numero_pedidos']}")
        print(f"Total de cajas enviadas: {producto['total_cajas']}")
        print(f"Recaudo total: ${producto['recaudo_total']:.2f}")
        print(f"Precio promedio por caja: ${producto['precio_promedio']:.2f}")
        print(f"Descuento promedio: {producto['descuento_promedio']:.2f}%")
        print(f"Marketing total: ${producto['marketing_total']:.2f}")


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
        
        elif int(inputs) == 8:
            print_data(control, None)
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
