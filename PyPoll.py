# add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file path
file_to_save=os.path.join("analysis","election_analysis.txt")

#1. Initialize a total vote count
total_votes = 0

#Candidate Options
candidate_options=[]
# Declare the empty dictionary
candidate_votes={}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0 

# Open the election results and read the file.election_data = open(file_to_load, 'r')
with open(file_to_load)as election_data:

# To do: perform and analyze data here.
    #print (election_data)

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Print the header row
    headers=next(file_reader)
    #print(headers)

    # Print each row in the CSV file
    for row in file_reader:
        #print(row)
        #2. Add to the total vote count
        total_votes += 1

        # Print the candiate name from each row
        candidate_name = row [2]

        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Determine the percentage of votes for each candidate by looping through the counts
    # 1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes
        print(f"{candidate_name}: received {vote_percentage} % of the vote")

        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal
        print(f"{candidate_name}: {vote_percentage:.1f}%({votes:,})\n")

        # Determine winning vote count and candidate
        # Determine if the votes greater than the winning count
        if (votes > winning_count) and (vote_percentage> winning_percentage):
            # if true then set winning_count=votes and winning_percentage=
            # vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # and set the winning_candidate equal to the candidate's name
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")

#3. Print the total votes
#print(total_votes)
#print(candidate_options)
#print (candidate_votes)
print (winning_candidate_summary)

# Create a filename variable to a direct or indirect path to the file.
# assign a variable to save the file to path
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the open() function with the "w" mode we will write data to the file.
#open(file_to_save, "w")

#with open(file_to_load) as election_data:
    # To do: read and analyze the data here 
    # Read the file object with the reader function
    #new_func(election_data)
    #file_reader=csv.reader(election_data)

# Create a filename variable to a direct or indirect path to the file.
#file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
#outfile = open(file_to_save, "w")
# Write some data to the file.
#outfile.write("Hello World")

# Using the with statement open the file as a text file.
#with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    #everything after \n will be a new line
    #txt_file.write("Counties in the Election\n-------------------------")
    #txt_file.write("\nArapahoe\nDenver\nJefferson")
    #txt_file.write("Denver,")
    #txt_file.write("Jeffweaon")

# Close the file
#outfile.close()



# Close the file.
#election_data.close()


