import csv
import os
#from pathlib import Path
path = os.path.join("..", "Resources", "budget_data.csv")
#path = Path("budget_data.csv”)
pl_change =[]
pl=[]

increase = ["", 0]
decrease = ["", 9999999999999999999]
total = 0
month_count = 0
with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the header
    header=next(csvreader) 
    print("Financial Analysis")
    print("______________________________")
    # loop through data to get total number of months
    first_row = next(csvreader)
    previous_net = int(first_row[1])
    month_count += 1
    total += int(first_row[1]) 
    for row in csvreader:
        #Get total months
        month_count = month_count + 1
        #Get net total amount
        total = total + int(row[1])
        
       #Get the average change
    
        net_change = int(row [1]) - previous_net 
        previous_net = int(row[1])
        pl_change += [net_change]
        if net_change > increase[1]:
            increase [0] = row[0]
            increase [1] = net_change
        if net_change < decrease[1]:
            decrease [0] = row[0]
            decrease [1] = net_change
    print(f"Total Months: {month_count}")
    print(f"total: {total}" )
    #loop through column 2 to get the change in p&l
    av =sum(pl_change)/len(pl_change)
    print(f"Average_change: {av}")
    print(f"Greatest Increase in Profits: {increase}")
    print(f"Greatest Decrease in Profits: {decrease}")
    

with open("output.txt", "w") as file_object:
    file_object.write(
    "Financial Analysis" "\n"
    "______________________________" "\n"
    f"Total Months: {month_count}" "\n"
    f"total: {total}" "\n"  
    f"Average_change: {av}""\n"
    f"Greatest Increase in Profits: {increase}""\n"
    f"Greatest Decrease in Profits: {decrease}" 
    )





   
   


   







    
  

