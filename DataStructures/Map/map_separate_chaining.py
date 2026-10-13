from DataStructures.List import array_list as al
from DataStructures.Map import map_functions as mf
from DataStructures.Map import map_entry as me
import random

def new_map(num_elements,load_factor,prime=109345121):
    capacity = mf.next_prime(int(num_elements/load_factor))

    table = al.new_list()
    for i in range(capacity):
        al.add_last(table, al.new_list())

    my_table = {
        "prime": prime,
        "capacity": capacity,
        "scale":random.randint(1,prime-1),
        "shift":random.randint(0,prime-1),
        "table": table,
        "current_factor": 0,
        "limit_factor": load_factor,
        "size": 0
        }
    return my_table

def default_compare(key, entry):
    entry_key = me.get_key(entry)
    if key == entry_key:
        return 0
    elif key > entry_key:
        return 1
    return -1

def put(my_map, key, value):
    hash_value = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map["table"], hash_value)
    pos = al.is_present(bucket, key, default_compare)

    if pos != -1:
        entry = al.get_element(bucket, pos)
        me.set_value(entry, value)
    else:
        entry = me.new_map_entry(key, value)
        al.add_last(bucket, entry)
        my_map["size"] += 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        if my_map["current_factor"] > my_map["limit_factor"]:
            rehash(my_map)
    return my_map

def rehash(my_map):
    new_table = new_map(2 * (my_map["capacity"]), 1, my_map["prime"])
    new_table["limit_factor"] = my_map["limit_factor"]

    old = my_map["table"]
    for i in range(al.size(old)):
        bucket = al.get_element(old, i)
        for j in range(al.size(bucket)):
            entry = al.get_element(bucket, j)
            put(new_table, me.get_key(entry), me.get_value(entry))
    my_map.update(new_table)
    return my_map

def contains(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map["table"], hash_value)
    pos = al.is_present(bucket, key, default_compare)
    return pos != -1

def get(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map["table"], hash_value)
    pos = al.is_present(bucket, key, default_compare)
    if pos != -1:
        entry = al.get_element(bucket, pos)
        return me.get_value(entry)
    return None

def remove(my_map, key):
    hash_value = mf.hash_value(my_map, key)
    bucket = al.get_element(my_map["table"], hash_value)
    pos = al.is_present(bucket, key, default_compare)
    if pos != -1:
        entry = al.get_element(bucket, pos)
        al.delete_element(bucket, pos)
        my_map["size"] -= 1
        my_map["current_factor"] = my_map["size"] / my_map["capacity"]
        return me.get_value(entry)
    return None

def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    return my_map["size"] == 0

def key_set(my_map):
    keys = al.new_list()
    for i in range(al.size(my_map["table"])):
        bucket = al.get_element(my_map["table"], i)
        for j in range(al.size(bucket)):
            entry = al.get_element(bucket, j)
            al.add_last(keys, me.get_key(entry))
    return keys

def value_set(my_map):
    values = al.new_list()
    for i in range(al.size(my_map["table"])):
        bucket = al.get_element(my_map["table"], i)
        for j in range(al.size(bucket)):
            entry = al.get_element(bucket, j)
            al.add_last(values, me.get_value(entry))
    return values
