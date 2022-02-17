import part2

data_11 = [1,2,3,4,5]
data_12 = [6,7,8,9,10]
data_13 = [11,12,13,14,15]
data_14 = [16,17,18,19,20]

data_21 = [5,10,15,20,25]
data_22 = [30,35,40,45,50]
data_23 = [55,60,65,70,75]
data_24 = [80,85,90,95,100]

data_31 = 1
data_32 = 2
data_33 = 3
data_34 = 4


#tests for averager function
assert type(averager(data_11)) is float
assert averager(data_11) == 3.0
assert averager(data_12) == 8.0
assert averager(data_13) == 13.0
assert averager(data_14) == 18.0

#tests for calc_turbidity function
assert type(calc_turbidity(data_11,data_21)) is float
assert calc_turbidity(data11,data_21) == 112.5 
assert calc_turbidity(data12,data_22) == 320.0
assert calc_turbidity(data13,data_23) == 845.0
assert calc_turbidity(data14,data_24) == 1620.0

#tests for calc_time function
assert type(calc_time(data31)) is int
assert calc_time(data_31) == 0 
assert calc_time(data_32) == 35 
assert calc_time(data_33) == 55 
assert calc_time(data_34) == 69 

