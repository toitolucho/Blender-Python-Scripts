

### Shapes Generator with blender Wooden Toys
![Objetivo a crear randomicamente](/WoodenToyShapeHoles/images/Example.png)

- Creating basic shapes 
- Using Boolean Modifier to create holes in the shapes
- Using Vectors to create colors
- Using Random assignments to colors and positions of the shapes

#### Basic Shapes Creation
Instrucciones asociadas a la creación de un cubo y un rectangulo
[Creación de la figura Cuadrado](https://youtu.be/rvrC9p7qHP0 "Creación de la figura Cuadrado")
```python
bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(0.5, 0.5, 0), scale=(1, 1, 0.2))
bpy.ops.transform.translate(value=(0, 0, 0.1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

bpy.ops.mesh.primitive_cube_add(size=1, enter_editmode=False, align='WORLD', location=(0.5, 0.75, 0), scale=(1, 1.5, 0.2))
bpy.ops.transform.translate(value=(0, 0, 0.1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
```
#### First steps to create a Cuabe Creator Function
En un bucle se invoca a la función creada para poder distribuir las figuras en forma de gradas([Video](https://youtu.be/rjI7C2wgtvw "Video"))
```python
import bpy

def crearCuadrado(x,y,z):
    bpy.ops.mesh.primitive_cube_add(size=1, location=(x,y,z), scale=(1, 1, 0.2))
    bpy.ops.transform.translate(value=(0, 0, 0.1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)    

def crearCuadrado2(posicion):
    bpy.ops.mesh.primitive_cube_add(size=1, location=posicion, scale=(1, 1, 0.2))
    bpy.ops.transform.translate(value=(0, 0, 0.1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)    

for i in range(0,5):
    crearCuadrado(0,i, i*2 )
    crearCuadrado2((0,-i, -i*2))

```
![Objetivo a crear randomicamente](/WoodenToyShapeHoles/images/CuadradosFunciones.png)

#### Steps to create the first hole with Boolean Modifier
Con el Modificador Boolean de Blender se automatizará la creación de los huecos de las figuras. [Video](https://youtu.be/e72Z9VV9Fk0 "Video")
```python
import bpy
bpy.ops.mesh.primitive_cylinder_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.transform.resize(value=(0.298459, 0.298459, 0.298459), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.mesh.primitive_cube_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
bpy.ops.transform.resize(value=(1, 1, 0.113995), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.object.modifier_add(type='BOOLEAN')
bpy.context.object.modifiers["Boolean"].object = bpy.data.objects["Cylinder"]
bpy.ops.object.modifier_apply(modifier="Boolean")
bpy.ops.transform.translate(value=(-0.138469, 1.4649, -0.15619), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.select_all(action='DESELECT')
```
![Objetivo a crear randomicamente](/WoodenToyShapeHoles/images/CuadradoHueco.png)

#### Repeting Hole's code for creating the rest Holes.
```python
import bpy

def crearCuadrado(posicion):
    bpy.ops.mesh.primitive_cylinder_add( location=posicion, scale=(0.14, 0.14, 0.5))
    #bpy.ops.transform.resize(value=(0.298459, 0.298459, 0.298459), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
    bpy.ops.transform.translate(value=(-0.25, -0.25, 0))
    cilindro = bpy.context.active_object
    
    bpy.ops.mesh.primitive_cube_add(size=1, location=posicion, scale=(1, 1, 0.2))
    bpy.ops.transform.translate(value=(0, 0, 0.1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)    
    cuadrado  = bpy.context.active_object

    bpy.ops.object.select_all(action='DESELECT')
    cuadrado.select_set(True)
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[cilindro.name]
    bpy.ops.object.modifier_apply(modifier="Boolean")
    #cilindro.hide_viewport = True
    
    bpy.ops.object.select_all(action='DESELECT')
    cilindro.select_set(True)
    bpy.ops.transform.translate(value=(0.5, 0, 0))
    
    bpy.ops.object.select_all(action='DESELECT')
    cuadrado.select_set(True)
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[cilindro.name]
    bpy.ops.object.modifier_apply(modifier="Boolean")
    
    
    bpy.ops.object.select_all(action='DESELECT')
    cilindro.select_set(True)
    bpy.ops.transform.translate(value=(0, 0.5, 0))
    
    bpy.ops.object.select_all(action='DESELECT')
    cuadrado.select_set(True)
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[cilindro.name]
    bpy.ops.object.modifier_apply(modifier="Boolean")
    
    bpy.ops.object.select_all(action='DESELECT')
    cilindro.select_set(True)
    bpy.ops.transform.translate(value=(-0.5, 0, 0))
    
    bpy.ops.object.select_all(action='DESELECT')
    cuadrado.select_set(True)
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[cilindro.name]
    bpy.ops.object.modifier_apply(modifier="Boolean")
    
    
    cilindro.hide_viewport = True
    bpy.ops.object.select_all(action='DESELECT')
    cilindro.select_set(True)
    #bpy.ops.object.delete(use_global=False)


for i in range (0,3):
    crearCuadrado((i*2,0,0))    
```


#### Refactoring with Hole creator Function
```python
import bpy

def crearAgujero(cilindro, figura, posicion):
    bpy.ops.object.select_all(action='DESELECT')
    cilindro.select_set(True)
    bpy.ops.transform.translate(value=posicion)
    
    #bpy.ops.object.select_all(action='DESELECT')
    cilindro.select_set(False)
    figura.select_set(True)
    bpy.ops.object.modifier_add(type='BOOLEAN')
    bpy.context.object.modifiers["Boolean"].object = bpy.data.objects[cilindro.name]
    bpy.ops.object.modifier_apply(modifier="Boolean")

def crearCuadrado(posicion):
    bpy.ops.mesh.primitive_cylinder_add( location=posicion, scale=(0.14, 0.14, 0.5))    
    cilindro = bpy.context.active_object

    
    
    bpy.ops.mesh.primitive_cube_add(size=1, location=posicion, scale=(1, 1, 0.2))
    bpy.ops.transform.translate(value=(0, 0, 0.1), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', constraint_axis=(False, False, True), mirror=True, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)       
    cuadrado  = bpy.context.active_object

    crearAgujero(cilindro, cuadrado,(-0.25, -0.25, 0))
    crearAgujero(cilindro, cuadrado,(0.5, 0, 0))
    crearAgujero(cilindro, cuadrado,(0, 0.5, 0))
    crearAgujero(cilindro, cuadrado,(-0.5, 0, 0))
    
    
    #cilindro.hide_viewport = True
    bpy.ops.object.select_all(action='DESELECT')
    cilindro.select_set(True)
    bpy.ops.object.delete(use_global=False)


for i in range (0,3):
    crearCuadrado((i*2,0,0))    
     
```

![Objetivo a crear randomicamente](/WoodenToyShapeHoles/images/CuadradosHuecos.png)
