import os #to create file paths across operating systems
import csv #to get module for reading csv files

csvpath = os.path.join("Resources","budget_data.csv") #to set the location to read from


with open(csvpath) as csvfile: #to read the csv file with csv module
   csvreader = csv.reader(csvfile, delimiter=",")
   csv_header = next(csvreader)
   print('Financial Analysis')

   #create list from csvreader for readability
   data_list = []
   for row in csvreader:
      data_list.append(row)
   

   #get total number of months
   row_count = len(data_list)
   print("Total Months: " + str(row_count))

   #get net total amount for entire period
   Total = 0
   for row in data_list:
      Total += int(row[1])
   print("Total: $" + str(Total))

   #create list for only the profit/loss column
   current_value = []
   for row in data_list:
      current_value.append(row[1])
  

   #create offset list to subtract from the current_value list
   offset_value = list(current_value)
   del(offset_value[-1])
   offset_value.insert(0, '0')
   

   #use list comprehension to get the change between the values in the lists
   for row in range(len(offset_value)):
      value_change = [int(current_value[x]) - int(offset_value[x]) for x in range(len(offset_value))]
   

   #calculate the change in value for the entire dataset   
   total_value_change = 0
   for each in value_change:
      total_value_change -= each
  

   #average the changes for the provided time period
   average_value_change = total_value_change / row_count
   print('Average Change: $' + str(round(average_value_change,2)))

   #create separate list of dates
   date_list = []
   for row in data_list:
      date_list.append(row[0])
   
      
   #zip value_change list with the date list to re-pair the values
   combined_list = list(zip(value_change, date_list))
  
   #find the greatest increase in profits
   greatest_value_increase = max(combined_list)

   #find the greatest decrease in profits
   greatest_value_decrease = min(combined_list)

   #print both values
   print('Greatest Increase in Profits: $' + str(greatest_value_increase)[1:-1])
   print('Greatest Decrease in Profits: $' + str(greatest_value_decrease)[1:-1])

   
   bank_output_path = os.path.join('Analysis','Financial_Results.txt')  #to set the out results txt file location

   with open(bank_output_path, 'w') as file:  #to write the result values to the txt file
      file.write('Financial Analysis')
      file.write('\n''\n')
      file.write('--------------------------------')
      file.write('\n''\n')
      file.write("Total Months: " + str(row_count))
      file.write('\n''\n')
      file.write("Total: $" + str(Total))
      file.write('\n''\n')
      file.write('Average Change: $' + str(round(average_value_change,2)))
      file.write('\n''\n')
      file.write('Greatest Increase in Profits: $' + str(greatest_value_increase)[1:-1])
      file.write('\n''\n')
      file.write('Greatest Decrease in Profits: $' + str(greatest_value_decrease)[1:-1])