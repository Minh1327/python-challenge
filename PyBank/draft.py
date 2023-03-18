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
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        # The total number of months included in the dataset
        month_list.append(row[0])

        # The net total amount of "Profit/Losses" over the entire period
        net_total += int(row[1])

        print('month', row[0])
        # The changes in "Profit/Losses" over the entire period, and then the average of those changes
        print('previous_value', previous_value)
        current_value = int(row[1])
        print('current_value', current_value)
        change = current_value - previous_value
        print('change', change)
        change_list.append(change)
        print()
        previous_value = current_value

    # Remove the first item because there is no change in the first month
    change_list.pop(0)
    average_change = round((sum(change_list)/len(change_list)), 2)
    max_index = change_list.index(max(change_list))
    min_index = change_list.index(min(change_list))

    print('month', month_list)
    print()
    print('change list', change_list)
    print()
    print('max change: ', max(change_list))
    print('max index', max_index)
    print('max month', month_list[max_index+1])
    print()
    print('min change: ', min(change_list))
    print('min index', min_index)
    print('min month', month_list[min_index+1])

    # print(f'Total Months: {len(months)}')
    # print(f'Total: ${net_total}')
    # print(f'Average Change: ${average_change}')
    print(
        f'Greatest Increase in Profits: {month_list[max_index+1]} (${max(change_list)})')

    print(
        f'Greatest Decrease in Profits: {month_list[min_index+1]} (${min(change_list)})')


# The total number of months
