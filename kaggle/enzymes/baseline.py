""" This script generates a baseline submission file for the Kaggle "Predicting the Melting Temperature of DNA" competition."""

import csv
import random

# Create a new csv file called "baseline"
with open("baseline.csv", "w") as csvfile:
    writer = csv.writer(csvfile)

    # Write the header
    writer.writerow(["seq_id", "tm"])

    # Read the "sample_submission.csv" file and write the "seq_id" column to the "baseline" file
    with open("sample_submission.csv") as samplesub:
        reader = csv.reader(samplesub)
        next(reader)  # skip the header row
        for row in reader:
            seq_id = row[0]

            # Sample a float number from a Gaussian distribution with mean 51.39 and std 12.075
            tm = random.gauss(51.39, 12.075)

            # Write the row to the "baseline" file
            writer.writerow([seq_id, tm])
