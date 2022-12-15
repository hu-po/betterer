"""Combine the predictions from the best models."""
import pandas as pd

# read in the csv files using pandas
df1 = pd.read_csv('file1.csv')
df2 = pd.read_csv('file2.csv')
df3 = pd.read_csv('file3.csv')

# join the dataframes together on the 'seq_id' column
df = df1.merge(df2, on='seq_id', how='outer')
df = df.merge(df3, on='seq_id', how='outer')

# find all rows that have duplicate 'seq_id' values
duplicate_rows = df[df.duplicated(['seq_id'], keep=False)]

# average the values of the duplicate rows
for seq_id, rows in duplicate_rows.groupby('seq_id'):
    avg_values = rows.mean()
    print(f'Averaging values for seq_id={seq_id}: {rows.values}')
    df.loc[df['seq_id'] == seq_id, :] = avg_values

# remove duplicate rows
df = df.drop_duplicates(subset=['seq_id'])

# write the resulting dataframe to a csv file
df.to_csv('final_dataframe.csv')

