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


