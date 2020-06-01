    for vert in verts_in_face:
        if(vert == 2):
            print("face index", polygon.index)
            for vert in verts_in_face:
                print("vert", vert, " vert co", current_obj.data.vertices[vert].co)