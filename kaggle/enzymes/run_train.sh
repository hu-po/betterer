python train.py \
--batch_size 32 \
--num_epochs 50 \
--tren_csv_file train_ready_embeddings_esm2_t33_650M_UR50D.csv \
--test_csv_file test_ready_embeddings_esm2_t33_650M_UR50D.csv \
--pred_csv_file predictions_embeddings_esm2_t33_650M_UR50D.csv

python train.py \
--batch_size 32 \
--num_epochs 50 \
--tren_csv_file train_ready_embeddings_esm1v_t33_650M_UR90S_1.csv \
--test_csv_file test_ready_embeddings_esm1v_t33_650M_UR90S_1.csv \
--pred_csv_file predictions_embeddings_esm1v_t33_650M_UR90S_1.csv
