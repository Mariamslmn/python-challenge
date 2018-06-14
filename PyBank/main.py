import os
import csv



budget_data_1_csv_path = os.path.join("Resources","budget_data_1.csv")

with open(budget_data_1_csv_path, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    
    
    # Skip the first row of the csv
    csv_header = next(csv_reader)
    #print(f"CSV Header: {csv_header}")

    # Each row is read as a row
    # for row in csv_reader:
    # print(f"{row[0]} {row[1]}")

    # Financial Analysis:Total Months, Total Revenue, Average Revenue Change,Greatest Increase & Decrease in Revenue
    print("Financial Analysis")
    print("-------------------")

    # Total number of months is equal to the count of rows 
    data = list(csv_reader)
    row_count = len(data)
    print(f"Total months = {row_count}")

    # The total amount of revenue gained over the entire period
    sum = 0
   
    for  row in data:
        sum += int(row[1])


    print(f"Total Revenue = ${sum}")
    
    #Average Revenue
        #Average = round(sum / row_count)
        #print(f"Average Revenue = ${Average}")

   # Average Change 
    sumDiff=0
    allDiffs =[]
    for i   in range(len(data)):
       if (i>0):
            diff = int(data[i][1]) - int(data[i-1][1])
            sumDiff +=  abs(diff)
            allDiffs.append(diff)
              
        
    print(f"Average Change = ${round(sumDiff/(row_count-1))}")
     
    # The greatest increase in revenue (date and amount) over the entire period
    def min_max(allDiffs):
        return min(allDiffs), max(allDiffs)
        
    #"Unpack" the return into separate variables
    min_Diff, max_Diff = min_max(allDiffs)

    #Find index of the date of greatest decrease and increase 
    dec_ind = allDiffs.index(min_Diff) + 1
    inc_ind = allDiffs.index(max_Diff) + 1

    #Date of greatest decrease(date_dec) and greatest increase(date_inc) 
    date_dec = str(data[dec_ind][0])
    date_inc = str(data[inc_ind][0])

    print(f"Greatest Decrease in Revenue: {date_dec} (${min_Diff})")
    print(f"Greatest Increase in Revenue: {date_inc} (${max_Diff})")
   
    

     


        








