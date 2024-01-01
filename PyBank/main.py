import os #to create file paths across operating systems
#import os.path
import csv #to get module for reading csv files

csvpath = os.path.join("Resources","budget_data.csv") #to set the location to read from

with open(csvpath) as csvfile: #to read the csv file with csv module
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # data_list = []
    # for row in csvreader:
    #   data_list.append(row)

    #total number of months
    row_count = len(data_list)
    print("Total Months: " + str(row_count))

    print()
    print() 

    #net total of amount for entire period
    for row in data_list:
       amoumt= row in [row[1]]
       Total = (sum(int(amoumt)))
       print(Total)