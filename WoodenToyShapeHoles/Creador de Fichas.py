
import bpy




def crear_material(nombre, color):    
    if nombre in bpy.data.materials:
        print("El color : "+ nombre+ " ya existe; changing...")
        mat = bpy.data.materials[nombre]
        mat.diffuse_color = color
        
    else:        
        try:

            mat = bpy.data.materials.new(name=nombre)
            mat.diffuse_color = color            
            mat.diffuse_intensity = 1
            

            
            print("El color " + nombre+" ha sido creado satisfactoriamente")
            
        except:
            print("Ocurrio un problema al crear el material  " + nombre)
    return mat;


def crearHueco(figura, hueco, pos):
    #Hueco 1 - Traslación
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[hueco.name].select_set(True) 
    bpy.ops.transform.translate(value=pos)

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[figura.name].select_set(True) 
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[hueco.name]
    bpy.ops.object.modifier_apply(modifier="Boolean")


def crearRectangulo(x,y,z):
    bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=0.13, depth=1, enter_editmode=False, align='WORLD', location=(x,y,z), scale=(1, 1, 1))
    hueco = bpy.context.active_object
    bpy.ops.mesh.primitive_cube_add(size=1.4, enter_editmode=False, align='WORLD', location=(x, y, x), scale=(1, 1.3, 0.15))
    triangulo = bpy.context.active_object

    
    
    crearHueco(triangulo, hueco, (-0.0, -0.45, 0))
    crearHueco(triangulo, hueco, (0, 0.9, 0))

    

    #Eliminación del cilindro
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[hueco.name].select_set(True) 
    bpy.ops.object.delete() 
    triangulo.name = 'Rectangulo'    
    return triangulo


def crearCuadrado(x,y,z):
    bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=0.13, depth=0.3, enter_editmode=False, align='WORLD', location=(x,y,z), scale=(1, 1, 1))
    hueco = bpy.context.active_object
    bpy.ops.mesh.primitive_cylinder_add(vertices=4, radius=1, depth=0.2, enter_editmode=False, align='WORLD', location=(x,y,z), scale=(1, 1, 1))
    triangulo = bpy.context.active_object
    bpy.ops.transform.rotate(value=0.785398, orient_axis='Z', orient_type='VIEW', orient_matrix=((1, -0, -0), (-0, 1, -0), (-0, 0, 1)), orient_matrix_type='VIEW', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    

        
    
    
    crearHueco(triangulo, hueco, (-0.3, -0.3, 0))
    crearHueco(triangulo, hueco, (0.6, 0, 0))
    crearHueco(triangulo, hueco, (0, 0.6, 0))
    crearHueco(triangulo, hueco, (-0.6, 0, 0))
    

    #Eliminación del cilindro
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[hueco.name].select_set(True) 
    bpy.ops.object.delete() 
    triangulo.name = 'Cuadrado'    
    return triangulo
    



def crearTriangulo(x,y,z):
    bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=0.13, depth=0.3, enter_editmode=False, align='WORLD', location=(x,y,z), scale=(1, 1, 1))
    hueco = bpy.context.active_object
    bpy.ops.mesh.primitive_cylinder_add(vertices=3, radius=1, depth=0.2, enter_editmode=False, align='WORLD', location=(x,y,z), scale=(1, 1, 1))
    triangulo = bpy.context.active_object
    
    
    crearHueco(triangulo, hueco, (-0.3, -0.2, 0))
    crearHueco(triangulo, hueco, (0.6, 0, 0))
    crearHueco(triangulo, hueco, (-0.3, 0.5, 0))    

    #Eliminación del cilindro
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[hueco.name].select_set(True) 
    bpy.ops.object.delete() 
    triangulo.name = 'Triangulo'    
    return triangulo
    

def crearRedondo(x,y,z):
    bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=0.13, depth=0.3, enter_editmode=False, align='WORLD', location=(x,y,z), scale=(1, 1, 1))
    hueco = bpy.context.active_object
    bpy.ops.mesh.primitive_cylinder_add(vertices=26, radius=0.75, depth=0.2, enter_editmode=False, align='WORLD', location=(x,y,z), scale=(1, 1, 1))
    triangulo = bpy.context.active_object
    
    
    crearHueco(triangulo, hueco, (0, -0, 0))
    

    #Eliminación del cilindro
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[hueco.name].select_set(True) 
    bpy.ops.object.delete() 
    triangulo.name = 'Redondo'    
    return triangulo


def crearPentagono(x,y,z):
    bpy.ops.mesh.primitive_cylinder_add(vertices=20, radius=0.13, depth=0.3, enter_editmode=False, align='WORLD', location=(x,y,z), scale=(1, 1, 1))
    hueco = bpy.context.active_object
    bpy.ops.mesh.primitive_cylinder_add(vertices=5, radius=0.9, depth=0.2, enter_editmode=False, align='WORLD', location=(x,y,z), scale=(1, 1, 1))
    triangulo = bpy.context.active_object
    
    
    crearHueco(triangulo, hueco, (-0.4, 0.1, 0))
    crearHueco(triangulo, hueco, (0.8, -0, 0))
    crearHueco(triangulo, hueco, (-0.1, -0.55, 0))
    crearHueco(triangulo, hueco, (-0.55, -0, 0))
    crearHueco(triangulo, hueco, (0.275, 0.8, 0))
    

    #Eliminación del cilindro
    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[hueco.name].select_set(True) 
    bpy.ops.object.delete() 
    triangulo.name = 'Pentagono'
    return triangulo


if len(bpy.data.materials) > 1:
    for i in range(0, len(bpy.data.materials)):
        bpy.data.materials.remove(bpy.data.materials[0])


colores = []
colores.append(crear_material('Rojo', (1.0,0,0,1) ))
colores.append(crear_material('Verde', (0,1,0,1) ))
colores.append(crear_material('Azul', (0,0,1,1) ))

print(len(colores))
print(colores[0])

for y in range(1,2):
    rec = crearRectangulo(0,0,y*0.3)
    rec.data.materials.append(colores[2])
    crearCuadrado(0,2,y*0.3)
    crearRedondo(0,4,y*0.3)
    crearPentagono(0,6,y*0.3)
    t1 =crearTriangulo(0,8,y*0.3)
    print(t1.name)
    t1.data.materials.append(colores[0])
    #t1.data.materials[0] = colores[0]
    t1.active_material_index = len(t1.data.materials) - 1 
    #activeObject.data.materials.append(mat)