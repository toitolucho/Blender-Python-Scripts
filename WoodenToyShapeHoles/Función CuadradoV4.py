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
    





