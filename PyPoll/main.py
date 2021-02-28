import csv

# Path to the csv file to open
csvpath = '/Users/joelox87/DataBootCamp/python-challenge/PyPoll/Resources/election_data.csv'

# Determine the total number of votes cast
Votes = int(0)

with open(csvpath, newline='') as csvfile:
  
  csvreader = csv.reader(csvfile, delimiter = ',')
  
  #Skip header row
  next(csvreader) 
  
  Votes= len(list(csvreader))

# Determine the list of candidates
Candidates = []

with open(csvpath, newline='') as csvfile:

  csvreader = csv.reader(csvfile, delimiter = ',')
  next(csvreader) #Skip header row
  
  for row in csvreader:
    #If the Candidate's name is not already in the list add it to the list of candidates
    if row[2] not in Candidates:    
      Candidates.append(row[2])

# Determine the amount and percentage of votes per candidate, and the election winner

## Variables to act as counters per candidate
Khan = int(0)
Correy = int(0)
Li = int(0)
OTooley = int(0)

with open(csvpath, newline='') as csvfile:

  csvreader = csv.reader(csvfile, delimiter = ',')
  #Skip header row
  next(csvreader) 
  
  for row in csvreader:
    #If the vote is for a candidate then increment this candidate's counter by 1  
    if row[2] == 'Khan':     
      Khan = Khan + 1
   
    if row[2] == 'Correy':    
      Correy = Correy + 1

    if row[2] == 'Li':     
      Li = Li + 1

    if row[2] == "O'Tooley":     
      OTooley = OTooley + 1

# Calculate percentages
KhanPerc = float(Khan/Votes)
CorreyPerc = float(Correy/Votes)
LiPerc = float(Li/Votes)
OTooleyPerc = float(OTooley/Votes)

## Calculate Winner
#Initialize variable to store the leading candidate's name
LeadingName = str() 
#Initialize variable to store the leading candidate's vote count
LeadingCount = int(0) 

#If "Khan" has more the most votes so far, make him the leading candidate
if Khan > LeadingCount:     
      LeadingName = "Khan"
      LeadingCount = Khan

#If "Correy" has more the most votes so far, make him the leading candidate
if Correy > LeadingCount:     
      LeadingName = "Correy"
      LeadingCount = Correy

#If "Li" has more the most votes so far, make him the leading candidate 
if Li > LeadingCount:    
      LeadingName = "Li"
      LeadingCount = Li

#If "O'Tooley" has more the most votes so far, make him the leading candidate
if OTooley > LeadingCount:     
      LeadingName = "O'Tooley"
      LeadingCount = OTooley

# Printing analysis to the terminal
print("Election Results")
print("-------------------------")
print("Total Votes:",Votes)
print("-------------------------")
print("Khan: ",format(KhanPerc*100, '.3f'),"% (",Khan,")",sep='')
print("Correy: ",format(CorreyPerc*100, '.3f'),"% (",Correy,")",sep='')
print("Li: ",format(LiPerc*100, '.3f'),"% (",Li,")",sep='')
print("O'Tooley: ",format(OTooleyPerc*100, '.3f'),"% (",OTooley,")",sep='')
print("-------------------------")
print("Winner:", LeadingName)
print("-------------------------")

# Export a text file with the results
# Path to the txt file to generate, including filename.
csvexportpath = '/Users/joelox87/DataBootCamp/python-challenge/PyPoll/Analysis/election.txt'

# Open the txt file
with open(csvexportpath, 'w') as exportfile: 
  
  # Define the lines that will go into the file
  outputtxt = ['Election Results\n',
               '-------------------------\n',
               'Total Votes:',str(Votes), '\n',
               '-------------------------\n',
               'Khan: ',str(format(KhanPerc*100, '.3f')),'% (',str(Khan),')\n',
               'Correy: ',str(format(CorreyPerc*100, '.3f')),'% (',str(Correy),')\n',
               'Li: ',str(format(LiPerc*100, '.3f')),'% (',str(Li),')\n',
               "O'Tooley: ",str(format(OTooleyPerc*100, '.3f')),'% (',str(OTooley),')\n',
               '-------------------------\n',
               'Winner:', LeadingName, '\n',
               '-------------------------']
  # Write the defined lines to the file
  exportfile.writelines(outputtxt) 