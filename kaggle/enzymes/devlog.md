
## Replicate Steps

*Step 0* Set up your local python environment
```
conda env create -f environment.txt
```

*Step 1* Run the clean python file
```
> python clean.py
```

*Step 2* Convert protein sequence strings into embeddings using various pre-trained LLMs.
```
python embed.py --gpu 0 --csv_input_file train_clean.csv --csv_output_file train_esm1v_t33_650M_UR90S_1.csv 
--batch_size 4 --model esm1v_t33_650M_UR90S_1

python embed.py --gpu 0 --csv_input_file test_clean.csv --csv_output_file test_esm1v_t33_650M_UR90S_1.csv --batch_size 4 --model esm1v_t33_650M_UR90S_1

python embed.py --gpu 0 --csv_input_file train_clean.csv --csv_output_file train_esm1v_t33_650M_UR90S_5.csv 
--batch_size 4 --model esm1v_t33_650M_UR90S_5

python embed.py --gpu 0 --csv_input_file test_clean.csv --csv_output_file test_esm1v_t33_650M_UR90S_5.csv --batch_size 4 --model esm1v_t33_650M_UR90S_5

python embed.py --gpu 0 --csv_input_file train_clean.csv --csv_output_file train_esm2_t33_650M_UR50D.csv 
--batch_size 4 --model esm2_t33_650M_UR50D

python embed.py --gpu 0 --csv_input_file test_clean.csv --csv_output_file test_esm2_t33_650M_UR50D.csv --batch_size 4 --model esm2_t33_650M_UR50D
```

*Step 3* Train an MLP using embeddings/pH as input and tm as target
```

```

*Step 4* Optimize Hyperparameters for MLP
```
python optimize.py
```

*Step 5* Combine predictions from best performing models (mixture of experts)
```
python submit.py
```

## 15.12.2022


Monitor GPU memory on Windows Command Prompt:

```
nvidia-smi --query-gpu=timestamp,name,pci.bus_id,driver_version,pstate,pcie.link.gen.max,pcie.link.gen.current,temperature.gpu,utilization.gpu,utilization.memory,memory.total,memory.free,memory.used --format=csv -l 1
```

More concisely (every 100 milliseconds)

```
nvidia-smi --query-gpu=timestamp,name,utilization.gpu,memory.total,memory.free,memory.used,utilization.memory --format=csv -lms 100
```

We debug our embeddor, scripts to prepare TRAIN data

```
python embeddor.py --gpu 0 --csv_input_file train_filtered.csv --csv_output_file train_embeddings_augmented_esm1v_t33_650M_UR90S_1.csv --batch_size 4 --model esm1v_t33_650M_UR90S_1

python embeddor.py --gpu 0 --csv_input_file train_filtered.csv --csv_output_file train_embeddings_augmented_esm1v_t33_650M_UR90S_5.csv --batch_size 4 --model esm1v_t33_650M_UR90S_5

python embeddor.py --gpu 0 --csv_input_file train_filtered.csv --csv_output_file train_embeddings_augmented_esm2_t33_650M_UR50D.csv --batch_size 4 --model esm2_t33_650M_UR50D

python embeddor.py --csv_input_file train_filtered.csv --csv_output_file train_embeddings_augmented_esm2_t48_15B_UR50D.csv --batch_size 4 --model esm2_t48_15B_UR50D
```


We try and train our MLP with the following data

```

```

## 14.12.2022

Command to embedd the TRAIN sequences:

```
python embeddor.py --gpu 0 --csv_input_file train_filtered.csv --csv_output_file train_embeddings_augmented_esm1v_t33_650M_UR90S_1.csv --batch_size 2 --model esm1v_t33_650M_UR90S_1
python embeddor.py --gpu 0 --csv_input_file train_filtered.csv --csv_output_file train_embeddings_augmented_esm1v_t33_650M_UR90S_5.csv --batch_size 2 --model esm1v_t33_650M_UR90S_5
python embeddor.py --gpu 0 --csv_input_file train_filtered.csv --csv_output_file train_embeddings_augmented_esm2_t33_650M_UR50D.csv --batch_size 2 --model esm2_t33_650M_UR50D
python embeddor.py --gpu 0 --csv_input_file train_filtered.csv --csv_output_file train_embeddings_augmented_esm2_t48_15B_UR50D.csv --batch_size 2 --model esm2_t48_15B_UR50D
```

Command to embedd the TEST sequences:

```
python embeddor.py --gpu 0 --csv_input_file test_normalized.csv --csv_output_file test_embeddings_augmented_esm1v_t33_650M_UR90S_1.csv --batch_size 2 --model esm1v_t33_650M_UR90S_1
python embeddor.py --gpu 0 --csv_input_file test_normalized.csv --csv_output_file test_embeddings_augmented_esm1v_t33_650M_UR90S_5.csv --batch_size 2 --model esm1v_t33_650M_UR90S_5
python embeddor.py --gpu 0 --csv_input_file test_normalized.csv --csv_output_file test_embeddings_augmented_esm2_t33_650M_UR50D.csv --batch_size 2 --model esm2_t33_650M_UR50D
python embeddor.py --gpu 0 --csv_input_file test_normalized.csv --csv_output_file test_embeddings_augmented_esm2_t48_15B_UR50D.csv --batch_size 2 --model esm2_t48_15B_UR50D
```

Command to train the model:

```    
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
```