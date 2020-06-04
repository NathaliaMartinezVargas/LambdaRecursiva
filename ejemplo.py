import unittest 

def cabeza(lista):
    return lista[0]

def cola(lista):
    return lista[1:] 

def reducir(lista, funcion):
    #Caso base
    if (len(lista) == 1):
        return lista[0]
    #Caso recursivo
    return funcion(cabeza(lista), reducir(cola(lista),funcion))    

def testReducir(self):
    self.assertEquals(20, reducir([3,5,4,8], lambda x, y: x + y))
    self.assertEquals(8, reducir([3,5], lambda x, y: x + y))  

if __name__ == "__main__":
    unittest.main()    