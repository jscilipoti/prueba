class prueba1():

    def __init__(self,name):
        self.name = name
        
    @classmethod
    def usando_classmethod(cls,nombre):
        prueba1_object = cls(nombre)
        return prueba1_object



nombre = "jose"
obj1 = prueba1(nombre)
obj2 = prueba1.usando_classmethod(nombre)
print (obj1.name)
print (obj2.name)

