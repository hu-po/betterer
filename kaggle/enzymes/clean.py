"""Clean the data

    The raw data is in two files:
        - train.csv
        - test.csv

    This script will clean the data and save it to new files:
        - train_clean.csv
        - test_clean.csv
    
"""
import pandas as pd

# read the train.csv file into a dataframe called "train_df"
train_df = pd.read_csv("train.csv")

# read the test.csv file into a dataframe called "test_df"
test_df = pd.read_csv("test.csv")

# remove any rows that contain NaN or null values
print("Removing NaN values from train_df")
train_df_filtered = train_df.dropna()
print(f"Removed {len(train_df) - len(train_df_filtered)} rows from train_df, original length: {len(train_df)}")

# Join the train and test dataframes for normalization
combined_df = pd.concat([train_df_filtered, test_df])

# Normalize the "pH" column
print("Normalizing pH mean and std (using both train and test data)")
ph_mean = combined_df["pH"].mean()
ph_std = combined_df["pH"].std()
print(f"\t pH mean: {ph_mean}")
print(f"\t pH std: {ph_std}")
test_df["pH"] = (test_df["pH"] - ph_mean) / ph_std
train_df_filtered["pH"] = (train_df_filtered["pH"] - ph_mean) / ph_std

# Normalize the "tm" column
print("Normalizing tm mean and std (using only train data)")
tm_mean = train_df_filtered["tm"].mean()
tm_std = train_df_filtered["tm"].std()
print(f"\t tm_mean: {tm_mean}")
print(f"\t tm_std: {tm_std}")
train_df_filtered["tm"] = (train_df_filtered["tm"] - tm_mean) / tm_std

# Write test_df to a new csv file called "test_clean.csv"
test_df.to_csv("test_clean.csv", index=False)

# Write train_df_filtered to a new csv file called "train_clean.csv"
train_df_filtered.to_csv("train_clean.csv", index=False)
