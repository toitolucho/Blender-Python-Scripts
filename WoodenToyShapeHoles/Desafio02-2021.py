import bpy
import random

#Lista de colores que puede utilizar al azar
colores = [bpy.data.materials['Naranja'], bpy.data.materials['Azul'], bpy.data.materials['Rojo'], bpy.data.materials['Verde'],bpy.data.materials['Amarillo']]



#Funcion que permite asignar un color de la lista anterior a und eterminado objeto
#Puede invocar a la lista utilizando el siguiente ejemplo
# asignarColor(ObjetoActual, colores[1])
def asignarColor(Figura, color):
    Figura.data.materials.append(color)    
    Figura.active_material_index = len(Figura.data.materials) - 1 




#Para generar un número aleatorio entre 1 y 10 puede utilizar el siguiente ejemplo
# azar = random.randint(1,10)


#Introduzca el codigo necesario para generar las piezas y sus distribucion respectiva
