import csv
import numpy as np

csvpath = '/Users/joelox87/DataBootCamp/python-challenge/PyBank/Resources/budget_data.csv'

# Determine the amount of months
with open(csvpath, newline='') as csvfile:

  csvreader = csv.reader(csvfile, delimiter = ',')
  next(csvreader) #Skip header row

  Months = []

  for row in csvreader:

    # print(row)

    if row[0] not in Months:
      Months.append(row[0])

# Calculate Net Total
with open(csvpath, newline='') as csvfile:

  csvreader = csv.reader(csvfile, delimiter = ',')
  next(csvreader) #Skip header row

  Total = float(0)

  for row in csvreader:
    Total = Total + float(row[1])

print("Financial Analysis")
print("----------------------------")
print("Total Months:",len(Months))
print("Total: $",Total, sep='')