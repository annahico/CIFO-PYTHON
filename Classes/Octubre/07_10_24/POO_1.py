# Escribir una clase en python con 2 métodos: get_string y print_string. get_string acepta una cadena ingresada por el usuario y print_string imprime la cadena en mayúsculas.

class cadena:
    def __init__(self,cadena) -> None: # Aquest mètode és el constructor de la classe. Inicialitza l'objecte amb una cadena de text (cadena) que es passa com a argument al crear un objecte de la classe.
        self.cadena = cadena
        pass
    def get_string(self): #  Aquest mètode simplement retorna el valor de la cadena que ha estat guardada a l'atribut cadena de l'objecte. 
        return self.cadena
    
    def set_string(self,new_cadena):
        self.cadena = new_cadena

    def print_string(self): # Aquest mètode imprimeix la cadena en el seu format original (sense modificar-la).
        print(self.cadena)

    def quitaespacios(self):
        self.cadena = self.cadena.replace("" "","")

    def listadepalabras(self,caracter):
        lista = self.cadena.split(caracter)
        return lista

    def longitud(self): # Aquest mètode calcula la longitud de la cadena (nombre de caràcters que conté) utilitzant la funció integrada len() de Python i retorna aquest valor.
        return len(self.cadena)

    def __str__(self) -> str: # imprimeix un missatge personalitzat
        return f"La cadena tiene este valor: {self.cadena}"
        pass

c1= cadena("Soy tu primera cadena") # creado el objeto c1 que es la cadena 1
c1.print_string()
print(c1.longitud())
c1.set_string("Hola")
print(c1)
c1.print_string()
print("c1.longitud: ", c1.longitud())
print("c1.__str__()",c1.__str__())
print(c1.cadena)
c1.cadena = "Te he canviado accediendo a la variable cadena de init"
print("c1", c1)
print("c1.longitud: ", c1.longitud())
print("c1.__str__()",c1.__str__())
c1.quitaespacios()
print("c1", c1)
c1.print_string()
print("c1.longitud", c1.longitud())
print("c1.__str__()",c1.__str__())
print(c1.listadepalabras)
