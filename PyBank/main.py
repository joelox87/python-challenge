import csv
import numpy as np

csvpath = '/Users/joelox87/DataBootCamp/python-challenge/PyBank/Resources/budget_data.csv'

# Determine the amount of months
with open(csvpath, newline='') as csvfile:

  csvreader = csv.reader(csvfile, delimiter = ',')
  
  #Skip header row
  next(csvreader) 

  Months = []

  for row in csvreader:

    #print(row)

    #If the month is not already in the list then add it
    if row[0] not in Months:    
      Months.append(row[0])

# Calculate Net Total
with open(csvpath, newline='') as csvfile:

  csvreader = csv.reader(csvfile, delimiter = ',')
  
  #Skip header row
  next(csvreader)

  # Using float format in case there are decimals present
  Total = float(0)

  for row in csvreader:
    Total = Total + float(row[1])

# Calculate Average Change
with open(csvpath, newline='') as csvfile:

  csvreader = csv.reader(csvfile, delimiter = ',')
  
  #Skip header row
  next(csvreader)
  
  # Create an empty list to store profit/losses values
  Values = []
  # Create an empty list to store changes in profit/losses
  Changes = [] 

  for row in csvreader: 
    # Populate the list with the values of the second column converted as float
    Values.append(float(row[1]))

# Calculate changes
for i in range(1,len(Values)):
  # Creates list of changes
  Changes.append(Values[i] - Values[i-1])

# Calculate mean of changes
# Create a variable to sum all changes and set an initial value of 0
AccChanges = float(0)

for i in range(0,len(Changes)):
  # Summation of all changes
  AccChanges = AccChanges + Changes[i] 

# Mean calculation
AvChanges = AccChanges / len(Changes)

# Identify the Greatest Increase in Profits
# Create a variable to store the greatest increase value and set an initial value of 0
GreatestInc = float(0) 
# Create a variable to store the position of the greatest increase value and set an initial value of 0
GreatestIncPos = float(0) 

with open(csvpath, newline='') as csvfile:

  csvreader = csv.reader(csvfile, delimiter = ',')
  #Skip header row
  next(csvreader) 
  
  # Create an empty list to store Date values
  Date = [] 
  for row in csvreader: 
    # Populate the list with the values of the first column
    Date.append(row[0]) 

for i in range(0,len(Changes)):
  temp = float(Changes[i])
  if temp > GreatestInc:
    GreatestInc = temp
    GreatestIncPos = i

# Identify the Greatest Decrease in Profits
# Create a variable to store the greatest decrease value and set a very big initial value
GreatestDec = float(9999999999999999999999999999999999)
# Create a variable to store the position of the greatest decrease value and set an initial value of 0 
GreatestDecPos = float(0) 

for i in range(0,len(Changes)):
  temp = float(Changes[i])
  if temp < GreatestDec:
    GreatestDec = temp
    GreatestDecPos = i

# Printing analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months:",len(Months))
print("Total: $",int(Total), sep='')
print("Average  Change: $",round(AvChanges,2), sep='')
print("Greatest Increase in Profits: ", Date[GreatestIncPos+1], " ($", int(GreatestInc), ")", sep='')   #Need to add 1 to the position because the first position got dropped when the changes got calculated
print("Greatest Decrease in Profits: ", Date[GreatestDecPos+1], " ($", int(GreatestDec), ")", sep='')   #Need to add 1 to the position because the first position got dropped when the changes got calculated

# Export a text file with the results
# Path to the analysis.txt file to generate
csvexportpath = '/Users/joelox87/DataBootCamp/python-challenge/PyBank/Analysis/analysis.txt' 

# Open the txt file
with open(csvexportpath, 'w') as exportfile: 
  
  # Define the lines that will go into the file
  outputtxt = ['Financial Analysis\n',
               '----------------------------\n',
               'Total Months: ', str(len(Months)), '\n',
               'Total: $', str(int(Total)), '\n',
               'Average  Change: $', str(round(AvChanges,2)), '\n',
               'Greatest Increase in Profits: ', Date[GreatestIncPos+1], ' ($', str(int(GreatestInc)), ')', '\n',  #Need to add 1 to the position because the first position got dropped when the changes got calculated
               'Greatest Decrease in Profits: ', Date[GreatestDecPos+1], ' ($', str(int(GreatestDec)), ')']  #Need to add 1 to the position because the first position got dropped when the changes got calculated
  
  # Write the defined lines to the file
  exportfile.writelines(outputtxt) 