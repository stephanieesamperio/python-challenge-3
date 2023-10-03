import os
import csv
import operator
import sys

#creating a dictionary
candidate_names = {}

#Text file
console_window = sys.stdout #saves console for future refrence
f = open("../PyPoll/Analysis/analysis.txt", 'w')
sys.stdout = f

#Opening csv file
csvpath = os.path.join("..", 'PyPoll', 'Resources', 'election_data.csv')
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    
    #skipping the header
    reader = csv.reader(csvfile)
    next(reader, None)
    
    count = 0

    for row in csvreader:
        count = count +1
        
        name = row[2]
        if name in candidate_names:
            candidate_names[name] = candidate_names[name] + 1
        else:
            candidate_names[name] = 1
    
print("     Election Results")
print("---------------------------")

#The total number of votes cast
print("Total Votes: " + str(count))
print("---------------------------")

#A complete list of candidates who received votes, The percentage of votes each candidate won & The total number of votes each candidate won

percent_results = []
percent = 0

for candidate, number_votes in candidate_names.items():
    percent = ((number_votes/count)/0.01)
    
    x = round(percent,3)
    
    print(candidate + ": " + str(x) + "%" + " (" + str(number_votes) + ")")

#The winner of the election based on popular vote
    winner = max(candidate_names.items(), key=operator.itemgetter(1))[0]
    
print("---------------------------")

print("Winner: " + str(winner))

print("---------------------------")

#print to console
sys.stdout = console_window
f = open("../PyPoll/Analysis/analysis.txt", 'r') #reopens text file
print_console = f.readlines()
for line in print_console:
    print(line)

f.close()

