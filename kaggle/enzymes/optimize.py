"""
    Step 4: Optimize Hyperparameters for MLP/Data using HyperOpt
    ======================

"""

import hyperopt
from hyperopt import fmin, tpe, hp
from .train import perform_one_run

# Define the objective function
def objective(params):
  dataset = params['dataset']
  # Use the selected dataset to train a model and evaluate its performance
  # ...
  # Return the evaluation metric
  return metric


if __name__ == "__main__":

    # Define the search space for the "dataset" hyperparameter
    dataset_space = hp.choice('dataset', ['dataset1', 'dataset2', 'dataset3'])

    # Run the optimization
    best = fmin(objective, space=dataset_space, algo=tpe.suggest, max_evals=100)

    # Print the best dataset found
    print(best)


