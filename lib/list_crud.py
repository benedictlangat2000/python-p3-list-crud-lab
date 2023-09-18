def create_an_empty_list():
    return []  # This function should work correctly.

def create_a_list():
    return [1, 2, 3, 4]  # This function should work correctly.

def add_element_to_end_of_list(l, element):
    l.append(element)  # This function should work correctly.
    return l

def add_element_to_start_of_list(l, element):
    l.insert(0, element)  # This function should work correctly.
    return l

def remove_element_from_end_of_list(l):
    l.pop()  # This function should work correctly.
    return l

def remove_element_from_start_of_list(l):
    del l[0]  # This function should work correctly.
    return l

def retrieve_first_element_from_list(l):
    return l[0]  # This function should work correctly.

def retrieve_element_from_index(l, index):
    return l[index]  # This function should work correctly.

def retrieve_last_element_from_list(l):
    return l[-1]  # This function should work correctly.
