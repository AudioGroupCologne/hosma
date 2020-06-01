import bpy,csv

#Programm Parameters
csv_path = 'C:\Aurames\input.csv'
mic_object_path = 'C:\Aurames\Objects\halterung.obj'

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

#Create Vertice cloud from coordinates
verts = []
for co in xyz:
    vert = (co['X'], co['Y'], co['Z'])
    verts.append(vert)
    
mesh_data = bpy.data.meshes.new("outer_shell_data")
mesh_data.from_pydata(verts, [], [])
mesh_data.update()

obj = bpy.data.objects.new("outer_shell", mesh_data)
bpy.context.scene.collection.objects.link(obj)
obj.select = True