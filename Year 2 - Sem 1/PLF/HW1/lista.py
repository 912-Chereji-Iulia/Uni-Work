class Nod:
    def __init__(self, e):
        self.e = e
        self.urm = None
    
class Lista:
    def __init__(self):
        self.prim = None
        

'''
crearea unei liste din valori citite pana la 0
'''
def creareLista():
    lista = Lista()
    lista.prim = creareLista_rec()
    return lista

def creareLista_rec():
    x = int(input("x="))
    if x == 0:
        return None
    else:
        nod = Nod(x)
        nod.urm = creareLista_rec()
        return nod
    
'''
tiparirea elementelor unei liste
'''
def tipar(lista):
    tipar_rec(lista.prim)
    
def tipar_rec(nod):
    if nod != None:
        print (nod.e)
        tipar_rec(nod.urm)


'''
EX 13:
    a. Test the inclusion of two sets, represented as lists.
    b. Eliminate all occurrences of an element from a list.
'''


def elim(nod, elem):
    if nod is None:
        return []
    else:
        if nod.e == elem:
            return elim(nod.urm, elem)
        if nod.e != elem:
            return [nod.e] + elim(nod.urm, elem)

def eliminate(lista, elem):
    return elim(lista.prim, elem)

def is_in_list(nod, elem):
    if nod is None:
        return False
    if nod.e == elem:
        return True
    else:
        return is_in_list(nod.urm, elem)

def is_set(nod):
    if nod is None:
        return True
    if is_in_list(nod.urm, nod.e):
        return False
    else:
        return is_set(nod.urm)

def inclusion(nod1, nod2):
    if nod1 is None and nod2 is None:
        return True
    elif nod1 is None and nod2 is not None:
        return True
    elif nod1 is not None and nod2 is None:
        return False
    elif not is_in_list(nod2, nod1.e):
        return False
    else:
        return inclusion(nod1.urm, nod2)

def test_inclusion(lista1,lista2):
    if is_set(lista1.prim) is False or is_set(lista2.prim) is False:
        return "Not sets"
    else:
        return inclusion(lista1.prim, lista2.prim)



'''
program pentru test
'''
        
def main():
    list1 = creareLista()

    print(eliminate(list1, 1))
    list2 = creareLista()
    print(eliminate(list2, 4))
    list3 = creareLista()


    print(test_inclusion(list1, list2))
    print(test_inclusion(list2, list1))
    print(test_inclusion(list1, list3))

main() 
