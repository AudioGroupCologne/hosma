import bpy

current_obj = bpy.context.active_object

print("="*40) # printing marker
i = 0
for vert in current_obj.data.vertices:
    #print("face index", polygon.index)
    print("vert", vert, " vert co", current_obj.data.vertices[i].co)
    i = i+1