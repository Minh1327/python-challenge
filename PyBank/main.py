# Import os and csv modules
import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

month_list = []
net_total = 0
previous_value = 0
change_list = []

# Reading using CSV module
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # The total number of months included in the dataset
        month_list.append(row[0])

        # The net total amount of "Profit/Losses" over the entire period
        net_total += int(row[1])

        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        current_value = int(row[1])
        change = current_value - previous_value
        change_list.append(change)
        previous_value = current_value

    # Remove the first item because there is no change in the first month
    change_list.pop(0)
    average_change = round((sum(change_list)/len(change_list)), 2)
    max_index = change_list.index(max(change_list))
    min_index = change_list.index(min(change_list))

    print('Financial Analysis')
    print('-----------------------------')
    print(f'Total Months: {len(month_list)}')
    print(f'Total: ${net_total}')
    print(f'Average Change: ${average_change}')
    print(
        f'Greatest Increase in Profits: {month_list[max_index+1]} (${max(change_list)})')
    print(
        f'Greatest Decrease in Profits: {month_list[min_index+1]} (${min(change_list)})')

    # Specify the file to write to
output_path = os.path.join(".", "analysis", "result.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as result:

    # Write the rows to a text file
    result.write('Financial Analysis')
    result.write('\n')
    result.write('-------------------------')
    result.write('\n')
    result.write(f'Total Months: {len(month_list)}')
    result.write('\n')
    result.write(f'Total: ${net_total}')
    result.write('\n')
    result.write(f'Average Change: ${average_change}')
    result.write('\n')
    result.write(
        f'Greatest Increase in Profits: {month_list[max_index+1]} (${max(change_list)})')
    result.write('\n')
    result.write(
        f'Greatest Decrease in Profits: {month_list[min_index+1]} (${min(change_list)})')
