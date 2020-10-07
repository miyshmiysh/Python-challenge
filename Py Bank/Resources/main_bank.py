import os
import csv
# I creaded a file path to read the data
budget_data_csv = os.path.join('..','resources', 'budget_data.csv')


# created my variable lists
total_months = []
total_profit = []
monthly_profit_change = []
month_list = []

# I opeaned the file in another location so we can gather the data
with open(budget_data_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',' )
    header_row = next(csv_reader)
# started the for loop that will add the values to a list 
    for row in csv_reader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
        month_list.append(str(row[0]))
        

    # this will help me get my monthly change and also find the average change
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])
        increased_profit = max(monthly_profit_change)
        lowest_profit = min(monthly_profit_change)
        average_change = sum(monthly_profit_change) / len(monthly_profit_change) 
        x = monthly_profit_change.index(int(increased_profit))
        x2 = monthly_profit_change.index(int(lowest_profit))


print('Financial Analysis')
print('--------------------')
# i used len to find the total amount of months in the data 
print(f'Total Months: {(len(total_months))}')
print(f'Total: ${sum(total_profit)}')
# i use another function to format the decimal places 
print(f'Average change : ${average_change:.2f}')
print(f'Greatest Increase in profits:{month_list[x]}(${increased_profit})')
print(f'Greatest Decrease in profits:{month_list[x2]} (${lowest_profit})')

#  i was confused on how to export the text file so i did the best i could

output_file = os.path.join("analysis.txt")

with open(output_file, "W") as datafile:
    writter = csv.writter(datafile)
    writer.writerow([
        'Financial Analysis'
        '--------------------'
        f'Total Months: {(len(total_months))}'
        f'Total: ${sum(total_profit)}'
        f'Average change : ${average_change:.2f}'
        f'Greatest Increase in profits:{month_list[x]}(${increased_profit})'
        f'Greatest Decrease in profits:{month_list[x2]} (${lowest_profit})'])

