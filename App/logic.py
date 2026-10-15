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
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog, fechaPedido, valor_min, valor_max):
    """
    Retorna el resultado del requerimiento 3 utilizando los TADs del proyecto
    y merge_sort para el ordenamiento múltiple.
    """
    start_time = get_time()

    fecha = mlp.get(catalog["ordenFecha"], fechaPedido)
    count = 0
    amount__total = 0
    marketing_spend_total = 0
    aporte_comercial_total = 0

    filtrados = lt.new_list()

    if fecha is not None:
        for pos in range(lt.size(fecha)):
            orden = lt.get_element(fecha, pos)
            
            if valor_min <= orden["Amount"] <= valor_max:
                count += 1
                amount__total += orden["Amount"]
                marketing_spend_total += orden["Marketing_Spend"]
                
                aporte_comercial = orden["Amount"] - orden["Marketing_Spend"]
                aporte_comercial_total += aporte_comercial
                orden["Aporte_Comercial"] = aporte_comercial
                
                # Agregamos a la lista de filtrados
                lt.add_last(filtrados, orden)

    def sort_criteria(orden1, orden2):
        amount1 = float(orden1["Amount"])
        amount2 = float(orden2["Amount"])
        if amount1 != amount2:
            return amount1 > amount2  
        
        ap1 = float(orden1["Aporte_Comercial"])
        ap2 = float(orden2["Aporte_Comercial"])
        if ap1 != ap2:
            return ap1 > ap2 
        
        return orden1["Order_ID"] < orden2["Order_ID"]

    lt.merge_sort(filtrados, sort_criteria)

    resultado_final = lt.new_list()
    total_filtrados = lt.size(filtrados)

    if total_filtrados <= 20:
        resultado_final = filtrados
    else:
        for i in range(10):
            elem = lt.get_element(filtrados, i)
            lt.add_last(resultado_final, elem)
        
        inicio_ultimos = total_filtrados - 10
        for i in range(inicio_ultimos, total_filtrados):
            elem = lt.get_element(filtrados, i)
            lt.add_last(resultado_final, elem)

    end_time = get_time()
    time = delta_time(start_time, end_time)

    return time, count, amount__total, marketing_spend_total, aporte_comercial_total, resultado_final           

    
    


def req_4(catalog, country, product):
    """
    Retorna el resultado del requerimiento 4
    """

    def es_mejor_pedido(orden1, orden2):
        """
        Compara dos pedidos según los criterios del requerimiento.
        """
        if float(orden1["Amount"]) > float(orden2["Amount"]):
            return True

        elif float(orden1["Amount"]) < float(orden2["Amount"]):
            return False

        if float(orden1["Marketing_Spend"]) < float(orden2["Marketing_Spend"]):
            return True

        elif float(orden1["Marketing_Spend"]) > float(orden2["Marketing_Spend"]):
            return False

        return orden1["Order_ID"] < orden2["Order_ID"]

    start_time = get_time()

    llave = product + "-" + country
    orders = msc.get(catalog["OrdenProdPais"], llave)

    count = 0
    prom_box = 0
    prom_disc = 0
    prom_mark = 0
    prom_box_ship = 0

    orden1 = None
    orden2 = None

    if orders is not None:
        for pos in range(0, lt.size(orders)):
            orden = lt.get_element(orders, pos)

            count += 1
            prom_box += float(orden["Price_per_Box"])
            prom_disc += float(orden["Discount_Pct"])
            prom_mark += float(orden["Marketing_Spend"])
            prom_box_ship += int(orden["Boxes_Shipped"])

            if orden1 is None:
                orden1 = orden

            elif es_mejor_pedido(orden, orden1):
                orden2 = orden1
                orden1 = orden

            elif orden2 is None:
                orden2 = orden

            elif es_mejor_pedido(orden, orden2):
                orden2 = orden

    if count == 0:
        return None

    prom_box = prom_box / count
    prom_disc = prom_disc / count
    prom_mark = prom_mark / count
    prom_box_ship = prom_box_ship / count

    amount1 = {
        "ID": orden1["Order_ID"],
        "channel": orden1["Channel"],
        "date": orden1["Order_Date"],
        "box_ship": orden1["Boxes_Shipped"],
        "amount": orden1["Amount"]
    }

    amount2 = None

    if orden2 is not None:
        amount2 = {
            "ID": orden2["Order_ID"],
            "channel": orden2["Channel"],
            "date": orden2["Order_Date"],
            "box_ship": orden2["Boxes_Shipped"],
            "amount": orden2["Amount"]
        }

    end_time = get_time()
    time = delta_time(start_time, end_time)

    return (
        time,
        count,
        prom_box,
        prom_disc,
        prom_mark,
        prom_box_ship,
        amount1,
        amount2
    )


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


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
