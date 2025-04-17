import json
import os

def find_files(folder_path):
    global dreima_files
    files = os.listdir(folder_path)
    dreima_files = [f for f in files if f.endswith(".3ma")]
    convert(folder_path)

def convert(skript_dir):
    for i in range (0, len(dreima_files)):
        thisfile = os.path.join(skript_dir, dreima_files[i])

        file_3ma = open(thisfile)
        fjile_3ma = json.loads(file_3ma.read())

        base_name, _ = os.path.splitext(thisfile)
        obj_file = open(f"{base_name}.obj", "wt")

        vertex_index = 0
        prev_vertex_index = vertex_index

        forward = 0
        meshes = fjile_3ma["meshes"]
        mesh_num = len(meshes)

        for msh in range(mesh_num):

            obj_file.write("\ng \n")
            preciseFactor = meshes[msh]["preciseFactor"]
            prev_vertex_index = vertex_index
            for vtx in range(0, len(meshes[msh]["_positions"]), 3):
                _pos_0 = meshes[msh]["_positions"][vtx] / preciseFactor
                _pos_1 = meshes[msh]["_positions"][vtx + 1] / preciseFactor
                _pos_2 = (meshes[msh]["_positions"][vtx + 2] * -1) / preciseFactor
                vtx_string = "v " + str(_pos_0) + " " + str(_pos_1) + " " + str(_pos_2) + "\n"
                obj_file.write(vtx_string)
                vertex_index = vertex_index + 1

            if msh > 0:
                forward = 1

            UnivertsList = meshes[msh]["facesUnivertsList"]
            obj_file.write("\ng name" + str(msh) + " \n")

            for fcx in UnivertsList:
                obj_file.write("f")

                for fcx_ndx in fcx["u"]:
                    obj_file.write(" " + str(fcx_ndx + 1 + (forward * prev_vertex_index)))

                obj_file.write("\n")

        file_3ma.close()
        obj_file.close()

    try:
        print(f"\nCoverted {i+1} Files successfully!")
    
    except:
        print("\nConverted no files!")
