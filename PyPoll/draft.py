# Import os and csv modules
import os
import csv

csvpath = os.path.join('.', 'Resources', 'election_data.csv')
total_votes = 0
candidates_list = []

# Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # convert csv file to dictionary

    # Read each row of data after the header
    for row in csvreader:
        #    The total number of votes cast
        total_votes += 1

        # candidates_list.add(row[2])

        candidates_list.append(row[2])
# A complete list of candidates who received votes
candidates_set = list(set(candidates_list))
percentage_list = []
# The percentage of votes each candidate won
for candidate in candidates_set:
    candidate_votes = candidates_list.count(candidate)
    percentage_votes = round(
        ((candidates_list.count(candidate))/total_votes)*100, 3)
    percentage_list.append(percentage_votes)

    print(f'{candidate} {percentage_votes}% {candidate_votes}')

print(f'Total Votes: {total_votes}')
print()
print('candidate_set', candidates_set)
print('percen list', percentage_list)
max_index = percentage_list.index(max(percentage_list))
print('max index', max_index)
print('can max', candidates_set[max_index])
