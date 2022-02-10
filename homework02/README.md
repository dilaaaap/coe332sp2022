
# Homework 2 - "Return of the JSON"

## Part 1 - 
This first python file generates tuples 5 times for each of siteid, latitude, longitude, and composition. The latitudes, longitudes, and compositions are obtained with random numbers. Following this, using a tuple to dict function, the tuples are grouped into dictionaries. Then they are appended to the list dictList. We then set the set up another dictionary with "sites" as the key with its value being dictList.

After this I import the data out into the jsonData.json file using json
## Part 2 - 
In this python file, I read in the json data from the jsonData.json. I then pull the list of dictionaries from the dictList and then further pull the dictionaries from each of those lists in a loop. Following this I pull the relevant values and calculate the necessary parameters, summing them up as I go. This information is then output.



NOTE:
The first python file must be run first for the second to work.