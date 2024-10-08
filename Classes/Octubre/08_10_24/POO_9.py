# Ejercicio 9
# Sigue los pasos:
# • Crea  una  clase,  Triangulo.  Su  método  __init__()  debe  tomar  como
# argumentos self, angle1, angle2 y angle3. Asegúrate de establecerlos
# apropiadamente en el cuerpo del método __init__().
# • Crea una variable llamada numero_de_lados y ponla igual a 3.
# • Crea  un  método  llamado  comprobar_angulos.  La  suma  de  los  tres
# ángulos  de  un  triángulo  debe  devolver  True  si  la  suma  de  ángulo1,
# ángulo2 y ángulo3 es igual a 180, y False en caso contrario.
# • Crea  una  variable  llamada  mi_triangulo  y  hazla  igual  a  una  nueva
# instancia  de  tu  clase  Triangulo.  Pásale  tres  ángulos  que  sumen  180
# (por ejemplo, 90, 30, 60).
# • Imprime mi_triangulo.numero_de_lados e imprime
# mi_triangulo.comprobar_angulos().


class Triangulo:
    # Inicialización de la clase con los tres ángulos
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    # Variable de clase para el número de lados
    numero_de_lados = 3

    # Método para comprobar si los ángulos suman 180 grados
    def comprobar_angulos(self):
        return self.angle1 + self.angle2 + self.angle3 == 180


# Crear una instancia de la clase Triangulo con ángulos que suman 180 grados
mi_triangulo = Triangulo(90, 30, 60)

# Imprimir el número de lados del triángulo
print(mi_triangulo.numero_de_lados)

# Comprobar si los ángulos suman 180 grados
print(mi_triangulo.comprobar_angulos())
