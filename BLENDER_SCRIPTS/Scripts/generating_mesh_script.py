#Mircrophone Tube
r_mic = 0.01
h_mic = 0.046
m_mic = 0.003
rm_mic = 0.009

#Generate the Microphone Mesh
def create_microphone_mesh():
    #MeshCreation
    bpy.ops.mesh.primitive_cylinder_add(vertices = 64, radius=r_mic, depth=h_mic-m_mic, enter_editmode=False, location=(0, 0, 0))
    bpy.context.active_object.name = 'mic_body'
    bpy.ops.mesh.primitive_cylinder_add(vertices = 64, radius=rm_mic, depth=m_mic, enter_editmode=False, location=(0, 0, h_mic/2))
    bpy.context.active_object.name = 'mic_head'
    bpy.ops.mesh.primitive_cylinder_add(vertices = 64, radius=rm_mic, depth=0.0, enter_editmode=False, location=(0, 0, h_mic/2))
    bpy.context.active_object.name = 'mic_membrane'
    
    #JoiningMeshesSettingOrigin
    bpy.data.objects['mic_body'].select_set(True)
    bpy.data.objects['mic_head'].select_set(True)
    bpy.data.objects['mic_membrane'].select_set(True)
    bpy.ops.object.join()
    bpy.context.active_object.name = 'mic'