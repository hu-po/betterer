"""
Train an MLP to predict the melting temperature of a protein sequence.

Command to train the model:
    
python train.py --tren_csv_file train_ready_embeddings_esm2_t33_650M_UR50D.csv --test_csv_file test_ready_embeddings_esm2_t33_650M_UR50D.csv --model_name esm2_t33_650M_UR50D
python train.py --tren_csv_file train_ready_embeddings_esm2_t33_650M_UR50D.csv --test_csv_file test_ready_embeddings_esm2_t33_650M_UR50D.csv --model_name esm2_t33_650M_UR50D
python train.py --tren_csv_file train_ready_embeddings_esm2_t33_650M_UR50D.csv --test_csv_file test_ready_embeddings_esm2_t33_650M_UR50D.csv --model_name esm2_t33_650M_UR50D
python train.py --tren_csv_file train_ready_embeddings_esm2_t33_650M_UR50D.csv --test_csv_file test_ready_embeddings_esm2_t33_650M_UR50D.csv --model_name esm2_t33_650M_UR50D

train_embeddings_augmented_esm1v_t33_650M_UR90S_1.csv
train_embeddings_augmented_esm1v_t33_650M_UR90S_5.csv
train_embeddings_augmented_esm2_t33_650M_UR50D.csv
train_embeddings_augmented_esm2_t48_15B_UR50D.csv

test_embeddings_augmented_esm1v_t33_650M_UR90S_1.csv
test_embeddings_augmented_esm1v_t33_650M_UR90S_5.csv
test_embeddings_augmented_esm2_t33_650M_UR50D.csv
test_embeddings_augmented_esm2_t48_15B_UR50D.csv
"""

import argparse

import pandas as pd
import torch
from torch.optim.lr_scheduler import StepLR
from torch.utils.data import DataLoader, random_split
from tqdm import tqdm

# Create an ArgumentParser object
parser = argparse.ArgumentParser()

# Define command line arguments
parser.add_argument("--lr", type=float, default=0.001)
parser.add_argument("--batch_size", type=int, default=32)
parser.add_argument("--num_epochs", type=int, default=2)
parser.add_argument("--step_size", type=int, default=10)
parser.add_argument("--gamma", type=float, default=0.1)
parser.add_argument("--tm_mean", type=float, default=51.399974792034286)
parser.add_argument("--tm_std", type=float, default=12.075682499193073)
parser.add_argument("--tren_csv_file", type=str, default="train_ready_embeddings_esm2_t33_650M_UR50D.csv")
parser.add_argument("--test_csv_file", type=str, default="test_ready_embeddings_esm2_t33_650M_UR50D.csv")
parser.add_argument("--pred_csv_file", type=str, default="predictions_embeddings_esm2_t33_650M_UR50D.csv")

# Make a class for the dataset
class TrainData(torch.utils.data.Dataset):
    
        def __init__(self, csv_file):
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(csv_file)
    
            # Separate the target from the input
            self.target = df.pop("tm")
            self.input = df[["pH"] + [f"latent_{i}" for i in range(1280)]]
    
            # Convert the DataFrame into a PyTorch tensor
            self.tensor = torch.Tensor(self.input.values)

            # Convert target into a PyTorch tensor
            self.target = torch.Tensor(self.target.values)
            
            # Add batch dimmension to target
            self.target = self.target.unsqueeze(1)
    
        def __len__(self):
            return len(self.tensor)
    
        def __getitem__(self, idx):
            return self.tensor[idx], self.target[idx]

class TestData(torch.utils.data.Dataset):
        
            def __init__(self, csv_file):
                # Read the CSV file into a pandas DataFrame
                df = pd.read_csv(csv_file)

                self.seq_id = df.pop("seq_id")
                self.input = df[["pH"] + [f"latent_{i}" for i in range(1280)]]
        
                # Convert the DataFrame into a PyTorch tensor
                self.tensor = torch.Tensor(self.input.values)
        
            def __len__(self):
                return len(self.tensor)
        
            def __getitem__(self, idx):
                return self.tensor[idx], self.seq_id[idx]


class MLP(torch.nn.Module):
  def __init__(self,
  input_size = 1281,
  hidden_size = 256,
  output_size = 1,
  dropout = 0.5,
):
    super().__init__()
    self.fc1 = torch.nn.Linear(input_size, hidden_size)
    self.layer_norm1 = torch.nn.LayerNorm(hidden_size)
    self.dropout = torch.nn.Dropout(p=dropout)
    self.fc2 = torch.nn.Linear(hidden_size, hidden_size)
    self.layer_norm2 = torch.nn.LayerNorm(hidden_size)
    self.fc3 = torch.nn.Linear(hidden_size, output_size)

  def forward(self, x):
    x = self.fc1(x)
    x = self.layer_norm1(x)
    x = self.dropout(x)
    x = torch.nn.relu(x)
    x = self.fc2(x)
    x = self.layer_norm2(x)
    x = self.dropout(x)
    x = torch.nn.relu(x)
    x = self.fc3(x)
    return x

# Function for training an MLP
def train_mlp(model, train_loader, criterion, optimizer):

    # Use tqdm to create a progress bar for the training loop
    with tqdm(total=len(train_loader)) as pbar:
        
        # Loop over the training data
        for data in train_loader:

            # Update the progress bar
            pbar.update(1)

            # Get the input and target
            input, target = data

            # Forward pass
            output = model(input)

            # Compute the loss
            loss = criterion(output, target)

            # Backward pass
            optimizer.zero_grad()
            loss.backward()

            # Update weights
            optimizer.step()

# Function for testing an MLP
def test_mlp(model, test_loader, criterion):

    # Use tqdm to create a progress bar for the test loop
    with tqdm(total=len(test_loader)) as pbar:
        
        # Initialize a list to store the losses
        losses = []

        # Loop over the test data
        for data in test_loader:

            # Get the input and target
            input, target = data
    
            # Forward pass
            output = model(input)
    
            # Compute the loss
            loss = criterion(output, target)
    
            # Store the loss
            losses.append(loss.item())
    
        # Return the average loss
        return sum(losses) / len(losses)


if __name__ == "__main__":

    # Parse the command line arguments
    args = parser.parse_args()

    # Create a model
    model = MLP()

    # Create a criterion
    criterion = torch.nn.MSELoss()

    # Create an optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=args.lr)

    # Create a learning rate scheduler
    scheduler = StepLR(optimizer, step_size=args.step_size, gamma=args.gamma)

    # Load the dataset
    train_data_full = TrainData(args.train_csv_file)

    # Split the dataset into train and validation sets with a split ratio of 0.8
    train_size = int(0.8 * len(train_data_full))
    val_size = len(train_data_full) - train_size
    train_data, val_data = random_split(train_data_full, [train_size, val_size])

    # Create a dataloader for the training data
    train_loader = DataLoader(train_data, batch_size=args.batch_size, shuffle=True)

    # Create a dataloader for the validation data
    val_loader = DataLoader(val_data, batch_size=args.batch_size, shuffle=False)

    # Loop over the number of epochs
    for epoch in range(args.num_epochs):

        # Print the epoch number
        print(f"Epoch {epoch}")

        # Train the model
        train_mlp(model, train_loader, criterion, optimizer, num_epochs=args.num_epochs)

        # Update the learning rate
        scheduler.step()

        # Test the model
        test_loss = test_mlp(model, val_loader, criterion)
        print(f"Test loss: {test_loss:.4f}")

    # Create a dataloader for the test data
    test_loader = DataLoader(TestData(args.test_csv_file), batch_size=args.batch_size, shuffle=False)

    # Predict the labels for the test data
    predictions = {
        "seq_id": [],
        "tm": [],
    }
    for i, data in enumerate(test_loader):
        input, seq_id = data
        with torch.no_grad():
            output = model(input)

        # Normalizations for the train/test data
        tm_mean = args.tm_mean
        tm_std = args.tm_std

        # Denormalize the output
        output = output * tm_std + tm_mean

        predictions["seq_id"].extend(seq_id.numpy())
        predictions["tm"].extend(output.flatten().numpy())

    # Create a DataFrame with the predictions
    df = pd.DataFrame(predictions)

    # Save the predictions to a CSV file
    df.to_csv(args.pred_csv_file, index=False)