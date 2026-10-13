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
