# Enzyme Stability Predition on Kaggle with ChatGPT

https://www.kaggle.com/competitions/novozymes-enzyme-stability-prediction/

https://chat.openai.com/chat


## How to use

Set up your local python environment
```
conda env create -f environment.txt
```

Clean the train and test data (remove NaNs, normalize `pH` and `tm`)
```
python clean.py
```

Convert protein sequence strings into embeddings using various pre-trained LLMs. Note that sequences are randomly cropped to prevent blowing up the GPU memory. This acts as a form of data augmentation.
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

Optimize Hyperparameters for training pipeline using HyperOpt.
```
python optimize.py
```

Use Tensorboard to visualize results, pick the best performing runs.
```
tensorboard --logdir='logs'
```

Combine predictions from best performing models (mixture of experts)
```
python submit.py
```
