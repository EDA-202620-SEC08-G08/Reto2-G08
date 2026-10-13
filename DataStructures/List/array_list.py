def new_list():
    new_list ={
    "elements": [],
    "size":0,
    }
    
    return new_list

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list

def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def size(my_list):

    return my_list["size"]

def first_element(my_list):
    if my_list["size"] == 0:
        raise Exception("IndexError: list index out of range")

    return my_list["elements"][0]

def is_empty(my_list):
    return my_list["size"] == 0

def last_element(my_list):
    if my_list["size"] == 0:
        raise Exception("IndexError: list index out of range")
    
    return my_list["elements"][-1]

def get_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise Exception("IndexError: list index out of range")

    return my_list["elements"][pos]

def is_present(my_list, element, cmp_function):
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0, size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise Exception("IndexError: list index out of range")
    else:
        my_list["elements"].pop(pos)
        my_list["size"] -= 1
        return my_list

def remove_first(my_list):
    if my_list["size"] == 0:
        if my_list["size"] == 0:
            raise Exception("IndexError: list index out of range")
    else:
        element = my_list["elements"].pop(0)
        my_list["size"] -= 1
        return element

def remove_last(my_list):
    if my_list["size"] == 0:
        if my_list["size"] == 0:
            raise Exception("IndexError: list index out of range")
    else:
        element = my_list["elements"].pop()
        my_list["size"] -= 1
        return element

def insert_element(my_list, pos, element):
    if pos < 0 or pos > my_list["size"]:
        raise Exception("IndexError: list index out of range")
    else:
        my_list["elements"].insert(pos, element)
        my_list["size"] += 1
        return my_list

def change_info(my_list, pos, new_element):
    if pos < 0 or pos >= my_list["size"]:
         raise Exception("IndexError: list index out of range")
        
    else:
        my_list["elements"][pos] = new_element
        return my_list
    
def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= my_list["size"] or pos2 < 0 or pos2 >= my_list["size"]:
         raise Exception("IndexError: list index out of range")
    else:
        my_list["elements"][pos1], my_list["elements"][pos2] = my_list["elements"][pos2], my_list["elements"][pos1]
        return my_list

def sub_list(my_list, pos, size):
    if pos < 0 or pos >= my_list["size"] or size < 0 or pos + size > my_list["size"]:
         raise Exception("IndexError: list index out of range")
    else:
        sub_list = {
            "elements": my_list["elements"][pos:pos + size],
            "size": size
        }
        return sub_list

    