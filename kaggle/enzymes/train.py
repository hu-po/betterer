"""Train an MLP to predict the melting temperature of a protein sequence."""

import argparse

import pandas as pd
import torch
from torch.optim.lr_scheduler import StepLR
from torch.utils.data import DataLoader, random_split
from torch.utils.tensorboard import SummaryWriter
from tqdm import tqdm
from typing import Any


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
parser.add_argument("--tren_csv_file", type=str,
                    default="train_ready_embeddings_esm2_t33_650M_UR50D.csv")
parser.add_argument("--test_csv_file", type=str,
                    default="test_ready_embeddings_esm2_t33_650M_UR50D.csv")
parser.add_argument("--pred_csv_file", type=str,
                    default="predictions_embeddings_esm2_t33_650M_UR50D.csv")
parser.add_argument("--log_dir", type=str, default="logs")
parser.add_argument("--run_name", type=str, default="debug")


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
  input_size=1281,
  hidden_size=256,
  output_size=1,
  dropout=0.5,
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


def train_mlp(model, train_loader, criterion, optimizer, epoch=None, tbwriter=None):

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

            # Log loss to tensorboard
            tbwriter.add_scalar('train/loss', loss.item(), epoch)

# Function for testing an MLP
def test_mlp(model, test_loader, criterion, epoch=None, tbwriter=None):

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

        # Cumulative loss
        cum_loss = sum(losses) / len(losses)

        # Log loss to tensorboard
        tbwriter.add_scalar('valid/loss', cum_loss, epoch)
    
        # Return the average loss
        return cum_loss

def perform_one_run(
    lr: float = 0.001,
    batch_size: int = 32,
    num_epochs: int = 2,
    step_size: int = 10,
    gamma: float = 0.1,
    tm_mean: float = 51.399974792034286,
    tm_std: float = 12.075682499193073,
    tren_csv_file: str = "train_ready_embeddings_esm2_t33_650M_UR50D.csv",
    test_csv_file: str = "test_ready_embeddings_esm2_t33_650M_UR50D.csv",
    pred_csv_file: str = "predictions_embeddings_esm2_t33_650M_UR50D.csv",
    log_dir: str = "logs",
    run_name: str = "debug",
) -> float:

    # Create a model
    model = MLP()

    # Create a criterion
    criterion = torch.nn.MSELoss()

    # Create an optimizer
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    # Create a learning rate scheduler
    scheduler = StepLR(optimizer, step_size=step_size, gamma=gamma)

    # Load the dataset
    train_data_full = TrainData(tren_csv_file)

    # Split the dataset into train and validation sets with a split ratio of 0.8
    train_size = int(0.8 * len(train_data_full))
    val_size = len(train_data_full) - train_size
    train_data, val_data = random_split(train_data_full, [train_size, val_size])

    # Create a dataloader for the training data
    train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)

    # Create a dataloader for the validation data
    val_loader = DataLoader(val_data, batch_size=batch_size, shuffle=False)

    # Create a tensorboard writer
    tbwriter = SummaryWriter(
        log_dir=log_dir,
        log_name=run_name,
    )

    # Best test loss
    best_test_loss = float("inf")

    # Loop over the number of epochs
    for epoch in range(num_epochs):

        # Print the epoch number
        print(f"Epoch {epoch}")

        # Train the model
        train_mlp(model, train_loader, criterion, optimizer, epoch=epoch, tbwriter=tbwriter)

        # Update the learning rate
        scheduler.step()

        # Test the model
        test_loss = test_mlp(model, val_loader, criterion, epoch=epoch, tbwriter=tbwriter)
        print(f"Test loss: {test_loss:.4f}")

        # Check if loss is better than the best loss
        if test_loss < best_test_loss:
            best_test_loss = test_loss
            print(f"Best test loss: {best_test_loss:.4f}")

    # Create a dataloader for the test data
    test_loader = DataLoader(TestData(test_csv_file), batch_size=batch_size, shuffle=False)

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
        tm_mean = tm_mean
        tm_std = tm_std

        # Denormalize the output
        output = output * tm_std + tm_mean

        predictions["seq_id"].extend(seq_id.numpy())
        predictions["tm"].extend(output.flatten().numpy())

    # Create a DataFrame with the predictions
    df = pd.DataFrame(predictions)

    # Save the predictions to a CSV file
    df.to_csv(pred_csv_file, index=False)

    return best_test_loss



if __name__ == "__main__":

    # Parse the command line arguments
    args = parser.parse_args()

    # Perform one run
    perform_one_run(**vars(args))

