import os #to create file paths across operating systems
import csv #to get module for reading csv files

csvpath = os.path.join("Resources","budget_data.csv") #to set the location to read from

def blank_space():
   '''this function puts blank space between blocks of code for readability'''
   print()
   print()

with open(csvpath) as csvfile: #to read the csv file with csv module
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")


    blank_space

    data_list = []
    for row in csvreader:
      data_list.append(row)

    #total number of months
    row_count = len(data_list)
    print("Total Months: " + str(row_count))

    blank_space()

    #net total of amount for entire period
    Total = 0
    for row in data_list:
       Total += int(row[1])
    print("Total: $" + str(Total))

    blank_space()


    #changes in profit/losses over the entire period
    #create offset list to subtract from unaltered list
    #split data list into dates and values



    offset_list = list(data_list)
    del (offset_list[-1])
    offset_list.insert(1, '0')

    #convert both list values to integers
    #int_offset_list = []
    #for row in offset_list:
    #   int_offset_list = int(row[1])
    #   print(int_offset_list)
    print(offset_list)

    #subtract offset list from unaltered list and save as new list
    value_change = [list(data_list[-1])-list(offset_list[-1])]


   # print(value_change)
    #for number in reversed(value_change):
       
    
    print(value_change)

    #value_change = data_list[i]-data_list[i-1] for i in range(1, len(data_list)) 
  

    blank_space()

    #find the greatest increase in profits
    for row in data_list:  #subtract the previous month from the current month
       value_change = end_val - start_val
       greatest_value = max(value_change)  #find the largest change
    
    print(greatest_value)
    
