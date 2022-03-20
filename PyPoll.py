# add our dependencies
import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file path
file_to_save=os.path.join("analysis","election_analysis.txt")

#1. Initialize a total vote count
total_votes = 0

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

#3. Print the total votes
print(total_votes)

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


