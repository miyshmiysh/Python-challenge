import os
import csv
# I creaded a file path to read the data
election_data_csv = os.path.join('..','resources', 'election_data.csv')


# created my variable lists
total_votes =[]
total_votes_cast = []
canidates = []
khan= []
Correy =[]
li = []
Otooley = []

#  i statred the for loop which is going to read through the dates and transactions of the file
with open(election_data_csv, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    header_row = next(csv_reader)

    for row in csv_reader:
        total_votes.append(int(row[0]))

for i in range(len(total_votes)-1):
    total_votes_cast.append(total_votes[i+1]-total_votes[i])
    total_votes = sum(total_votes_cast)
    Khan = sum(total_votes_cast)
    Correy = sum(total_votes_cast)
    Li = sum(total_votes_cast)
    Otooley = sum(total_votes_cast)

    Khan_vote_percentage = sum(total_votes_cast) / len(total_votes)
    Correy_vote_percentage = sum(total_votes_cast) / len(total_votes)
    Khan_vote_percentage = sum(total_votes_cast) / len(total_votes)
    Li_vote_percentage = sum(total_votes_cast) / len(total_votes)
    Otooley_vote_percentage = sum(total_votes_cast) / len(total_votes)









print('Election Results')
print('--------------------')
print(f'Total votes: {sum(total_votes)}')
print('--------------------')
print(f'Khan: {Khan_vote_percentage}({Khan})')
print(f'Correy: {Correy_vote_percentage}({Correy})')
print(f'Li:{Li_vote_percentage}({Li})')
print(f'O Tooley: {Otooley_vote_percentage}({Otooley})')