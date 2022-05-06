# Water Turbidity

## Part 1 (the readme file)
In this homework, we further our usage of dictionaries and lists to calculate the turbidity of water for a real world application of python. The python script calculates the turbidity of the water and, if the water is not within acceptable values, how long it will take for the water to be acceptable again.


## Description
## Part2 
This first python file imports the turbidity_data.json and using three functions() averager(),calc_turbidity(), and calc_time()) calculates the turbidity of the water and the time for it to be clean using the 5 most recent detector current and calibration constant values.

Averager takes an input of 5 values and outputs the average.
```
def averager(val_1: float, val_2: float, val_3: float, val_4: float,val_5: float) -> float:
    sumVal = map( math.fsum, [val_1, val_2, val_3, val_4, val_5] )
    return (sumVal/5)
```
calc_turbidity reads in data from the json file and calculates the current turbidity values.

Finally, the calc_time function take the turbidity value and calculates how long it will take for it to be acceptable.
## Part 3 - Pytest for part 2
In the part 3, we run tests using the built in python function 'assert'. Running these tests ensure that the functions that we have written are performing as expected and to

For example:
 ```   
    assert type(calc_turbidity(data_11,21)) is float
```
will check if the output is a float 
```
    assert calc_turbidity(data_11,21) == 112.5
```
will check if the output is equal to the expected value

### Dependencies

* My program requires installations of python3,pytest, and 

Before running these files please download the turbidity water quality json data file from the link below:

[Water Quality Data](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json)
### Installing
To install python, if you have homebrew installed, you can run
```
brew install python3
```
Otherwise you will have to take it from the python website
### Executing program
i
* To run this file, after pulling the water data from the link above, compile and run part2.py. Then also run the test_part2.py to make sure the output is valid.
