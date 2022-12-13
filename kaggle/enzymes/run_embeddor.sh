# TEST
export CSV_INPUT_FILE="test.csv"

python embeddor.py --csv_input_file=${CSV_INPUT_FILE} \
--model="esm2_t33_650M_UR50D" \
--csv_output_file="test_embeddings_esm2_t33_650M_UR50D.csv" \
--batch_size=1

python embeddor.py --csv_input_file=${CSV_INPUT_FILE} \
--model="esm1v_t33_650M_UR90S_1" \
--csv_output_file="test_embeddings_esm1v_t33_650M_UR90S_1.csv"
--batch_size=1

# TRAIN
export CSV_INPUT_FILE="train_filtered.csv"

python embeddor.py --csv_input_file=${CSV_INPUT_FILE} \
--model="esm2_t33_650M_UR50D" \
--csv_output_file="train_filtered_embeddings_esm2_t33_650M_UR50D.csv" \
--batch_size=1

python embeddor.py --csv_input_file=${CSV_INPUT_FILE} \
--model="esm2_t48_15B_UR50D" \
--csv_output_file="train_filtered_embeddings_esm2_t48_15B_UR50D.csv" \
--batch_size=1

python embeddor.py --csv_input_file=${CSV_INPUT_FILE} \
--model="esm1v_t33_650M_UR90S_1" \
--csv_output_file="train_filtered_embeddings_esm1v_t33_650M_UR90S_1.csv"

python embeddor.py --csv_input_file=${CSV_INPUT_FILE} \
--model="esm1v_t33_650M_UR90S_5" \
--csv_output_file="train_filtered_embeddings_esm1v_t33_650M_UR90S_5.csv"