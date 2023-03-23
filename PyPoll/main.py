# Import os and csv modules
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
total_votes = 0
candidates_list = []

# Specify the file to write to
output_path = os.path.join("analysis", "result.csv")

results = open(output_path, 'w')

# Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        #    The total number of votes cast
        total_votes += 1

        candidates_list.append(row[2])

print("Election Results")
results.write("Election Results")
results.write('\n')

print("------------------------------")
results.write("------------------------------")
results.write('\n')

# Total number of votes
print(f'Total Votes: {total_votes}')
results.write(f'Total Votes: {total_votes}')
results.write('\n')

print("------------------------------")
results.write("------------------------------")
results.write('\n')

# A complete list of candidates who received votes
candidates_set = list(set(candidates_list))
candidates_set.sort()
percentage_list = []


# The percentage of votes each candidate won
for candidate in candidates_set:
    candidate_votes = candidates_list.count(candidate)
    percentage_votes = round(
        ((candidates_list.count(candidate))/total_votes)*100, 3)
    percentage_list.append(percentage_votes)

    print(f'{candidate} {percentage_votes}% ({candidate_votes})')
    results.write(f'{candidate} {percentage_votes}% ({candidate_votes})')
    results.write('\n')

print("--------------------------")
results.write("--------------------------")
results.write('\n')


max_index = percentage_list.index(max(percentage_list))
print(f'Winner: {candidates_set[max_index]}')
results.write(f'Winner: {candidates_set[max_index]}')
results.write('\n')

print("---------------------------")
results.write("--------------------------")
