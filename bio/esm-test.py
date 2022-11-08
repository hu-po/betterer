import torch
import esm
import matplotlib.pyplot as plt
import biotite.structure.io as bsio
from Bio.PDB import MMCIFParser
from Bio import SeqIO

# 650M parameters - Over 1GB of memory
# model, alphabet = esm.pretrained.esm2_t33_650M_UR50D()

# 8M parameters 0 - 29MB
model, alphabet = esm.pretrained.esm2_t6_8M_UR50D()

print(f"Length of alphabet is {len(alphabet)}")

batch_converter = alphabet.get_batch_converter()
model.eval().cuda()

# E-Coli residue sequences (FASTA)
# It seems that "single-letter residue sequence strings" the same thing as FASTA
# The "M" in the FASTA file is the start codon, the start codon always codes for methionine in eukaryotes
test_batch = [
    ("LexA Repressor", "MKALTARQQEVFDLIRDHISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSGASRGIRLLQEEEEGLPLVGRVAADEPLLAQQHIEGHYQVDPSLFKPNADFLLRVSGMSMKDIGIMDGDLLAVHKTQDVRNGQVVVARIDDEVTVKRLKKQGNKVELLPENSEFKPIVVDLRQQSFTIEGLAVGVIRNGDWL"),
    ("LexA Repressor Masked", "MKAL<mask>ARQQEVFDLIRDHISQTGMPPTRAEIAQRLGFRSPNAAEEHLKALARKGVIEIVSGASRGIRLLQEEEEGLPLVGRVAADEPLLAQQHIEGHYQVDPSLFKPNADFLLRVSGMSMKDIGIMDGDLLAVHKTQDVRNGQVVVARIDDEVTVKRLKKQGNKVELLPENSEFKPIVVDLRQQSFTIEGLAVGVIRNGDWL"),
    # ("Random GitHub Protein", "LEU LEU HIS LEU ALA PRO VAL LEU LEU ARG PRO STOP HIS LEU ILE VAL HIS HIS GLY")
]
test_batch += [(f"1JHF part {i}", res.seq) for i, res in enumerate(SeqIO.parse("1jhf.pdb", "pdb-atom"))]
# https://www.rcsb.org/structure/1K6F
test_batch += [(f"1K6F part {i}", res.seq) for i, res in enumerate(SeqIO.parse("1k6f.cif", "cif-atom"))]

batch_labels, batch_strs, batch_tokens = batch_converter(test_batch)

print("\n\n\n\n")
print(test_batch)
print("\n\n\n\n")

# Extract per-residue representations (on GPU)
with torch.no_grad():
    results = model(batch_tokens.cuda(), repr_layers=[6], return_contacts=True)
token_representations = results["representations"][6]

print(f"Results includes {str(results.keys())}")
print(f"Token representation shape {token_representations.shape}")


sequence_representations = []
for i, (_, seq) in enumerate(test_batch):
    # Remove the start and end tokens
    sequence_representations.append(
        token_representations[i, 1: len(seq) + 1].mean(0))

print(f"Sequence representation shape {sequence_representations[0].shape}")

for (_, seq), attention_contacts in zip(test_batch, results["contacts"]):
    # Remove the start and end tokens
    attention_contacts = attention_contacts[: len(seq), : len(seq)]
    plt.figure(figsize=(10, 10))
    plt.imshow(attention_contacts.cpu().numpy())
    plt.title(seq)
    plt.show()

# Folding for structure prediction
# fold_model = esm.pretrained.esmfold_v1()
