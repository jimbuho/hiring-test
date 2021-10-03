"""

Un Stack o Pila: el primer elemento en entrar es el primero en salir.

Nota: En el siguiente codigo hay cuatro lineas que deben corregirse
para que las tres pruebas sean superadas 

"""

class Stack:
    
    def __init__(self, initial_items=[]):
        self.items = initial_items
        
    def shift(self):
        self.items = self.items[1:]
        return self.items[0]
    
    def push(self, item):
        self.items.append(item)
    
    def printit(self):
        return str(self.items)

class TestStack:

    def test_stack(self):
        """ Stack Test of numbers from 1 to 5 """
        expected = str([i+1 for i in range(5)])

        queue = Stack([1,2,3])
        
        for i in range(3,5):
            queue.push(i)

        assert queue.printit() == expected, "Should be {}".format(expected)

    def test_destack(self):
        """ Stack of numbers from 1000 and de-Stack of a set of numbers """
        expected = str([1000+(i*10) for i in range(4)])
    
        queue = Stack()
        
        for i in range(4):
            queue.push(1000+(i*10))
        
        item = queue.shift()        
        assert queue.printit() == expected, "Should be {}".format(expected)
        assert item == 1000, "Should be 1000"
