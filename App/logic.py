import time
import csv
import os
from datetime import datetime

from DataStructures.List import array_list as lt
from DataStructures.Map import map_linear_probing as mlp
from DataStructures.Map import map_separate_chaining as msc

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog={
        "orders": lt.new_list(),
        "OrdenFecha": mlp.new_map(1000, 1),
        "OrdenProdPais": msc.new_map(1000, 4),
        "OrdenMes": mlp.new_map(100, 1),
        "OrdenProd": mlp.new_map(100, 1),
        "OrdenPais": mlp.new_map(100, 1),
        "pedidos_por_canal": mlp.new_map(10, 1),
    }
    return catalog

# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    start_time = get_time()
    csv.field_size_limit(2147483647)
    path=os.path.join("Data", "Data",filename)
    with open(path, encoding="utf-8-sig") as file:
        reader = csv.DictReader(file)
        for row in reader:

            row["Amount"] = float(row["Amount"])
            row["Marketing_Spend"] = float(row["Marketing_Spend"])
            row["Price_per_Box"] = float(row["Price_per_Box"])
            row["Discount_Pct"] = float(row["Discount_Pct"])
            row["Boxes_Shipped"] = int(row["Boxes_Shipped"])

            lt.add_last(catalog["orders"], row)

            # orden por fecha
            fecha = row["Order_Date"]
            lista_fecha = mlp.get(catalog["OrdenFecha"], fecha)
            if lista_fecha is None:
                lista_fecha = lt.new_list()
                mlp.put(catalog["OrdenFecha"], fecha, lista_fecha)
            lt.add_last(lista_fecha, row)

            # orden por producto y pais
            llave = row["Product"] + "-" + row["Country"]
            lista_combo = msc.get(catalog["OrdenProdPais"], llave)
            if lista_combo is None:
                lista_combo = lt.new_list()
                msc.put(catalog["OrdenProdPais"], llave, lista_combo)
            lt.add_last(lista_combo, row)

            # orden por mes
            mes = row["Order_Date"][:7]
            lista_mes = mlp.get(catalog["OrdenMes"], mes)
            if lista_mes is None:
                lista_mes = lt.new_list()
                mlp.put(catalog["OrdenMes"], mes, lista_mes)
            lt.add_last(lista_mes, row)

            # orden por producto
            producto = row["Product"]
            lista_producto = mlp.get(catalog["OrdenProd"], producto)
            if lista_producto is None:
                lista_producto = lt.new_list()
                mlp.put(catalog["OrdenProd"], producto, lista_producto)
            lt.add_last(lista_producto, row)

            # orden por pais
            pais = row["Country"]
            lista_pais = mlp.get(catalog["OrdenPais"], pais)
            if lista_pais is None:
                lista_pais = lt.new_list()
                mlp.put(catalog["OrdenPais"], pais, lista_pais)
            lt.add_last(lista_pais, row)

            # pedidos por canal
            canal = row["Channel"]
            lista_canal = mlp.get(catalog["pedidos_por_canal"], canal)
            if lista_canal is None:
                lista_canal = lt.new_list()
                mlp.put(catalog["pedidos_por_canal"], canal, lista_canal)
            lt.add_last(lista_canal, row)

    end_time = get_time()
    return catalog, delta_time(start_time, end_time)

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
def req_1(catalog, anio, mes, descuento_min, descuento_max):
    """
    Retorna el resultado del requerimiento 1
    """
    def criterio(pedido_1, pedido_2):
        if pedido_1["Discount_Pct"] != pedido_2["Discount_Pct"]:
            return pedido_1["Discount_Pct"] > pedido_2["Discount_Pct"]
        if pedido_1["Amount"] != pedido_2["Amount"]:
            return pedido_1["Amount"] > pedido_2["Amount"]
        return pedido_1["Order_ID"] <= pedido_2["Order_ID"]

    start_time = get_time()

    llave_mes = str(int(anio)).zfill(4) + "-" + str(int(mes)).zfill(2)
    pedidos_mes = mlp.get(catalog["OrdenMes"], llave_mes)

    filtrados = lt.new_list()
    total_amount = 0.0
    suma_precio = 0.0
    suma_cajas = 0

    if pedidos_mes is not None:
        for i in range(lt.size(pedidos_mes)):
            pedido = lt.get_element(pedidos_mes, i)
            descuento = pedido["Discount_Pct"]
            if descuento >= descuento_min and descuento <= descuento_max:
                lt.add_last(filtrados, pedido)
                total_amount += pedido["Amount"]
                suma_precio += pedido["Price_per_Box"]
                suma_cajas += pedido["Boxes_Shipped"]

    total_pedidos = lt.size(filtrados)
    promedio_precio = 0.0
    promedio_cajas = 0.0
    if total_pedidos > 0:
        lt.merge_sort(filtrados, criterio)
        promedio_precio = suma_precio / total_pedidos
        promedio_cajas = suma_cajas / total_pedidos

    end_time = get_time()
    return (delta_time(start_time, end_time), total_pedidos, total_amount,
            promedio_precio, promedio_cajas, filtrados)



def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog, fechaPedido, valor_min, valor_max):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass
def req_6(catalog, n, producto, fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 6
    """
    def criterio(pais_1, pais_2):
        if pais_1["eficiencia"] != pais_2["eficiencia"]:
            return pais_1["eficiencia"] > pais_2["eficiencia"]
        if pais_1["amount_total"] != pais_2["amount_total"]:
            return pais_1["amount_total"] > pais_2["amount_total"]
        return pais_1["Country"] <= pais_2["Country"]

    start_time = get_time()

    pedidos_producto = mlp.get(catalog["OrdenProd"], producto)

    resumen_paises = mlp.new_map(20, 0.5)
    paises_encontrados = lt.new_list()

    total_pedidos = 0
    amount_total = 0.0
    marketing_total = 0.0

    if pedidos_producto is not None:
        for i in range(lt.size(pedidos_producto)):
            pedido = lt.get_element(pedidos_producto, i)
            fecha = pedido["Order_Date"]
            if fecha >= fecha_inicial and fecha <= fecha_final:
                total_pedidos += 1
                amount_total += pedido["Amount"]
                marketing_total += pedido["Marketing_Spend"]

                pais = pedido["Country"]
                resumen = mlp.get(resumen_paises, pais)
                if resumen is None:
                    resumen = {
                        "Country": pais,
                        "num_pedidos": 0,
                        "amount_total": 0.0,
                        "marketing_total": 0.0,
                        "boxes_total": 0,
                        "suma_precio": 0.0,
                        "precio_promedio": 0.0,
                        "eficiencia": 0.0,
                    }
                    mlp.put(resumen_paises, pais, resumen)
                    lt.add_last(paises_encontrados, resumen)

                resumen["num_pedidos"] += 1
                resumen["amount_total"] += pedido["Amount"]
                resumen["marketing_total"] += pedido["Marketing_Spend"]
                resumen["boxes_total"] += pedido["Boxes_Shipped"]
                resumen["suma_precio"] += pedido["Price_per_Box"]

    total_paises = lt.size(paises_encontrados)

    ranking = lt.new_list()
    for i in range(total_paises):
        resumen = lt.get_element(paises_encontrados, i)
        resumen["precio_promedio"] = resumen["suma_precio"] / resumen["num_pedidos"]
        if resumen["marketing_total"] > 0:
            resumen["eficiencia"] = resumen["amount_total"] / resumen["marketing_total"]
            lt.add_last(ranking, resumen)

    lt.merge_sort(ranking, criterio)

    top_paises = lt.new_list()
    limite = lt.size(ranking)
    if n < limite:
        limite = n
    for i in range(limite):
        lt.add_last(top_paises, lt.get_element(ranking, i))

    end_time = get_time()
    return (delta_time(start_time, end_time), total_pedidos, total_paises,
            amount_total, marketing_total, top_paises)



# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
