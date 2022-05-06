
# Return of the JSON,

In this file, we take data from a dataset, jsonData.json, and we show that we can access the data and modify it using python in an example scenario with randomly generated meteorites.

## Description - Part 1
This first python file generates tuples 5 times for each of siteid, latitude, longitude, and composition. The latitudes, longitudes, and compositions are obtained with random numbers. Following this, using a tuple to dict function, the tuples are grouped into dictionaries using this method:
```
def tuple2dict(tup,di):
    for a,b in tup:
        di.setdefault(a, []).append(b)
    return di
```
Which uses setdefault() to allow me to append the tuples together.
Then they are appended to the list dictList. We then set the set up another dictionary with "sites" as the key with its value being dictList.

After this I import the data out into the jsonData.json file using json for usage in part 2.
## Part 2 - 
In this python file, I read in the json data from the jsonData.json. I then pull the list of dictionaries from the dictList and then further pull the dictionaries from each of those lists in a loop. Following this I pull the relevant values and calculate the necessary parameters, summing them up as I go. This information is then output.
Starting with the original ml_data_analysis.py file, we first modify the main function to instead count the number of landings in each quadrant and then output them using a for loop.

### Dependencies

* My program requires python3 
### Installing

* Install python with homebrew
```
brew install python3
```
otherwise go to the python website

### Executing program

* To run this file, make sure to run the first file before running the second, or it will not function normally.
