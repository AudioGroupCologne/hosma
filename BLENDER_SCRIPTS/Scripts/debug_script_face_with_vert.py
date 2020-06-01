import bpy

current_obj = bpy.context.active_object

print("="*40) # printing marker
for polygon in current_obj.data.polygons:
    verts_in_face = polygon.vertices[:]
    #print("face index", polygon.index)
    for vert in verts_in_face:
        if(vert == 1):
            print("face index", polygon.index)
            for vert in verts_in_face:
                print("vert", vert, " vert co", current_obj.data.vertices[vert].co)