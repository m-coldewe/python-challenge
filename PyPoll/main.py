import os #to create file paths across operating systems
import csv #to get module for reading csv files

csvpath = os.path.join("Resources","election_data.csv") #to set the location to read from

print('Election Results')

with open(csvpath) as csvfile:  #to open the csvfile
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #create list for data manipulation
    ballot_data=[]
    for row in csvreader:
        ballot_data.append(row)
    

    #get total number of votes
    vote_count = len(ballot_data)
    print('Total Votes: ' + str(vote_count)) 
    
    #get the list of candidates who received votes
    candidate_n = set()  #name set
    for row in ballot_data:  #loop through list to check rows for unique values
        candidate_n.add(row[2])  #add unique values to set
       

    candidate_list = list(candidate_n)  #translate set back to a list for use


    #set starting vote for each candidate
    can1_total = 0
    can2_total = 0
    can3_total = 0

    #loop through rows to count number of votes received
    for row in ballot_data:
        if candidate_list[0] in row:
            can1_total = can1_total + 1
        elif candidate_list[1] in row:
            can2_total = can2_total + 1
        elif candidate_list[2] in row:
            can3_total = can3_total + 1
    

    #get the percentage of votes each candidate won
    percent_can1 = can1_total / vote_count * 100
    percent_can2 = can2_total / vote_count * 100
    percent_can3 = can3_total / vote_count * 100

    #print the results of the voting
    print(candidate_list[0] + ': ' + str(round(percent_can1, 3)) + '% (' + str(can1_total) + ')')
    print(candidate_list[1] + ': ' + str(round(percent_can2, 3)) + '% (' + str(can2_total) + ')')
    print(candidate_list[2] + ': ' + str(round(percent_can3, 3)) + '% (' + str(can3_total) + ')')

    #declare the winner
    #the winning candidate is the candidate with the most votes
    if can1_total > can2_total and can3_total:
        winner = candidate_list[0]
    elif can2_total > can1_total and can3_total:
        winner = candidate_list[1]
    elif can3_total > can1_total and can2_total:
        winner = candidate_list[2]
    print('Winner: ' + winner)
        
output_path = os.path.join("Analysis","Elections_Results.txt")  #to set print-to location

with open(output_path, 'w') as file:  #to open tile

    file.write('Election Results')
    file.write('\n''\n')
    file.write(candidate_list[0] + ': ' + str(round(percent_can1, 3)) + '% (' + str(can1_total) + ')')
    file.write('\n')
    file.write(candidate_list[1] + ': ' + str(round(percent_can2, 3)) + '% (' + str(can2_total) + ')')
    file.write('\n')
    file.write(candidate_list[2] + ': ' + str(round(percent_can3, 3)) + '% (' + str(can3_total) + ')')
    file.write('\n''\n')
    file.write('Winner: ' + winner)