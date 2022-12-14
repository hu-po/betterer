# python embeddor.py --csv_input_file="test.csv" \
# --model="esm2_t33_650M_UR50D" \
# --csv_output_file="test_embeddings_esm2_t33_650M_UR50D.csv" \
# --batch_size=1

# python embeddor.py --csv_input_file="train_filtered.csv" \
# --model="esm2_t33_650M_UR50D" \
# --csv_output_file="train_filtered_embeddings_esm2_t33_650M_UR50D.csv" \
# --batch_size=1

python embeddor.py --csv_input_file="test.csv" \
--model="esm1v_t33_650M_UR90S_1" \
--csv_output_file="test_embeddings_esm1v_t33_650M_UR90S_1.csv" \
--batch_size=1

python embeddor.py --csv_input_file="train_filtered.csv" \
--model="esm1v_t33_650M_UR90S_1" \
--csv_output_file="train_filtered_embeddings_esm1v_t33_650M_UR90S_1.csv" \
--batch_size=1

# python embeddor.py --csv_input_file="train_filtered.csv" \
# --model="esm2_t48_15B_UR50D" \
# --csv_output_file="train_filtered_embeddings_esm2_t48_15B_UR50D.csv" \
# --batch_size=1

# python embeddor.py --csv_input_file="train_filtered.csv" \
# --model="esm1v_t33_650M_UR90S_5" \
# --csv_output_file="train_filtered_embeddings_esm1v_t33_650M_UR90S_5.csv"