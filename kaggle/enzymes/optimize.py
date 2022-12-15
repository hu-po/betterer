"""Optimize Hyperparameters for MLP/Data using HyperOpt."""

import hyperopt
from hyperopt import fmin, tpe, hp
from .train import perform_one_run

# Define the objective function
def objective(params):
  
  # The run name will be used to create a folder for the run
  run_name = f"run_{params['dataset']}_{params['batch_size']}_{params['lr']}"

  # Perform the run
  best_loss = perform_one_run(
    run_name = run_name,
    lr = params["lr"],
    batch_size = params["batch_size"],
    tren_csv_file = f"train_{params['encoder']}.csv",
    test_csv_file = f"test_{params['encoder']}.csv",
    pred_csv_file = f"pred_{run_name}.csv",
  )
  return best_loss


if __name__ == "__main__":

    # Define the search space
    search_space = {
        'dataset': hp.choice('dataset', [
          'esm1v_t33_650M_UR90S_1',
          'esm1v_t33_650M_UR90S_5',
          'esm2_t33_650M_UR50D'
        ]),
        'batch_size': hp.choice('batch_size', [32, 64]),
        'lr': hp.loguniform('lr', -10, -1),
    }


    dataset_space = hp.choice('dataset', ['dataset1', 'dataset2', 'dataset3'])


    # Run the optimization
    best = fmin(objective, space=dataset_space, algo=tpe.suggest, max_evals=3)

    # Print the best dataset found
    print(best)


