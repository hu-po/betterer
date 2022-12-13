import torch
import csv
import gc
import esm
import argparse


# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Define command line arguments
parser.add_argument("--batch_size", type=int, default=2)
parser.add_argument("--csv_input_file", type=str, default="train_filtered.csv")
parser.add_argument("--csv_output_file", type=str,
                    default="train_filtered_encoded.csv")
parser.add_argument("--model", type=str, default="esm1v_t33_650M_UR90S_5")


def encode_sequence_batch(model, alphabet, device, sequence_batch, repr_layers=33):
    """Encode a batch of sequences using the ESM-2 model."""

    # Print the shape of the sequence_batch
    # print(f"Sequence batch size: {len(sequence_batch)}")
    # print(f"Individual sequence shape: {len(sequence_batch[0])}")

    # Prepare data (first 2 sequences from ESMStructuralSplitDataset superfamily / 4)
    batch_converter = alphabet.get_batch_converter()
    batch_labels, batch_strs, batch_tokens = batch_converter(sequence_batch)
    batch_lens = (batch_tokens != alphabet.padding_idx).sum(1)

    # Extract per-residue representations
    with torch.no_grad():
        results = model(batch_tokens.to(device),
                        repr_layers=[repr_layers],
                        return_contacts=True)
    token_representations = results["representations"][repr_layers]

    # Generate per-sequence representations via averaging
    # NOTE: token 0 is always a beginning-of-sequence token, so the first residue is token 1.
    sequence_representations = []
    for i, tokens_len in enumerate(batch_lens):
        sequence_representations.append(
            token_representations[i, 1: tokens_len - 1].mean(0))

    encoded_sequences = [seq.cpu().numpy() for seq in sequence_representations]

    print(f"Converted sequences {sequence_batch} into {encoded_sequences}")
    print(f"Encoded sequences shape: {encoded_sequences[0].shape}")

    return encoded_sequences


if __name__ == "__main__":

    # Parse command line arguments
    args = parser.parse_args()

    # List available CUDA devices
    print(f"Available CUDA devices: {torch.cuda.device_count()}")

    # Print the name of the CUDA devices
    for i in range(torch.cuda.device_count()):
        print(f"Device {i}: {torch.cuda.get_device_name(i)}")

    # Check if a GPU is available
    # device = torch.device("cuda:1" if torch.cuda.is_available() else "cpu")
    device = "cpu"
    print(f"Using device {device}")

    # Clear out any stale data in the GPU
    torch.cuda.empty_cache()

    # Load the ESM models
    if args.model == "esm1v_t33_650M_UR90S_1":
        model, alphabet = esm.pretrained.esm1v_t33_650M_UR90S_1()
        repr_layers = 33
        embedding_size = 1280
        max_sequence_length = 1024
    elif args.model == "esm1v_t33_650M_UR90S_5":
        model, alphabet = esm.pretrained.esm1v_t33_650M_UR90S_5()
        repr_layers = 33
        embedding_size = 1280
        max_sequence_length = 1024
    elif args.model == "esm2_t33_650M_UR50D":
        model, alphabet = esm.pretrained.esm2_t33_650M_UR50D()
        repr_layers = 33
        embedding_size = 1280
        max_sequence_length = 1024 # Made up number
    elif args.model == "esm2_t48_15B_UR50D":
        model, alphabet = esm.pretrained.esm2_t48_15B_UR50D()
        repr_layers = 48
        embedding_size = 1280
        max_sequence_length = 1024 # Made up number

    # Set the model to evaluation mode
    model.eval()
    model.to(device)

    with open(args.csv_input_file, 'r') as csv_input_file:
        with open(args.csv_output_file, 'w') as csv_output_file:

            reader = csv.reader(csv_input_file)
            headers = next(reader)

            writer = csv.writer(csv_output_file)
            # Headers for the encoded sequences
            writer.writerow(["seq_id"] + [f"latent_{i}" for i in range(embedding_size)])

            sequence_batch = []
            for i, line in enumerate(reader):

                print(f"Processing line {i} for {args.model}...")

                # seq_id,protein_sequence,pH,data_source,tm
                seq_id = line[0]
                protein_sequence = line[1]
                pH = line[2]
                data_source = line[3]
                # tm = line[4]

                # Clip the protein sequence to the maximum sequence length
                protein_sequence = protein_sequence[:max_sequence_length-2]

                # Append the sequence to the sequence batch
                sequence_batch.append((seq_id, protein_sequence))

                # If the sequence batch is full, encode the sequences
                if len(sequence_batch) == args.batch_size:

                    encoded_sequences = encode_sequence_batch(
                        model, alphabet, device, sequence_batch, repr_layers=repr_layers)

                    # Zip the encoded sequences with the sequence IDs
                    for seq_id, encoded_sequence in zip([seq[0] for seq in sequence_batch], encoded_sequences):
                        # Write the encoded sequences to the output file
                        writer.writerow([seq_id] + encoded_sequence.tolist())

                    # Clear the sequence batch
                    sequence_batch = []
                    del encoded_sequences

                    # Clear out any stale data in the GPU
                    gc.collect()
                    torch.cuda.empty_cache()
