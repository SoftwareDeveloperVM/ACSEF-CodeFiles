import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem
import py3Dmol

l_theanine_smiles = 'C[C@@H](CC(=O)O)NC(=O)CCN'

mol = Chem.MolFromSmiles(l_theanine_smiles)
mol = Chem.AddHs(mol) 

AllChem.EmbedMolecule(mol, AllChem.ETKDG())

def visualize_molecule(mol, viewer):
    block = Chem.MolToMolBlock(mol)
    viewer.addModel(block, 'mol')
    viewer.setStyle({'stick': {}})
    viewer.zoomTo()

def load_nmdareceptor_pdb(file_path):
    with open(file_path, "r") as f:
        return f.read()

def visualize_nmdareceptor_and_ltheanine():
    viewer = py3Dmol.view(width=800, height=600)

    nmdareceptor_pdb = load_nmdareceptor_pdb("8v14.pdb")
    viewer.addModel(nmdareceptor_pdb, 'pdb')

    visualize_molecule(mol, viewer)

    viewer.setStyle({'model': 0, 'cartoon': {'color': 'rainbow'}})
    viewer.setStyle({'model': 1, 'stick': {}})

    viewer.zoomTo()

    return viewer.show()

visualize_nmdareceptor_and_ltheanine()
