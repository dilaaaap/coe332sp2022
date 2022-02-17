# Homework 3

In this homework, we further our usage of dictionaries and lists to calculate the turbidity of water for a real world application of python. The python script calculates the turbidity of the water and, if the water is not within acceptable values, how long it will take for the water to be acceptable again.


### Important- 
Before running these files please download the turbidity water quality json data file from the link below:

[Water Quality Data](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json)


## Part 2 - Turbidity of Water 
This first python file imports the turbidity_data.json and using three functions() averager(),calc_turbidity(), and calc_time()) calculates the turbidity of the water and the time for it to be clean using the 5 most recent detector current and calibration constant values.
## Part 3 - Pytest for part 2
In the part 3, we run tests using the built in python function 'assert'. Running these tests ensure that the functions that we have written are performing as expected and to

For example:
    
    assert type(calc_turbidity(data_11,21)) is float

will check if the output is a float 

    assert calc_turbidity(data_11,21) == 112.5

will check if the output is equal to the expected value




