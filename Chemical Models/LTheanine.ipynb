import rdkit
from rdkit import Chem
from rdkit.Chem import AllChem, Draw
from rdkit.Chem.Draw import IPythonConsole
import py3Dmol

l_theanine_smiles = 'C[C@@H](CC(=O)O)NC(=O)CCN'


mol = Chem.MolFromSmiles(l_theanine_smiles)
mol = Chem.AddHs(mol)  

AllChem.EmbedMolecule(mol, AllChem.ETKDG())

def visualize_molecule(mol):
    block = Chem.MolToMolBlock(mol)
    viewer = py3Dmol.view(width=800, height=600)
    viewer.addModel(block, 'mol')
    viewer.setStyle({'stick': {}})
    viewer.zoomTo()
    return viewer.show()

visualize_molecule(mol)

with open("l_theanine.pdb", "w") as f:
    f.write(Chem.MolToPDBBlock(mol))

print("Molecule prepared and saved for docking.")
