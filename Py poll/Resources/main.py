import os
import csv
# I creaded a file path to read the data
election_data_csv = os.path.join('election_data.csv')


# created my variable lists
total_votes =[]
canidates_unique= []
canidates = []

#  i statred the for loop which is going to read through the votes of the file
with open(election_data_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header_row = next(csv_reader)
# stated the for loop to add the values to a list 
    for row in csv_reader:
        total_votes.append(int(row[0]))
        canidates.append(row[2])
    #    this for loop was to count the votes for each name specifically and how many votes they had 
    for name in canidates:
        if name not in canidates_unique:
            canidates_unique.append(name)



print('Election Results')
print('--------------------')
print(f'Total votes: {sum(total_votes)}')
print('--------------------')
for name in canidates_unique:
    print(f'{name}: {(canidates.count(name)/(total_votes)*100):.3f}% ({canidates.count(name)})')
print('--------------------')
print(f'Winner: {max(set(canidates), key = canidates.count)}')
print('--------------------')

#  i was confused on how to export the text file so i did the best i could
output_file = os.path.join("analysis_poll.txt")

with open(output_file, "W") as datafile:
    writter = csv.writter(datafile)
    writer.writerow(
    'Elevtion Results'
    '--------------------'
    f'Total votes: {sum(total_votes)}'
    '--------------------'
    f'{name}: {(canidates.count(name)/(total_votes)*100):.3f}% ({canidates.count(name)})'
    '--------------------'
    f'Winner: {max(set(canidates), key = canidates.count)}'
    '--------------------')
 