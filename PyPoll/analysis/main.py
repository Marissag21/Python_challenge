import csv
import os
path = os.path.join("..", "Resources", "election_data.csv")
from collections import Counter
candidate_count = {}
vote_count = 0
total = 0
candidate_list = []
candidate_vote = []
candidate_percent = []

#election_results = {}
final_winner = {}
final_candidate_info = []
with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #skip the header
    header=next(csvreader) 
    print("Election Results")
    print("______________________________")
    # loop through data to get total number of votes
    first_row = next(csvreader)
    previous_vote = int(first_row[0])
    vote_count += 1
    total += int(first_row[0]) 
    for row in csvreader:
        #Get total months
        vote_count = vote_count + 1
         
         #Get vote count per candidate
        total = total + int(row[0])
        if row[2] not in candidate_list:
           candidate_list.append(row[2]) 
           candidate_count[row[2]] = 0
        candidate_count[row[2]] +=1
    #for candidate  in candidate_list:this gives me 3 of each
    for candidate in candidate_count:
        #Got candidate names and votes and created a dictionary to hold them in
        count = candidate_count.get(candidate)    
        percent = round(int(count) / int(vote_count) * 100, 3) 
        candidate_percent.append(str(percent) + "%")
        winner = max(candidate_count, key=candidate_count.get)
        election_results = {
            "candidate": candidate,
            "percent": percent,
            "Candidate_count": count
        }
        final_candidate_info.append(election_results)
    
        #get winner
        final_winner = {"Winner": winner}
     
        #print(f'{election_results["candidate"]}: {election_results["percent"]}, {election_results["Candidate_count"]}')
        print(f'{election_results["candidate"]}: {election_results["percent"]}%, ({election_results["Candidate_count"]})')
    print("______________________________") 
    print(f"Total Votes: {vote_count}")    
    print("______________________________") 
   
    #print winner
print(final_winner)
     
    
  
#print textfile

with open("output.txt", "w") as file_object:
    file_object.write(
    "Election Results""\n"
    "______________________________""\n"
    f'{election_results["candidate"]}: {election_results["percent"]}%, ({election_results["Candidate_count"]})'"\n"
    "______________________________" "\n"
    f"Total Votes: {vote_count}"    "\n"
    "______________________________""\n"
    f"Winner:{winner}"
    )
  
   
   
  
    

       
       
    
    


    