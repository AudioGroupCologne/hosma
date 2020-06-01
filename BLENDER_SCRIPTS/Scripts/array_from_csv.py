import bpy,csv, bmesh

#Programm Parameters
csv_path = 'C:\Aurames\input.csv'
mic_object_path = 'C:\Aurames\Objects\mic_for_boolean.obj'
#Objects used:  mic_for_boolean.obj   halterung.obj    mic_model_git.obj

#Open csv File and extract xyz coordinate
with open(csv_path, newline='') as f:
    reader = csv.DictReader(f)
    xyz = []
    for row in reader:
        temp = {'X' : 0,'Y' : 0,'Z' : 0}
        temp['X']=float(row['X'])
        temp['Y']=float(row['Y'])
        temp['Z']=float(row['Z'])

        xyz.append(temp)

#Create an Empty Object as target for Constraint
bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
bpy.context.active_object.name = 'constraint_origin'

#Generate Mesh for each set of xyz coordinates
for co in xyz:
    #create_microphone_mesh()
    bpy.ops.object.select_all(action='DESELECT')
    imported_object = bpy.ops.import_scene.obj(filepath=mic_object_path)
    bpy.context.view_layer.objects.active = bpy.context.selected_objects[0]
    
    bpy.context.object.location[0] = co['X']
    bpy.context.object.location[1] = co['Y']
    bpy.context.object.location[2] = co['Z']

    bpy.ops.object.constraint_add(type='DAMPED_TRACK')
    bpy.context.object.constraints["Damped Track"].track_axis = 'TRACK_Y'
    bpy.context.object.constraints["Damped Track"].target = bpy.data.objects["constraint_origin"]

#Create vertex at 0 0 0
bpy.ops.object.select_all(action='DESELECT')
mesh = bpy.data.meshes.new("meshdata")
obj = bpy.data.objects.new("grid_origin", mesh)
bpy.context.scene.collection.objects.link(obj)
obj.select_set(True)

#Create vertex at Write Vertex
bm = bmesh.new()
vert = (0, 0, 0)
bm.verts.new(vert)
bm.to_mesh(mesh)
bm.free()

#Join grid
bpy.ops.object.select_all(action='SELECT')
bpy.context.view_layer.objects.active = obj
bpy.ops.object.join()

#Delete Empty Constraint Object
bpy.ops.object.select_all(action='DESELECT')
bpy.data.objects['constraint_origin'].select_set(True)
bpy.ops.object.delete()

#Create Vertice cloud from coordinates
bpy.ops.object.select_all(action='DESELECT')
mesh = bpy.data.meshes.new("vertex_cloud_data")
obj = bpy.data.objects.new("vertex_cloud", mesh)
bpy.context.scene.collection.objects.link(obj)
obj.select_set(True)

bm = bmesh.new()

for co in xyz:
    vert = (co['X'], co['Y'], co['Z'])
    print(vert)
    bm.verts.new(vert)
    
bm.to_mesh(mesh)
bm.free()

