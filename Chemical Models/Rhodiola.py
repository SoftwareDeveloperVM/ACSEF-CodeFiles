import py3Dmol

def load_pdb(file_path):
    with open(file_path, "r") as f:
        return f.read()

def visualize_pdb(pdb_data):
    viewer = py3Dmol.view(width=800, height=600)
    viewer.addModel(pdb_data, 'pdb')
    viewer.setStyle({'stick': {}})
    viewer.zoomTo()
    viewer.show()

pdb_data = load_pdb("rhodiola.pdb")

visualize_pdb(pdb_data)
