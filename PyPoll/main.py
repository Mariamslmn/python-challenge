import os
import csv

election_data_1_csv = os.path.join("Resources", "election_data_1.csv")

# Open and read csv
with open(election_data_1_csv, newline="") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

# REad the header row firstn(skip this part if there is no header)
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")

     #Election Results:total number of votes cast,list of candidates,percentage of votes,total number of votes , and the winner
    print("Election Results")
    print("-----------------")

     # Total number of  is equal to the count of rows 
    election_data = list(csv_reader)
    row_count = len(election_data)
    print(f"Total Vote: {row_count}")
    print('--------------------')

   
    
    

def unique(election_data):
   
    unique_list = []
    
    # Using dictionary to store unique names and the frequency of their appearance
    # dictionary key is the candidate name and the value is the count/frequency
    my_dict = {}
    for row in election_data:
        # check if exists in unique_list or not
        y = str(row[2])
        
        if y not in unique_list:
            unique_list.append(y)
            my_dict[y]=1
        else:
            if my_dict.__contains__(y):
                my_dict[y] +=1
    print("------------------") 
    #using the frequeny stored in dictionary, we calculate the percentages and we get the name with max frequency
    nameWinner=""
    max=0
    for key, value in my_dict.items():
        # this if is to get the name of the candidate with max vote => winner
        if value>max:
            max=value
            nameWinner=key

        # Doing percentage calculation inside the print func  
        print(f" {key}: {round((value/row_count)*100)} % ({value})")
    print("------------------") 
    print(f" Winner is {nameWinner}") 
    print("------------------") 

        
     
unique(election_data)

