from rdkit import Chem
from rdkit.Chem import Draw
import matplotlib.pyplot as plt

# Test in a kinase inhibitor
mol = Chem.MolFromSmiles("C1CC2=C3C(=CC=C2)C(=CN3C1)[C@H]4[C@@H](C(=O)NC4=O)C5=CNC6=CC=CC=C65")
im = Draw.MolToImage(mol)
fig = plt.figure(figsize=(10,5))
ax = plt.axes(frameon=True)
ax.imshow(im)
ax.axis('off')
plt.show()
