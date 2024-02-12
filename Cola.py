from random import randint, uniform, random
import time

class Cola():

    def __init__(self):
        self.items = []

    def encolar(self, x):
        self.items.append(x)

    def desencolar(self):  
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola esta vacia")
    
    def es_vacia(self):
        return self.items==[]

    def TLlegada(self):

        Tiempo = randint(0, 2)
        return Tiempo

    def TAtn(self):
        Tiempo = randint(0, 2)
        return Tiempo

    def Cual(self):
        return randint(1,2)
        
if __name__ == "__main__":

    c = Cola() 
    Objeto=1
    
    while True:
        if c.Cual()==1 :
            time.sleep(c.TLlegada())
            c.encolar(Objeto)
            Objeto=Objeto+1
        else:
            if c.es_vacia():
                c.encolar(Objeto)
                Objeto=Objeto+1
                time.sleep(c.TLlegada())
            else:
                c.desencolar()
                Objeto = Objeto+1
        print(c.items)
