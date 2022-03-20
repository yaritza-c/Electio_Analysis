from sys import orig_argv


counties =["Arapahoe","Denver","Jefferson"]
if counties[1]=='Denver':
    print(counties[1])
if counties[3]!= 'Jefferson':
    print(counties[2]) 
if "El Paso" in counties:
    print("El Paso is in the list of cunties")

else:
    print("El Paso is not the list of counties")

if "Arapahoe" in counties or "El Paso"in counties:
     print("Arapahoe or El Paso is not in the list of counties") 

else:
    print("Arapahoe and El Paso are not in the list of counties")

for county in counties:
    print (county)

numbers = [0, 1, 2, 3, 4]
for i in range(len(counties)):
    print(counties[i])

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict.keys:
    print(county)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    for value in county_dict.values():
        print(county_dict)

candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100.2f}% of the total votes.")

print(message_to_candidate)

