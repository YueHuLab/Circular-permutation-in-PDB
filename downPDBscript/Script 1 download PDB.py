from Bio.PDB import PDBList, PDBParser, Select, PDBIO

# Define a class to select the chain
class ChainSelect(Select):
    def __init__(self, chain):
        self.chain = chain

    def accept_chain(self, chain):
        return chain.get_id() == self.chain

# Function to read PDB ID and chain ID from each line of a file
def read_ids(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():  # Skip empty lines
                yield line.strip().split()

# Function to download and save the specific chain
def download_chain(pdb_id, chain_id):
    pdb_list = PDBList()
    pdb_list.retrieve_pdb_file(pdb_id, pdir='.', file_format='pdb')
    parser = PDBParser()
    structure = parser.get_structure(pdb_id, f"pdb{pdb_id.lower()}.ent")
    select = ChainSelect(chain_id)
    io = PDBIO()
    io.set_structure(structure)
    file_name = f"{pdb_id}_{chain_id}.pdb"
    io.save(file_name, select=select)
    print(f"Chain {chain_id} from PDB ID {pdb_id} has been saved as {file_name}")

# Main execution
if __name__ == "__main__":
    # Replace 'input.txt' with your actual file path
    pdbs_list=PDBList()
    pdb_ids = []
    for pdb_id, chain_id in read_ids('name.txt'):
        pdb_ids.append(pdb_id) 
    pdbs_list.download_pdb_files(pdb_ids, pdir='.', file_format='pdb')
    for pdb_id, chain_id in read_ids('name.txt'):
         try: download_chain(pdb_id, chain_id)
         except:
             pass

