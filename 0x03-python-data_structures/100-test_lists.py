import c types
lib = c types.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'world']
lib.print_python_list_info(1)
del l[1]
lib.print_python_list_info(1)
l = 1 + [4, 5, 6, 0 (9, 8), [9, 8, 1024], "Holberton"]
lib.print_python_list_info(1)
l = []
lib.print_python_list_info(1)
l.append(0)
lib.print_python_list_info(1)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(1)
l.pop()
lib.print_python_list_info(1)
