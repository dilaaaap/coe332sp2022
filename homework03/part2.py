import json
import math

""" Script to calculate turbidity conditions.

The script pulls the turbidity data from the json file and gets the average of the 5 most recent values
of the calibration constant and detector current to calculate whether the water is acceptable or not.
If the water is within acceptable parameters, then 
"""

with open('turbidity_data.json') as json_file:
    data = json.load(json_file)

turb_threshold = 1.0
decay_fact = 0.02
count = 0

def averager(val_1: float, val_2: float, val_3: float, val_4: float,val_5: float) -> float:
    sumVal = map( math.fsum, [val_1, val_2, val_3, val_4, val_5] )
    return (sumVal/5)

def calc_turbidity()):
for i in range(0,5):
    lister = []
    holderDict = {}
    leg = leg +1
    holderDict = holderList[i]
    holderLat = holderDict['calibration_constant']
    latVal = holderLat[0]
    holderLong = holderDict['detector_current']
    longVal = holderLong[0]
    s = 'leg = '+ repr(leg)
    lister.append(s)
    print(lister)
    latHold = holderDict['calibration_constant'][0]
    longHold = holderDict['detector_current'][0]
    totalTime = travelTime + sampleTime + totalTime

    return(turb)


def calc_time(turb_1:float) -> float:
    if turb_1 > 1.0
        print("Turbidity below threshold for safe use.")
        while turb_1 > 1.0
            count = count + 1
            turb_1 = turb_1*(1-decay_fact)
    elif turb_1 <= 1.0:
        print("Turbidity acceptable")
    return(count)

def main():
    a = calc_turbidity()
    b = calc_time(a)

